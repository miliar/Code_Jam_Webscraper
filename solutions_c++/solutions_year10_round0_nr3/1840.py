#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
//#define DEBUG
#ifdef DEBUG
#define printd(args...) printf(args)
#else
#define printd(args...)
#endif
#define scand(args...) if(scanf(args) == EOF) { \
   fprintf(stderr, "FATAL ERROR: unexpected end of file\n"); \
   exit(1); \
}
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(),(c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define PF push_front
#define MP make_pair
const int INF = 1000000001;
const double EPS = 10e-9;

const int MAX = 1010;

int r, k, n;
int g[MAX];

void wczytaj() {
    scand("%d%d%d", &r, &k, &n);
    REP(i,n) scand("%d", &g[i]);
}

void play(int nr) {
    VI step(MAX, -1);
    vector<LL> money(MAX, -1);

    int x = 0;
    int v = 0;
    LL sum = 0;
    int act = 0;
    int z = 0;

    while (x < r && step[v] == -1) {
        step[v] = x;
        money[v] = sum;

        for (act = 0, z = 0; z<n && act+g[v] <= k; v = (v+1)%n, z++)
            act += g[v];
        sum += act;
        x++;
    }

    r -= x;
    if (r > 0) {
        sum += (sum - money[v]) * (r / (x - step[v]));
        r %= (x - step[v]);
        while (r > 0) {
            for (act = 0, z = 0; z<n && act+g[v] <= k; v = (v+1)%n, z++)
                act += g[v];
            sum += act;
            r--;
        }
    }

    printf("Case #%d: %lld\n", nr, sum);
}

int main() {
    int t;
    scand("%d", &t);
    REP(i, t) {
        wczytaj();
        play(i+1);
    }
    return 0;
}
