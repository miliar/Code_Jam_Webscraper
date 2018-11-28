#include<stdio.h>
#include<memory.h>
#define INF 0x3f3f3f
using namespace std;

int op[10000];
int ans[10000][2];
int now[10000];
int ch[10000];

int N,M,V;

int min(int a,int b)
{
    return a<b?a:b;
}

int mmin(int a,int b,int c)
{
    return min(a,min(b,c));
}

int get_min(int n,int v)
{
    int tt;
    int ss;
    if(n>=(M-1)/2)
    {
         if(now[n]==v)
         {
             ans[n][v]=0;
             return 0;
         }
         ans[n][v]=INF;
         return INF;
    }
    else
    {
         if(ans[n][v]!=-1)
             return ans[n][v];
         if(!ch[n])
         {
             if(v==1)
             {
                 if(op[n]==0)
                 {
                     ans[n][v]=get_min(2*n+1,1)+get_min(2*n+2,1);
                     return ans[n][v];
                 }
                 else
                 {
                     ans[n][v]=mmin(get_min(2*n+1,1)+get_min(2*n+2,0),get_min(2*n+1,1)+get_min(2*n+2,1),
                     get_min(2*n+1,0)+get_min(2*n+2,1));
                     return ans[n][v];
                 }
             }
             else
             {
                  if(op[n]==0)
                  {
                      ans[n][v]=mmin(get_min(2*n+1,0)+get_min(2*n+2,0),get_min(2*n+1,1)+get_min(2*n+2,0),
                      get_min(2*n+1,0)+get_min(2*n+2,1));
                      return ans[n][v];
                  }
                  else
                  {
                      ans[n][v]=get_min(2*n+1,0)+get_min(2*n+2,0);
                      return ans[n][v];
                  }
             }
         }
         else
         {
             if(v==1)
             {
                   if(op[n]==0)
                   {
                        ss=get_min(2*n+1,1)+get_min(2*n+2,1);
                        tt=mmin(get_min(2*n+1,1)+get_min(2*n+2,0),get_min(2*n+1,1)+get_min(2*n+2,1),
                        get_min(2*n+1,0)+get_min(2*n+2,1))+1;
                        ans[n][v]=min(ss,tt);
                        return ans[n][v];
                   }
                   else
                   {
                       ss=get_min(2*n+1,1)+get_min(2*n+2,1)+1;
                       tt=mmin(get_min(2*n+1,1)+get_min(2*n+2,0),get_min(2*n+1,1)+get_min(2*n+2,1),
                        get_min(2*n+1,0)+get_min(2*n+2,1));
                        ans[n][v]=min(ss,tt);
                        return ans[n][v];
                   }
             }
             else
             {
                 if(op[n]==0)
                 {
                     ss=mmin(get_min(2*n+1,0)+get_min(2*n+2,0),get_min(2*n+1,1)+get_min(2*n+2,0),
                      get_min(2*n+1,0)+get_min(2*n+2,1));
                     tt=get_min(2*n+1,0)+get_min(2*n+2,0)+1;
                     ans[n][v]=min(ss,tt);
                     return ans[n][v];
                 }
                 else
                 {
                     ss=mmin(get_min(2*n+1,0)+get_min(2*n+2,0),get_min(2*n+1,1)+get_min(2*n+2,0),
                      get_min(2*n+1,0)+get_min(2*n+2,1))+1;
                     tt=get_min(2*n+1,0)+get_min(2*n+2,0);
                     ans[n][v]=min(ss,tt);
                     return ans[n][v];
                 }
             }
         }
    }
}

void init()
{
     int i;
     int G,C;
     scanf("%d%d",&M,&V);
     for(i=0;i<(M-1)/2;i++)
     {
        scanf("%d%d",&G,&C);
        op[i]=!G;
        ch[i]=C;
     }
     for(i=(M-1)/2;i<M;i++)
        scanf("%d",&now[i]);
     memset(ans,-1,sizeof(ans));
}

int main()
{
    int i;
    //freopen("A.in","r",stdin);
    //freopen("A.txt","w",stdout);
    scanf("%d",&N);
    for(i=1;i<=N;i++)
    {
        init();
        get_min(0,V);
        if(ans[0][V]>=INF)
           printf("Case #%d: IMPOSSIBLE\n",i);
        else
            printf("Case #%d: %d\n",i,ans[0][V]);
    }
    //scanf("%d",&N);
    return 0;
}
                           
     
