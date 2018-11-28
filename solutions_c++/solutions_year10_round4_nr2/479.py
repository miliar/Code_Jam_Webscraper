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

#define MAX 12

#define INF 1000000000000000LL

int nRound;
int nTeam;
int nTest;
int miss[1<<MAX];
int price[MAX][1<<MAX];

int ret;

int64 f[MAX][1<<MAX][MAX];

int64 calcF(int round, int team, int match) {
    int64 ret=0;
    if (f[round][team][match]!=-1) {
        ret=f[round][team][match];
    }  else {
        int l = team;
        int r = team + (1<<round) - 1;
        FOR(i,l,r) if (miss[i] < nRound - (match+round)) {
            ret= INF;
            break;
        }       
        if (ret!=INF) {
            if (round==0) ret=0;
            else {
                int64 minl = calcF(round-1, team, match+1);
                int64 minr = calcF(round-1, team+(1<<(round-1)), match+1);
                if (minl!=INF && minr!=INF) ret = price[round][team] + minl + minr;
                minl = calcF(round-1, team, match);
                minr = calcF(round-1, team+(1<<(round-1)), match);
                ret = min(ret, minl+minr);
            }
        }
    }
    f[round][team][match]=ret;
    //cout << round << " " << team << " " << match << " " << ret << endl;
    return ret;
}

void solve() {
   memset(f,-1,sizeof(f));
   ret = calcF(nRound,0,0);
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> nTest;
    REP(test, nTest) {
        cin >> nRound;        
        nTeam = 1<<nRound;
        REP(i,nTeam) {
            cin >> miss[i];   
        }
        FOR(i,1,nRound) {
            for (int j=0; j<nTeam; j+=(1<<i)) {
                cin >> price[i][j];
            }
        }
        
        solve();
        
        printf("Case #%d: %d\n", test+1, ret);
    }    
	return 0;
}
