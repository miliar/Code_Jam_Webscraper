#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int maxn = 1000 + 10;
const int inf = (-1u) >> 1;

int Case = 1, n, k;

void init() {
    scanf ("%d%d", &n, &k);
}

void solve() {
    printf ("Case #%d: ", Case++);
    printf ("%s\n", k % (1 << n) == (1 << n) - 1? "ON" : "OFF");
}

//#define SMALL
#define LARGE

int main() {
    string name = "A";
    #ifdef SMALL
    freopen ((name + "-small-attempt2.in").c_str(), "r", stdin);
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

