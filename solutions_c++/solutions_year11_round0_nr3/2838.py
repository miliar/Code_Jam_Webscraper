#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

#define PB push_back
#define PII pair<int, int>
#define SZ(x) ((int)((x).size()))
#define OUT(x) printf(#x" %d\n", x)
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)

const int maxn = 1000 + 10;
const int inf = (-1u) >> 1;

int Case = 1;
int n, a[maxn];

void init() {
    scanf ("%d", &n);
    REP(i,n) {
        scanf ("%d", &a[i]);
    }
}

void solve() {
    printf ("Case #%d: ", Case++);
    int sum = 0, mina = inf, sumc = 0;
    REP(i,n) {
        sum += a[i];
        mina = min(mina, a[i]);
        sumc ^= a[i];
    }
    if (sumc == 0) {
        printf ("%d\n", sum - mina);
    } else {
        puts ("NO");
    }
}

//#define SMALL
#define LARGE

int main() {
    string name = "C";
    #ifdef SMALL
    freopen ((name + "-small-attempt0.in").c_str(), "r", stdin);
    freopen ((name + "-small.out").c_str(), "w", stdout);
    #endif
    #ifdef LARGE
    freopen ((name + "-large.in").c_str(), "r", stdin);
    freopen ((name + "-large.out").c_str(), "w", stdout);
    #endif
    
    int testCase;
    scanf ("%d\n", &testCase);
    while (testCase--) {
        init();
        solve();
    }
    
    return 0;
}


