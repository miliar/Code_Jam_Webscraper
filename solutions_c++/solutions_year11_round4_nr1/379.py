#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>
#include <sstream>
#include <iomanip>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
using namespace std;

const double PI = acos(-1.0);

int n, S, R, T, X;
pair<int,int> a[10111];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        printf("Case #%d: ", test);
        scanf("%d %d %d %d %d", &X, &S, &R, &T, &n);
        long double t = T;
        FOR(i,1,n) {
            int u, v;
            scanf("%d %d %d", &u, &v, &a[i].F);
            a[i].S = v - u;
            X -= v - u;
        }
        if (X) a[++n] = MP(0, X);
        
        long double res = 0.0;
        sort(a+1, a+n+1);
        
        FOR(i,1,n) {
            // If run all
            if (t * (R + a[i].F) >= a[i].S) {
                long double now = a[i].S / (long double) (R + a[i].F);
                res += now;
                t -= now;
            }
            
            // Run all we can
            else {
                long double req = a[i].S;
                req -= t * (R + a[i].F);
                res += t;
                t = 0;
                res += req / (long double) (S + a[i].F);
            }
        }
        
        cout << (fixed) << setprecision(7) << res << endl;
    }
    return 0;
}
