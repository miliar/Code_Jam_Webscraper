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

const char *file_name = "A-large.in";

char mat[64][64];

int main() {
    FILE *f = fopen(file_name, "rt");
    int num_tests;
    fscanf(f, "%d\n", &num_tests);
    int N;
    REP(t, num_tests) {
        fscanf(f, "%d\n", &N);
        REP(i, N) fscanf(f, "%s\n", mat[i]);
        VI val;
        REP(i, N) {
            int j;
            for (j = N - 1; j >= 0; --j) if (mat[i][j] == '1') {
                val.pb(j + 1);
                break;
            }
            if (j < 0) {
                val.pb(0);
            }
        }
        //REP(i, val.sz) printf("%d ", val[i]);
        //printf("\n");
        int sol = 0;
        FOR(i, 1, N) {
            REP(j, val.sz) {
                if (val[j] <= i) {
                    VI new_val;
                    REP(k, val.sz) {
                        if (k != j) {
                            new_val.pb(val[k]);
                        }
                    }
                    sort(ALL(new_val));
                    bool ok = true;
                    REP(k, new_val.sz) {
                        if (new_val[k] > i + 1 + k) {
                            ok = false;
                        }
                    }
                    if (ok) {
                        sol += j;
                        val.erase(val.begin() + j);
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", t + 1, sol);
    }
    fclose(f);
    return 0;
}

