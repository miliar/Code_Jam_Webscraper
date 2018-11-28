#include <cstdio>
#include <cstring>
//#include <string>
//#include <vector>
//#include <deque>
//#include <set>
//#include <map>
//#include <numeric>
//#include <algorithm>
//#include <functional>
using namespace std;

#define FOR(i, n) for (i = 0; i < (n); ++i)
#define FOR1(i, n) for (i = 1; i <= (n); ++i)
#define ROF(i, n) for (i = (n) - 1; i >= 0; --i)
#define ROFN(i, n) for (i = (n); i > 0; --i)
//#define debug(what...) fprintf(stderr, what) 
#define debug(what...)

typedef long long llong;
typedef unsigned long long ullong;

void redirect() {
//    freopen("C-test.in", "rt", stdin);
//    freopen("C-small-attempt0.in", "rt", stdin);
//    freopen("C-small-attempt0.out", "wt", stdout);
    freopen("C-large.in", "rt", stdin);
    freopen("C-large.out", "wt", stdout);
}

//const ullong MOD = 1000000007;

const int MOD = 10000;
const char pat[] = "welcome to code jam";
char s[500 + 1];
short int a[20][500];

int main() {
    int tn, tt;
    int i, j, k, m, n;
    int x, y, z;
    redirect();
    m = strlen(pat);
    scanf("%d\n", &tn);
    FOR1(tt, tn) {
        gets(s);
        debug("Case #%d: %s\n", tt, s);
        n = strlen(s);
        if (n < m) {
            k = 0;
        }
        else {
            FOR(i, m) {
                for (j = i; j < n; ++j) {
                    a[i][j] = (j == 0) ? 0 : a[i][j-1];
                    if (s[j] == pat[i]) {
                        a[i][j] += (i == 0) ? 1 : a[i-1][j-1];
                        a[i][j] %= MOD;
                    }
                }
            }
            k = a[m-1][n-1];
        }
        printf("Case #%d: %d%d%d%d\n", tt, k/1000, k%1000/100, k%100/10, k%10);
    }

    return 0;
}
