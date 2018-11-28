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

const int N = 100000;
int n1,n2;          // INPUT
vector<int> g[N];   // INPUT
int m1[N], m2[N];   // OUTPUT
bool c[N*2];
int id[2*N];
int next[2*N];

bool dfs(int u) {
    if (u<0) return true;
    if (c[u]) return false; else c[u]=true;
    FOREACH(v, g[u]) 
        if (dfs(m2[*v])) { m1[u] = *v; m2[*v] = u; return true; }
    return false;
}

int matching() {
    REP(i,n1) m1[i]=-1;
    REP(i,n2) m2[i]=-1;
    bool changed;
    do {
        changed = 0;
        REP(i,n1) c[i]=false;
        REP(i,n1) if (m1[i]<0) changed |= dfs(i);
    } while(changed);
    int siz = 0;
    REP(i,n1) siz += (m1[i]!=-1);
    return siz;
}


void single_case(int case_number) {
    REP(i,N) g[i].clear();
    int R=gi();
    int C=gi();
    n1 = n2 = R*C;
    int n = n1;

    REP(i,R) {
        char buf[1000];
        int di, dj;
        scanf("%s",buf);
        REP(j,C) {
            if (buf[j]=='|') { di=1; dj=0; }
            if (buf[j]=='-') { di=0; dj=1; }
            if (buf[j]=='\\') { di=1; dj=1; }
            if (buf[j]=='/') { di=1; dj=-1; }
            int i1 = (i+di+R)%R;
            int j1 = (j+dj+C)%C;
            int i2 = (i-di+R)%R;
            int j2 = (j-dj+C)%C;
            g[i*C+j].push_back(i1*C+j1);
            g[i*C+j].push_back(i2*C+j2);
        }
    }

    if (matching()!=n) {
       printf("Case #%d: 0\n",case_number);
       return;
    }
    
    REP(i,n) {
        next[i+n] = m2[i];
        if (g[i][0]==m1[i])
            next[i] = n+g[i][1];
        else
            next[i] = n+g[i][0];
    }



    n*=2;
//    REP(i,n) printf("%d -> %d\n",i,next[i]);
//    printf("counting begins\n");
    int count = 0;
    REP(i,n) id[i] = -1;
    REP(i,n) { 
        if (id[i]!=(-1)) continue;
        id[i] = i;
        int it = next[i];
        while (id[it]==(-1)) {
            id[it] = i;
            it = next[it];
        }
        if (id[it]==i) count++;
    }
    int MOD = 1000003;
    int result = 1;
    REP(i,count) result = (result*2)%MOD;
    printf("Case #%d: %d\n",case_number,result);
}

int main() {
    int j;
    scanf("%d",&j);
    REP(i,j) single_case(i+1);
    return 0;
}


