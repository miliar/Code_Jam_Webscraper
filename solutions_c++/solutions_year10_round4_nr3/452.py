#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <functional>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <cctype>
#include <ctime>
#include <cassert>
#include <deque>
using namespace std;

#define int64 long long
#define uint64 unsigned long long
#define two(X) (1<<(X))
#define twoL(X) ((int64)(1) << (X))
#define contain(S,X) (((S) & two(X)) != 0)
#define containL(S,X) (((S) & twoL(X)) != 0)
#define setBit(S,X) ((S) | two(X))
#define EPS 1E-6
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define REP(i,n) for (int i=0; i<n; ++i)
#define REPD(i,n) for (int i=n-1; i>=0; --i)
#define FOR(i,a,b) for (int i=a; i<=b; ++i)
#define FORD(i,a,b) for (int i=a; i>=b; --i)
#define FORALL(s,x) for (typeof(s.begin()) x=s.begin(); x!=s.end(); ++x) 
#define PRINT(s) {FORALL(s,v) cout << *v << " "; cout << endl;}
#define DEBUG(st) if (DEBUGON) {st}

#define DEBUGON 0

template<class T> inline void checkMin(T &a, T b) {if (b<a) a=b;}
template<class T> inline void checkMax(T &a, T b) {if (b>a) a=b;}
template<class T> inline T sqr (T x) {return x*x;}
template<class T> string toString(T value) {ostringstream sout; sout << value; return sout.str();}
template<class T> inline int countBit(T n) {return (n==0)?0:(1+countBit(n & (n-1)));}
int getBit(int n, int i) {return ((n>>i) & 1);}
int toInt(string s) {int r=0; istringstream sin(s); sin >> r; return r;}
const int di[] = {-1,0,1,0};
const int dj[] = {0,1,0,-1};
bool isEqual(double a, double b, double e=EPS) {return fabs(a-b)<e;}
bool isDiff(double a, double b, double e=EPS) {return fabs(a-b)>=e;}
bool isLess(double a, double b, double e=EPS) {return a<b-e;}
bool isMore(double a, double b, double e=EPS) {return a>b+e;}
bool isLessEq(double a, double b, double e=EPS) {return a<b+e; }
bool isMoreEq(double a, double b, double e=EPS) {return a>b-e;}


string toBinary(int n, int l=32) {string s; REP(i,l) s+=(char)(getBit(n,i)+'0'); return s;}
int randIn(int a, int b) {return rand()%(b-a+1) +  a;}

using namespace std;

int test, nTest, nRect;

#define MAX 120
#define INF 1000000000

bool a[MAX+2][MAX+2], b[MAX+2][MAX+2];

int ret;

bool transform() {    
    bool ok=false;
    memset(b,0,sizeof(b));
    FOR(i,1,MAX) FOR(j,1,MAX)  {
        if (a[i][j]) ok=true;
        b[i][j]=a[i][j];
        if (a[i][j] && !a[i][j-1] && !a[i-1][j]) {
            b[i][j]=false;
        }
        if (!a[i][j] && a[i][j-1] && a[i-1][j]) {
            b[i][j]=true;
        }
    }
    FOR(i,1,MAX) FOR(j,1,MAX) a[i][j]=b[i][j];
    return ok;
}

void solve() {
    ret = 0;
    while (transform()) {
        ++ ret;
/*        FOR(y,1,MAX) {
            FOR(x,1,MAX) {
                cout << a[x][y] << " ";
            }
            cout << endl;
        }
        cout << endl;*/
    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);    
    cin >> nTest;
    REP(test, nTest) {
        cin >> nRect;
        memset(a,0,sizeof(a));
        REP(i,nRect) {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;            
            FOR(i,x1,x2) FOR(j,y1,y2) a[i][j]=true;
        }
        solve();
        printf("Case #%d: %d\n", test+1, ret);
    }    
	return 0;
}
