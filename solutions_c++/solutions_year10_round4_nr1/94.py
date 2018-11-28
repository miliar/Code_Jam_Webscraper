#include <cstdio>
#include <vector>
using namespace std;

const int MAX_N = 64;

int n;
int a[MAX_N][MAX_N];
int offx, offy;

void add(vector<int> &v, int i, int j) {
    if (i < offx || i >= offx + n || j < offy || j >= offy + n)
        return;
    v.push_back(a[i - offx][j - offy]);
}

bool isok(vector<int> &v) {
    for (int i = 0; i < (int)v.size(); ++i)
        for (int j = i + 1; j < (int)v.size(); ++j)
            if (v[i] != v[j])
                return false;
    return true;
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test_no = 1; test_no <= t; ++test_no) {
        scanf("%d", &n);
        int i = 0, j = 0;
        for (int cnt = 0; cnt < n * n; ++cnt) {
            scanf("%d", &a[i][j]);
            if (j == n - 1) {
                j = i + 1;
                i = n - 1;
            } else if (i == 0) {
                i = j + 1;
                j = 0;
            } else {
                --i;
                ++j;
            }
        }

        int sol = n;
        while (true) {
            bool ok = false;

            for (offx = 0; !ok && offx + n <= sol; ++offx)
                for (offy = 0; !ok && offy + n <= sol; ++offy) {
                    bool good = true;

                    for (int i = 0; good && i < sol; ++i)
                        for (int j = 0; good && j < sol; ++j) {
                            vector<int> v;

                            add(v, i, j);
                            add(v, j, i);
                            add(v, sol - j - 1, sol - i - 1);
                            add(v, sol - i - 1, sol - j - 1);

                            good &= isok(v);
                        }

                    ok |= good;
                }

            if (ok) break;
            ++sol;
        }
        printf("Case #%d: %d\n", test_no, sol * sol - n * n);
    }
}
