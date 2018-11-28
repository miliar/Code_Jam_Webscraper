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
int c[1024];

void single_case(int case_number) {
    int n = gi();
    if (n==0) {
        printf("Case #%d: %d\n",case_number,0);
        return;
    }

    REP(i,n) c[i]=gi();
    c[n] = 99999;
    int best = 0;
    sort(c,c+n);
    
    do {
        int s = n+1,l=1;
        REP(i,n) {
            if (c[i+1]!=c[i]+1) {
                s = min(s,l);
                l = 1;
            } else l++;
        }
        best = max(best, s);
    } while (next_permutation(c,c+n));
    printf("Case #%d: %d\n",case_number,best);
    //printf("Case #%d:\n",case_number);
}

int main() {
    int j;
    scanf("%d",&j);
    REP(i,j) single_case(i+1);
    return 0;
}


