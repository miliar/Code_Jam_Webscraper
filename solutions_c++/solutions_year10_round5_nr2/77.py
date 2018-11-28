
//Tomasz Kulczyński
#include <cstdio>
#include <iostream>
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

int nwd(int a,int b)
{
    return a?nwd(b%a,a):b;
}

#define M 101013 

int t[M];

void test()
{
    ll l;
    int n,b[113];
    scanf("%lld %d",&l,&n);
    REP(i,n) scanf("%d",&b[i]);
    int d = 0;
    REP(i,n) d = nwd(d, b[i]);
    if(l % d)
    {
        puts("IMPOSSIBLE");
        return ;
    }
    REP(i,n) b[i]/=d;
    l /= d;
    int inf = 1<<28;
    ll ret = l+1;
        REP(i,M) t[i] = inf;
        t[0] = 0;
        REP(i,n) REP(j,M-b[i]) t[j+b[i]] = min(t[j+b[i]], t[j] + 1);
        REP(i,n) REP(j,M) if((l-j)%b[i] == 0 && t[j]<inf) ret = min(ret, (l-j)/b[i] + t[j]);
     if(ret>l) 
     {
        puts("IMPOSSIBLE");
     }
     else printf("%lld\n",ret);
/*    REP(pocz,n)
    {
        int s = b[pocz];
        ll inf = l+l;
        REP(i,s) w[i] = inf;
        w[0] = 0;
        e[0] = 0;
        int ee = 1;
        while(ee)
        {
            int g = 0;
            int ff = 0;
            while(g < ee)
            {
                int x = e[g++];
                REP(i,n) 
                    if(x+b[i] > s && w[u = (x+b[i])%s] > w[x]) w[e[ee++] = u] = w[x];
                else if(x+b[i] < s && w[u = (x+b[i])%s] > w[x]) w[e[ee++] = u] = w[x];
            }
            REP(i,ff) e[i]=f[i];
            ee=ff;
        }
    }*/
}

int main()
{
    int dd,cas;
    scanf("%d",&dd);
    FOR(cas,1,dd)
    {
        printf("Case #%d: ",cas);
        test();
    }
    return 0;
}
