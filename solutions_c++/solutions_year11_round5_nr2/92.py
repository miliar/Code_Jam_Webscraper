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

int n, a[1011];
vector<pair<int,int> > cur;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test; cin >> test;
    FOR(t,1,test) {
        printf("Case #%d: ", t);
        scanf("%d", &n); FOR(i,1,n) scanf("%d", &a[i]);
        sort(a+1, a+n+1);
        
        cur.clear();
        FOR(i,1,n) {
            int nn = n + 1;
            REP(x,cur.size())
            if (a[i] == cur[x].F + 1) nn = min(nn, cur[x].S);
            
            if (nn == n+1) cur.PB(MP(a[i], 1));
            else {
                REP(x,cur.size())
                if (a[i] == cur[x].F+1 && nn == cur[x].S) {
                    cur[x].S++;
                    cur[x].F++;
                    break;
                }
            }
        }
        int res = n;
        REP(x,cur.size()) res = min(res, cur[x].S);
        printf("%d\n", res);
    }
    return 0;
}
