//Tomasz Kulczyński
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define COND 1
#define DB(x) { if(COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }


/* TK
 * Maksymalne skojarzenie w grafie dwudzielnym.
 * Złożoność: O(VE), ale w praktyce _bardzo_ szybkie. 
 */

#define MAXN 1010

int n1,n2;
VI v[MAXN]; //krawędzie LEWYCH wierzchołków!

bool c[2*MAXN];
int skoj[2*MAXN];

bool dfs(int x)
{
    c[x]=1;
    FORE(i,v[x])
        if(skoj[*i]==-1 || (!c[skoj[*i]] && dfs(skoj[*i])))
        {
            skoj[x]=*i; 
            skoj[*i]=x;
            return 1;
        }
    return 0;
}

int skojarzenie()
{
    int ret=0;
    REP(i,n1+n2) skoj[i]=-1;
    for(bool d=1;d;)
    {
        d=0;
        REP(i,n1) c[i]=0;
        REP(i,n1) if(skoj[i]==-1 && !c[i] && dfs(i)) d=1,ret++;
    }
    return ret;
}

int e[101][101];

int main()
{
    int dd;
    scanf("%d",&dd);    
    FOR(cas,1,dd)
    {
        REP(i,MAXN) v[i].clear();
        int n,k;
        scanf("%d %d",&n,&k);
        n1 = n2 = n;
        REP(i,n) REP(j,k) scanf("%d",&e[i][j]);
        REP(i,n) REP(j,n) 
        {
            int ok = 1;
            REP(u,k) if(e[i][u] >= e[j][u]) ok = 0;
            if(ok) 
            {
                v[i].push_back(j+n);
        //        printf("%d -> %d\n",i,j);
            }
        }
        printf("Case #%d: %d\n",cas,n - skojarzenie());
    }
    return 0;
}
