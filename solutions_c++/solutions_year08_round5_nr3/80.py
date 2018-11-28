#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
using namespace std;

inline long min(long a,long b){return a<b?a:b;}
inline long max(long a,long b){return a>b?a:b;}
inline long swap(long &a,long &b){long tt;tt=a,a=b,b=tt;}

const long N = 100,INF = 1<<28;
const double eps = 1e-8,pi=acos(-1);
long n,m;
char s[N][N];

void Init()
{
    long i,j,k;
    scanf("%ld%ld",&n,&m);
    for(i=0;i<n;i++)
        scanf("%s",s[i]);
}
long dy[]={1,1,1,-1,-1,-1};
long dx[]={1,0,-1,1,0,-1};
long mx[N][N],my[N][N];
long cov[N][N];
bool ok(long x,long y)
{
    return x>=0&&x<n&&y>=0&&y<m&&s[x][y]!='x';
}
bool dfs(long x,long y)
{
    long i,nx,ny;
    for(i=0;i<6;i++)
    {
        nx=x+dx[i];ny=y+dy[i];
        if(cov[nx][ny])continue;
        if(ok(nx,ny))
        {
            cov[nx][ny]=1;
            if(mx[nx][ny]==-1||dfs(mx[nx][ny],my[nx][ny]))
            {
                mx[nx][ny]=x;
                my[nx][ny]=y;
                return 1;
            }
        }
    }
    return 0;
}
void Solve()
{
    long i,j,k;
    long ans ,all;
    all=ans=0;
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            if(s[i][j]!='x')all++;
          //  printf("%ld al\n",all);
    memset(mx,-1,sizeof(mx));
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j+=2)
        {
            memset(cov,0,sizeof(cov));
            if(s[i][j]!='x'&&dfs(i,j))ans++;
        }
    }
    ans=all-ans;
    printf("%ld\n",ans);
}
int main()
{
    long T,K=1;
    freopen("i300.txt","r",stdin);
    freopen("o300.txt","w",stdout);
    scanf("%ld",&T);
    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    return 0;
}
