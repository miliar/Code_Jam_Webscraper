#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <numeric>
#include <algorithm>
using namespace std;
#ifdef DEBUGRUN
#define LOG(a) (cerr<<__LINE__<<": "#a" = "<<(a)<<endl)
#define DBG(...) (__VA_ARGS__)
#else
#define LOG(...) ((void)0)
#define DBG(...) ((void)0)
#endif
#define rep(i, n) for(int i=0; i<(int)(n); i++)
#define mp make_pair
#define foreach(it, c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
typedef long long Int;
#define INF MY_INFINITY

double p[2000][2000], dp[2000];

int main() {
    p[0][0] = 1;
    for(int i=1; i<1010; i++) {
        double f=1;
        p[i][0] = 1;
        for(int j=1; j<=i; j++) {
            f /= j; // f = 1/(j!)
            p[i][j] = p[i-j][0]*f;
            p[i][0] -= p[i][j];
        }
    }
    dp[0] = 0;
    for(int i=1; i<1010; i++) {
        double s = 0;
        for(int j=1; j<=i; j++) s += p[i][j]*dp[i-j];
        dp[i] = (1+s)/(1-p[i][0]);
    }
    int T;
    scanf("%d", &T);
    rep(q, T) {
        int n;
        scanf("%d", &n);
        int k=0;
        rep(i, n) {
            int a;
            scanf("%d", &a);
            if(i+1!=a) k++;
        }
        printf("Case #%d: %.6f\n", q+1, dp[k]);
    }
    return 0;
}


