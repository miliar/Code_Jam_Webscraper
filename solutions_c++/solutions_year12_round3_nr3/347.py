/*
TASK: Box Factory
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
long long a[127],b[127];
int ty1[127],ty2[127];
long long Mc;
int u[127];
void chk(int id,long long re,int idx,long long bb,long long s)
{
//    printf("%d %d\n",id,idx);
    if(id>N || idx>M)
    {
//        printf("--\n");
        Mc=max(Mc,s);
        return;
    }
    if(u[id]==0)    chk(id+1,a[id+1],idx,bb,s);
    else
    {
        if(ty1[id]==ty2[idx])
        {
            long long xx=min(re,bb);
            if(re-xx>0)
                chk(id,re-xx,idx+1,b[idx+1],s+xx);
            else
                chk(id+1,a[id+1],idx,bb-xx,s+xx);
        }
        else
        {
            chk(id+1,a[id+1],idx,bb,s);
            chk(id,re,idx+1,b[idx+1],s);
        }
    }
}
void dfs(int x)
{
    if(x>N)
    {
        int i;
        for(i=1;i<=N;i++)
            if(u[i]!=0)
                break;
//        printf("%d%d%d\n",u[1],u[2],u[3]);
//        printf("(%d)\n",i);
        chk(i,a[i],1,b[1],0);
        return;
    }
    u[x]=0;
    dfs(x+1);
    u[x]=1;
    dfs(x+1);
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
        scanf("%d%d",&N,&M);
        for(i=1;i<=N;i++)
            scanf("%I64d%d",&a[i],&ty1[i]);
        for(i=1;i<=M;i++)
            scanf("%I64d%d",&b[i],&ty2[i]);
        Mc=0;
        dfs(1);
        printf("Case #%d: %I64d\n",ii,Mc);
    }
}
