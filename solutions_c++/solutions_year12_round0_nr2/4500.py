#include<iostream>
#include<stdio.h>
using namespace std;

int ans=0;

void dfs(int x,int s0,int N,int P, int S,int t[],int MaxSum)
{
    if(s0>S)
    {
       // printf("s0==S  x=%d\n",x);
        return;
    }
    if(x==N)
    {
        if(s0==S && MaxSum>ans)
        {
         //   printf("s0=%d ans=%d\n",s0,MaxSum);
            ans=MaxSum;
        }
        return;
    }
    int num=t[x]/3;
    //printf("t[%d]/3 = %d\n",x,num);
    if(t[x]==0)
    {
        if(0>=P)
        {
            dfs(x+1,s0,N,P,S,t,MaxSum+1);
        }
        else
        {
            dfs(x+1,s0,N,P,S,t,MaxSum);
        }
    }
    else
    {

    if(t[x]%3==0)
    {

        if(num>=P)
        {
            dfs(x+1,s0,N,P,S,t,MaxSum+1);
        }
        else
        {
            dfs(x+1,s0,N,P,S,t,MaxSum);
        }

        if(num+1>=P||num>=P||num-1>=P)
        {
            dfs(x+1,s0+1,N,P,S,t,MaxSum+1);
        }
        else
        {
            dfs(x+1,s0+1,N,P,S,t,MaxSum);
        }
    }

    else if(t[x]%3==1)
    {
        if(num+1>=P||num>=P)
        {
            dfs(x+1,s0,N,P,S,t,MaxSum+1);
        }
        else
        {
            dfs(x+1,s0,N,P,S,t,MaxSum);
        }

        if(num+1>=P||num-1>=P)
        {
            dfs(x+1,s0+1,N,P,S,t,MaxSum+1);
        }
        else
        {
            dfs(x+1,s0+1,N,P,S,t,MaxSum);
        }
    }

    else if(t[x]%3==2)
    {
        if(num+1>=P||num>=P)
        {

            dfs(x+1,s0,N,P,S,t,MaxSum+1);
        }
        else
        {
            dfs(x+1,s0,N,P,S,t,MaxSum);
        }

        if(num+2>=P||num>=P)
        {
            dfs(x+1,s0+1,N,P,S,t,MaxSum+1);
        }
        else
        {
            dfs(x+1,s0+1,N,P,S,t,MaxSum);
        }
    }
    }
}

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T=0;
    scanf("%d",&T);
    int t[105];
    int k=1;
    while(T--)
    {
        int N=0;
        int P=0;
        int S=0;
        scanf("%d%d%d",&N,&S,&P);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&t[i]);
        }
        ans=0;
        dfs(0,0,N,P,S,t,0);
        printf("Case #%d: %d\n",k++,ans);
    }
    return 0;
}
