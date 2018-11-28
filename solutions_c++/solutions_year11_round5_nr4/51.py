#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <utility>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<long> VL;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)

#define pb push_back
#define mp make_pair
#define st first
#define nd second

LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }
int bc(LL x) { return x?bc(x>>1)+(x&1):0; }

inline int rnd(int n) { return rand()%n; }

inline double gd() { double x; scanf("%lf",&x); return x; }
inline int gi() { int x; scanf("%d",&x); return x; }
inline LL gl() { LL x; scanf("%lld",&x); return x; }
inline LD gld() { LD x; scanf("%llf",&x); return x; }
inline char gc() { char x[2]; scanf("%s",x); return x[0]; }
inline void gs(char *x) { scanf("%s",x); }

char s[200];
int n,m;

void single_case(int case_number) {
    scanf("%s",s);
    n = strlen(s);
    m = 0;
    REP(i,n) if (s[i]=='?') m++;
    REP(kk, (1<<m)) {
        int k = kk;
        long long x = 0;
        REP(i,n) {
            if (s[i]=='?') {
                x = x*2 + (k&1);
                k /= 2;
            } else {
                x = x*2 + (s[i]-'0');
            }
        }
        long long y = sqrtl(x);
        if (y*y==x) {
            FORD(i,n,0) {
                s[i] = '0'+x%2;
                x/=2;
            }
            printf("Case #%d: %s\n",case_number,s);
            return;
        }
    }
}

int main() {
    int j;
    scanf("%d",&j);
    REP(i,j) single_case(i+1);
    return 0;
}


