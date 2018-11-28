#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <sstream>
#include <vector>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
using namespace std;

#define REP(i, N) for (int i = 0; i < (int)(N); ++i)
#define FOR(i, N, M) for (int i = (int)(N); i <= (int)(M); ++i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); --i)
#define FORI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define TIP(x) (cerr << #x << " = " << (x) << endl)
#define sz size()
#define pb push_back
#define mp make_pair
#define pf first
#define ps second
#define INF 1000000000
#define ALL(x) (x).begin(), (x).end()
#define CLEAR(X) (memset(X, 0, sizeof(X)))
typedef vector<int> VI;
typedef vector<string> VS;

const char *file_name = "C-small-attempt1.in";

int v[128][128];
int mat[128][128];
int N, T;

inline int sgn(int x) {
    return x < 0 ? -1 : x > 0 ? 1 : 0;
}

int inter(int a, int b) {
    REP(i, T) {
        if (v[a][i] == v[b][i] || sgn(v[a][i] - v[b][i]) != sgn(v[a][0] - v[b][0])) {
            return 1;
        }
    }
    return 0;
}

int dst[1 << 16];
int q[1 << 16];
bool ok[1 << 16];

bool is_ok(int cfg) {
    REP(i, N) if (cfg & (1 << i)) {
        FOR(j, i+1, N-1) if (cfg & (1 << j)) {
            if (mat[i][j]) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    FILE *f = fopen(file_name, "rt");
    int num_tests;
    fscanf(f, "%d", &num_tests);
    REP(t, num_tests) {
        fscanf(f, "%d %d", &N, &T);
        REP(i, N) REP(j, T) {
            fscanf(f, "%d", v[i] + j);
        }
        CLEAR(mat);
        REP(i, N) FOR(j, i+1, N-1) {
            mat[i][j] = inter(i, j);
        }
        /*
        REP(i, N) {
            REP(j, N) {
                printf("%d", mat[i][j]);
            }
            printf("\n");
        }
        */

        q[0] = 0;
        REP(cfg, 1 << N) {
            ok[cfg] = is_ok(cfg);
        }
        dst[0] = 1;
        CLEAR(dst);
        int l, r;
        VI bts;
        for (l = r = 0; l <= r; l++) {
            int cfg = q[l];
            bts.clear();
            bts.reserve(N);
            REP(i, N) if (!(cfg & (1 << i))) {
                bts.pb(i);
            }
            REP(x, 1 << (bts.sz)) {
                int cx = 0;
                REP(i, bts.sz) {
                    if (x & (1 << i)) {
                        cx += (1 << bts[i]);
                    }
                }
                if (ok[cx] && dst[cfg + cx] == 0) {
                    q[++r] = cfg + cx;
                    dst[cfg + cx] = dst[cfg] + 1;
                }
            }
        }
        printf("Case #%d: %d\n", t + 1, dst[(1 << N) - 1] - 1);
    }
    fclose(f);
    return 0;
}

