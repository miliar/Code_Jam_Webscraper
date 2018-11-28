#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long double LD;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(__typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
template<class T> inline void debug(const T&c) { cout << "{"; FOREACH(it,c) cout << *it << ","; cout << "}" << endl; }
template<class T> inline void setmin(T &a,const T& b){if(b<a) a=b;}
template<class T> inline void setmax(T &a,const T& b){if(b>a) a=b;}
template<class T> inline int size(const T&c) { return (int)c.size(); }
template<class T> inline string to_str(const T& a) { ostringstream os(""); os << a; return os.str(); }
template<class T> inline T sqr(const T&a) { return a*a; }
template<class T> T next() { T x; cin >> x; return x; }
int nint() { int x; scanf("%d",&x); return x; }
#define all(A) (A).begin(),(A).end()
#define FI first
#define SE second
#define MP make_pair
#define PB push_back

typedef pair<int,int> pi;
typedef pair<int, pi> pii;

bool porownaj(const pii& a, const pii& b) {
    return a.SE.FI < b.SE.FI;
}

void solve() {
    int X, S, R, N;
    double t;
    cin >> X >> S >> R >> t >> N;
    priority_queue<pii, vector<pii>, greater<pii> > Q;
    vector<pii> pary;
    while(N--) {
        int x, y, sp;
        cin >> x >> y >> sp;
        pary.PB(MP(sp, MP(x,y)));
    }
    sort(pary.begin(), pary.end(), porownaj);
    if(pary[0].SE.FI != 0)
        Q.push(  MP(0, MP(0, pary[0].SE.FI))  );
    if( pary.back().SE.SE != X )
        Q.push( MP(0, MP(pary.back().SE.SE, X)) );
    
    Q.push(pary[0]);
    for(int i=1; i<pary.size(); i++) {
        if(pary[i].SE.FI != pary[i-1].SE.SE)
	  Q.push(MP(0, MP(pary[i-1].SE.SE, pary[i].SE.FI)));
        Q.push(pary[i]);
    }
    
    double sol = 0;
    while(!Q.empty()) {
        pii tmp = Q.top();
        Q.pop();
        int len = tmp.SE.SE - tmp.SE.FI;
        
        int sp = tmp.FI;
        
        double aT = double(len) / double(sp + R);
        if(t >= aT) {
	  t -= aT;
	  sol += aT;
        }
        else {
	  double ilepoc = t * (sp + R);
	  
	  double ileres = len - ilepoc;
	  sol += t;
	  sol += ileres / double(sp + S);
	  t = 0;
        }
    }
    printf("%.8lf\n", sol);
}

int main() {
    int tests;
    cin >> tests;
    FOR(test,1,tests) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
















