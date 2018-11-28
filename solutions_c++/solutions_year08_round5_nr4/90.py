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

const long N = 105,M=10007,INF = 1<<28;
const double eps = 1e-8,pi=acos(-1);
long n,m,l;
bool f[N][N];
long dx[]={1,2};
long dy[]={2,1};
long w[N][N];
void Init()
{
    long i,j,k;
    memset(f,0,sizeof(f));
    memset(w,-1,sizeof(w));
    scanf("%ld%ld%ld",&n,&m,&l);
    for(i=0;i<l;i++)
    {
        scanf("%ld%ld",&j,&k);
        f[j][k]=1;
    }
}
long dfs(long x,long y)
{
    if(x<1||y<1)return 0;
    if(f[x][y])return 0;
    if(x==1&&y==1)return 1;
    if(w[x][y]!=-1)return w[x][y];
    w[x][y]=0;
    w[x][y]+=dfs(x-2,y-1);
    w[x][y]+=dfs(x-1,y-2);
    w[x][y]%=M;
    return w[x][y];
}
void Solve()
{
    long i,j,k;
    long ans =dfs(n,m)%M;
    printf("%ld\n",ans);
}
int main()
{
    long T,K=1;
    freopen("i400.txt","r",stdin);
    freopen("o400.txt","w",stdout);
    scanf("%ld",&T);
    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    return 0;
}
