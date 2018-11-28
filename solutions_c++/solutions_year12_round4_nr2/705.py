#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

#define MAXN 10110
#define MAXT 110

long long r[MAXN];
long long xxxx[MAXN],yyyy[MAXN];
int n,l,w;
bool dfs(int x);
long long randomx()
{
    return (long long)rand()*rand()%(w+1);
}
long long randomy()
{
    return (long long)rand()*rand()%(l+1);
}
inline long long sqr(long long x)
{
    return x*x;
}
bool check(long long x,long long y,int idx)
{
    for(int i=0;i<idx;++i)
        if(sqr(x-xxxx[i])+sqr(y-yyyy[i])<sqr(r[i]+r[idx])) return false;
    return true;
}
bool solve(int idx)
{
     for(int i=0;i<MAXT;++i)
    {
        long long x=randomx(),y=randomy();
        if(check(x,y,idx))
        {
            xxxx[idx]=x,yyyy[idx]=y;
            if(dfs(idx+1)) return true;
        }
    }
}
bool dfs(int idx)
{
    if(idx==n)
    {
        for(int i=0;i<n;++i)
            printf(" %lld %lld",xxxx[i],yyyy[i]);
        printf("\n");
        return true;
    }
  if( solve(idx))return true;
    dfs(idx-1);
}
void input()
{
     scanf("%d%d%d",&n,&w,&l);
        for(int i=0;i<n;++i)
            scanf("%lld",&r[i]);
}
int main()
{
    freopen("in33.txt","r",stdin);
    freopen("out.txt","w",stdout);
    srand((unsigned)time(0));
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        printf("Case #%d:",cas);
        input();
        dfs(0);
    }
    return 0;
}

