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

pair<int,int> a[1011];
int ok[1011];

int main() {
    freopen("B2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int n; cin >> n;
        FOR(i,1,n) {
            cin >> a[i].F >> a[i].S;
        }
        int star = 0, res = 0;
        memset(ok, 0, sizeof ok);
        FOR(turn,1,2*n) {
            bool done = false;
            FOR(i,1,n) if (ok[i] < 2 && a[i].S <= star) {
                star += 2 - ok[i];
                res++;
                ok[i] = 2;
                done = true;
                break;
            }
            if (done) continue;
            
            int maxb = -1;
            FOR(i,1,n) if (ok[i] < 1 && a[i].F <= star)
                maxb = max(maxb, a[i].S);
                
            FOR(i,1,n) if (ok[i] < 1 && a[i].F <= star && a[i].S == maxb) {
                star++;
                res++;
                ok[i] = 1;
                done = true;
                break;
            }
            if (!done) break;
        }
        printf("Case #%d: ", test);
        bool passed = true;
        FOR(i,1,n) if (ok[i] != 2) { passed = false; break; }
        if (!passed) puts("Too Bad");
        else printf("%d\n", res);
    }
    return 0;
}
