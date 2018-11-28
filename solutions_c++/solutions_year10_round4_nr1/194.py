#include <cstdio>
#include <deque>
#include <vector>

using namespace std;

int N, MIN = 0x3f3f3f3f;
vector<deque<int> > d, newD, finD;

inline int checkHorizontal(vector<deque<int> > &d) {
    for (size_t line = 0; line < d.size(); line++) {
        int l = 0, r = (int)d[line].size() - 1;
        for (; l < r; l++, r--) {
            if (d[line][l] != d[line][r]) {
                if (d[line][l] == -1) {
                    d[line][l] = d[line][r];
                } else if (d[line][r] == -1) {
                    d[line][r] = d[line][l];
                } else {
                    return false;
                }
            }
        }
    }
    return true;
}

inline int checkVertical(vector<deque<int> > &d) {
    int l = 0, r = (int)d.size() - 1;
    for (; l < r; l++, r--) {
        for (size_t col = 0; col < d[l].size(); col++) {
            if (d[l][col] != d[r][col]) {
                if (d[l][col] == -1) {
                    d[l][col] = d[r][col];
                } else if (d[r][col] == -1) {
                    d[r][col] = d[l][col];
                } else {
                    return false;
                }
            }
        }
    }
    return true;
}

inline void solve() {
    for (int h = 0; h <= N; h++) {
        newD.clear();
        int length = 1, delta = 1;
        int added = 0;
        deque<int> line;
        for (int i = 0; i < h; i++) {
            line.push_back(-1);
            newD.push_back(line);
            added += length;
            length += delta;
        }
        for (int i = 0; i < 2 * N - 1; i++) {
            newD.push_back(d[i]);
            for (; (int)newD.back().size() < length; ) {
                newD.back().push_back(-1);
                added += 1;
            }
            length += delta;
            if (length == (N + h)) {
                delta = -1;
            }
        }
        for (int i = 0; i < h; i++) {
            newD.push_back(line);
            added += length;
            length += delta;
            line.pop_back();
        }

        if (added >= MIN) {
            continue;
        }

        for (int v = 0; v <= N + h; v++) {
            if (added >= MIN) {
                continue;
            }

            length = 1; delta = 1;
            finD = newD;
            int addedNow = added;
            finD.resize(2 * (N + h + v) - 1);
            for (int i = 0; i < 2 * (N + h + v) - 1; i++) {
                for (; (int)finD[i].size() + 2 <= length; ) {
                    finD[i].push_front(-1);
                    finD[i].push_back(-1);
                    addedNow += 2;
                }
                for (; (int)finD[i].size() < length; ) {
                    finD[i].push_back(-1);
                    addedNow += 1;
                }

                length += delta;
                if (length == (N + h + v)) {
                    delta = -1;
                }
            }
            if (addedNow >= MIN) {
                continue;
            }

            if (!checkHorizontal(finD)) {
                continue;
            }
            if (!checkVertical(finD)) {
                continue;
            }

            MIN = min(MIN, addedNow);
            /*
            {
                printf("%d %d\n", h, v);
                for (size_t k = 0; k < finD.size(); k++) {
                    printf("\t");
                    for (size_t l = 0; l < finD[k].size(); l++) {
                        printf("%2d ", finD[k][l]);
                    }
                    printf("\n");
                }
                printf("\n");
            }
            */
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        d.clear();
        int len = 1, delta = 1;
        for (int i = 0; i < 2 * N - 1; i++) {
            deque<int> line;
            for (int j = 0; j < len; j++) {
                int val;
                scanf("%d", &val);
                line.push_back(val);
            }
            d.push_back(line);
            len += delta;
            if (len == N) {
                delta = -1;
            }
        }

        MIN = 0x3f3f3f3f;
        solve();
        for (size_t i = 0; i < d.size(); i++) {
            size_t l = 0, r = d[i].size() - 1;
            for (; l < r; l++, r--) {
                swap(d[i][l], d[i][r]);
            }
        }
        solve();
        for (size_t l = 0, r = d.size() - 1; l < r; l++, r--) {
            swap(d[l], d[r]);
        }
        solve();
        for (size_t i = 0; i < d.size(); i++) {
            size_t l = 0, r = d[i].size() - 1;
            for (; l < r; l++, r--) {
                swap(d[i][l], d[i][r]);
            }
        }
        solve();

        printf("Case #%d: %d\n", t, MIN);
    }
    return 0;
}
