#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 17
#define MAXK 32

int N, K;
int m[MAXN][MAXK];

int l[MAXN][MAXN];

inline int is_less(int a, int b) {
    for (int i = 0; i < K; i++) {
        if (m[a][i] >= m[b][i]) {
            return 0;
        }
    }
    return 1;
}

int st[MAXN], MAXCNT;
int back(int k, int count = 0) {
    if (count > MAXCNT) {
        return 0;
    }
    if (k == N) {
        return 1;
    }

    for (int i = 1; i <= count + 1; i++) {
        int ok = 1;
        for (int j = 0; j < k && ok; j++) {
            if (st[j] == i) {
                if (!is_less(k, j) && !is_less(j, k)) {
                    ok = 0;
                }
            }
        }

        if (!ok) {
            continue;
        }

        st[k] = i;
        if (back(k + 1, max(i, count))) {
            return 1;
        }
    }
    return 0;
}

int main() {
    freopen("C.in", "rt", stdin);
#ifndef DEBUG
    freopen("C.out", "wt", stdout);
#endif

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &N, &K);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < K; j++) {
                scanf("%d", m[i] + j);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                l[i][j] = is_less(i, j);
            }
        }

        for (MAXCNT = 1; MAXCNT <= N; MAXCNT++) {
            if (back(0)) {
                printf("Case #%d: %d\n", t, MAXCNT);
                break;
            }
        }
    }

/*    memset(bst, 0x3f, sizeof(bst));
    bst[0] = 0;

    for (int st = 0; st < (1 << N); st++) {
        vector<int> root;
        for (int i = 0; i < N; i++) {
            if (!(st & (1 << i))) {
                continue;
            }

            int ok = 1;
            for (int j = 0; j < N && ok; j++) {
                if (!(st & (1 << j))) {
                    continue;
                }

                if (l[i][j]) {
                    ok = 0;
                }
            }

            if (ok) {
                root.push_back(i);
            }
        }

        printf("%d\n", st);
        for (size_t k = 0; k < root.size(); k++) {
            printf("%d ", root[k]);
        }
        printf("\n");

        for (int i = 0; i < N; i++) {
            if (st & (1 << i)) {
                continue;
            }
        }
    }
    */

    return 0;
}


