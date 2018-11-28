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

char msg[128];
int let2dig[256];

int main() {
    FILE *f = fopen(file_name, "rt");
    int num_tests;
    fscanf(f, "%d\n", &num_tests);

    REP(t, num_tests) {
        fscanf(f, "%s\n", msg);
        //printf("msg = %s\n", msg);
        VI digs;
        digs.pb(1);
        REP(i, 256) let2dig[i] = -1;
        let2dig[msg[0]] = 1;
        int cnt = 1;
        for (int i = 1; msg[i]; ++i) {
            if (let2dig[msg[i]] == -1) {
                if (cnt == 1) let2dig[msg[i]] = 0;
                else let2dig[msg[i]] = cnt;
                ++cnt;
            }
            digs.pb(let2dig[msg[i]]);
        }
        /*
        for (int i = 0; i < digs.sz; ++i) {
            printf("%d ", digs[i]);
        }
        printf("\n");
        */
        if (cnt == 1) {
            cnt = 2;
        }
        long long sol = 0, pow = 1;
        for (int i = digs.sz - 1; i >= 0; --i) {
            sol += (long long) digs[i] * pow;
            pow *= (long long) cnt;
        }
        printf("Case #%d: %lld\n", t + 1, sol);
    }
    fclose(f);
    return 0;
}

