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

inline int GI() { int x; scanf("%d",&x); return x; }
inline LL GL() { LL x; scanf("%lld",&x); return x; }
inline char GC() { char x[2]; scanf("%s",x); return x[0]; }
inline void GS(char *x) { scanf("%s",x); }

const int N = 1<<20;

vector<LL> primes;
bool s[N];


void single_case(int case_number) {
    LL n;
    scanf("%lld",&n);

    if (n==1) {
        printf("Case #%d: 0\n",case_number);
        return;
    }

    int result = 1;

    for(int i=0;;i++) {
        LL q = primes[i]*primes[i];
        if (q>n) break;
        while(q<=n) {
            result++;
            q *= primes[i];
        }
    }
    printf("Case #%d: %d\n",case_number,result);
}

int main() {
    
    REP(i,N) s[i] = 1;
    FOR(i,2,N) if (s[i]) {
        primes.pb(i);
        for(int j=i;j<N;j+=i) s[j]=0;
    }

    int j;
    scanf("%d",&j);
    REP(i,j) single_case(i+1);
    return 0;
}


