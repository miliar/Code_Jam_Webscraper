/*
TASK: Equal Sums
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
using namespace std;
#define X first
#define Y second
int N,M,T;
bool ok;
int a[509];
int b[509];
void dfs2(int x,int sum,int s)
{
//    printf("%d %d %d\n",x,sum,s);
    if(x>N)    return;
    if(s>sum)   return;
    if(s==sum && s>0)
    {
//        printf("%d %d\n",s,x);
        ok=true;
        return;
    }
    if(b[x]!=1)
    {
        b[x]=2;
        dfs2(x+1,sum,s+a[x]);
        if(ok)  return;
        b[x]=0;
        dfs2(x+1,sum,s);
    }
    else
        dfs2(x+1,sum,s);
}
void dfs(int x,int sum)
{
    if(x>N)    return;
    if(ok)  return;
    b[x]=1;
    dfs2(1,sum+a[x],0);
    dfs(x+1,sum+a[x]);
    if(ok)  return;
    b[x]=0;
    dfs2(1,sum,0);
    dfs(x+1,sum);
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int ii=0;
    while(T--)
    {
        ii++;
        printf("Case #%d:\n",ii);
        scanf("%d",&N);
        for(i=1;i<=N;i++)
            scanf("%d",&a[i]);
        ok=false;
        dfs(1,0);
        if(!ok)
            printf("Impossible\n");
        else
        {
            for(i=1;i<=20;i++)
                if(b[i]==1)
                    printf("%d ",a[i]);
            printf("\n");
            for(i=1;i<=20;i++)
                if(b[i]==2)
                    printf("%d ",a[i]);
            printf("\n");
        }
        memset(b,0,sizeof b);
    }
}
