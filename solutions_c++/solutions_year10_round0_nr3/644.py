
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
int cond = 1;
#define db(x) {if(cond){cerr << __LINE__ << " " << #x << " " << x << endl; } }
#define dbv(x) {if(cond){cerr << __LINE__ << " " << #x << ": "; FORE(__i,x) cerr << *__i << " "; cerr << endl;} }

#define M 2013 

ll G;
int g[M], kr[M];
ll s[M];

void szuk(int &a, int n, int k, ll &ret, int &u)
{
    if(k >= G)
    {
        ret += G;
        u++;
        return ;
    }
    while(g[a] <= k)
    {
        k -= g[a];
        ret += g[a];
        a++;
    }
    a %= n;
    u++;
}

int main()
{
    int dd, cas = 0;
    scanf("%d",&dd);
    while(dd--)
    {
        int r,k,n;
        scanf("%d %d %d",&r,&k,&n);
        G = 0;
        REP(i,n) scanf("%d",&g[i]);
        REP(i,n) G += g[n+i] = g[i], kr[i] = -1;
        kr[0] = 0;
        s[0] = 0;
        int u = 0, ok = 0, a = 0;
        ll ret = 0;
        while(u < r)
        {
            szuk(a, n, k, ret, u);
            if(!ok)
            {
                if(kr[a] != -1)
                {
                    int ile = (r-u) / (u - kr[a]);
                    u += ile * (u - kr[a]);
                    ret += ile * (ret - s[a]);
                    ok = 1;
                }
                else
                {
                    kr[a] = u;
                    s[a] = ret;
                }
            }
        }
        printf("Case #%d: %lld\n",++cas,ret);
    }
    return 0;
}
