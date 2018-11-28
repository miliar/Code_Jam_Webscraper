#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
using namespace std;

const double eps = 1e-10;

inline double min(double a,double b){return a<b?a:b;}
inline double max(double a,double b){return a>b?a:b;}
const long N =405,M=1005;
const long INF= 1<<28;
long n,m,T,w[N][N],match[N],cov[N];
struct point {long st,et;}p[N];
long K = 1;
inline void swap(double &a,double &b){double tt;tt=a,a=b,b=tt;}

void Init()
{
    scanf("%ld%ld%ld",&T,&n,&m);
    long i,j,a1,a2,b1,b2;
    for(i=1;i<=n+m;i++)
    {
        scanf("%ld:%ld %ld:%ld",&a1,&a2,&b1,&b2);
        p[i].st=a1*60+a2;
        p[i].et=b1*60+b2;
    }
    memset(match,-1,sizeof(match));
    for(i=1;i<=n+m;i++)
    {
        for(j=1;j<=n+m;j++)
            if(i!=j&&(i<=n&&j>n||i>n&&j<=n)&&p[i].et+T<=p[j].st)
                w[i][j]=1;
            else w[i][j]=0;
    }
}
bool dfs(long v)
{
    long i,st,ed;
    if(v<=n){st=n+1,ed=n+m;}
    else {st=1,ed=n;}
    for(i=st;i<=ed;i++)
    {
        if(cov[i])continue;
        if(w[v][i])
        {
            cov[i]=1;
            if(match[i]==-1||dfs(match[i]))
            {
                match[i]=v;return 1;
            }
        }
    }
    return 0;
}
void Solve()
{
    long i,j,k;
    long a1,a2;
    a1=a2=0;
    for(i=1;i<=n+m;i++)
    {
        for(j=1;j<=n+m;j++)cov[j]=0;
        dfs(i);
    }
    for(i=1;i<=n;i++)if(match[i]==-1)a1++;
    for(i=n+1;i<=n+m;i++)if(match[i]==-1)a2++;
    printf("Case #%ld: ",K++);
    printf("%ld %ld\n",a1,a2);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T;scanf("%ld",&T);

    while(T--)
    {
        Init();
        Solve();
    }
    return 0;
}
