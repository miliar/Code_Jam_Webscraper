//#pragma comment(linker, "/STACK:66777216")
#include <iomanip>
#include <sstream>
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

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i<_a; ++i)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define DEBUG(x) cout << #x << " = " << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(i,1,n) cout << a[i] << ' '; puts("");
using namespace std;

const double PI = acos(-1.0);

long double s[100111], p[100111];

int main() {
    freopen("A2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int A, B;
        cin >> A >> B;
        s[0] = 1.0;
        FOR(i,1,A) {
            cin >> p[i];
            s[i] = s[i-1] * p[i];
        }
//        PR(p, A);
//        PR(s, A);
        
        long double res = B + 2;
        FOR(x,0,A) {
            res = min(res, s[A-x]*(B-A+1+2*x) + (1-s[A-x])*(2*B-A+2+2*x));
        }
        printf("Case #%d: %.6lf\n", test, (double) res);
    }
    return 0;
}
