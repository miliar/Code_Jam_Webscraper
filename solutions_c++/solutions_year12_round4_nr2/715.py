#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#define MAX_N 10050
#define MAX_T 105
using namespace std;

long long r[MAX_N];
long long hehe_x[MAX_N];
int n,l,w;
long long hehe_y[MAX_N];

bool jud(long long x,long long y,int argu)
{
    int i;
    for(i=0;i<argu;++i)
        if((x-hehe_x[i])*(x-hehe_x[i])+(y-hehe_y[i])*(y-hehe_y[i])<(r[i]+r[argu])*(r[i]+r[argu]))
            return false;
    return true;
}

bool ahaha(long long x,long long y,int argu)
{
    return jud(x,y,argu);
}
bool dfs(int dfsargu)
{
    if(dfsargu==n)
    {
        int i = 0;
        while(i<n)
        {
            printf(" %lld %lld",hehe_x[i],hehe_y[i]);
            i++;
        }
        printf("\n");
        return true;
    }
    for(int i=0;i<MAX_T;++i)
    {
        long long x=(long long)rand()*rand()%(w+1);
        long long y=(long long)rand()*rand()%(l+1);
        if(ahaha(x,y,dfsargu))
        {
            hehe_x[dfsargu]=x,hehe_y[dfsargu]=y;
            if(dfs(dfsargu+1))
                return true;
        }
    }
    dfs(dfsargu-1);
}
void DoIt()
{
    int t;
    scanf("%d",&t);
    srand((unsigned)time(0));
    for(int cases =1 ; cases <= t; cases ++)
    {
        int i;
        scanf("%d%d%d",&n,&w,&l);
        for(i=0;i<n;++i)
            scanf("%lld",&r[i]);
        printf("Case #%d:",cases);
        dfs(0);
    }
}
int main()
{
//    freopen("B-small-attempt0.in","r",stdin);
//    freopen("B-small-attempt0.out","w",stdout);
    DoIt();
    return 0;
}
