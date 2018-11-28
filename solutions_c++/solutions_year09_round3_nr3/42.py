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

const char *file_name = "C-large.in";

VI prison;
int cache[128][128];

int dyn(int l, int r) {
    if (l + 1 == r) return 0;
    if (cache[l][r] != -1) return cache[l][r];
    int mn = INF;
    for (int i = l + 1; i < r; ++i) {
        int tmp = prison[r] - prison[l] - 2 + dyn(l, i) + dyn(i, r);
        if (mn > tmp) {
            mn = tmp;
        }
    }
    //fprintf(stderr, "(%d, %d) = %d\n", l, r, mn);
    return cache[l][r] = mn;
}

int main() {
    FILE *f = fopen(file_name, "rt");
    int num_tests;
    fscanf(f, "%d", &num_tests);
    REP(t, num_tests) {
        int P, Q;
        fscanf(f, "%d %d", &P, &Q);
        prison.clear();
        prison.pb(0);
        REP(i, Q) {
            int x;
            fscanf(f, "%d", &x);
            prison.pb(x);
        }
        prison.pb(P + 1);
        REP(i, prison.sz) REP(j, prison.sz) cache[i][j] = -1;
        printf("Case #%d: %d\n", t + 1, dyn(0, prison.sz - 1));
    }
    fclose(f);
    return 0;
}
