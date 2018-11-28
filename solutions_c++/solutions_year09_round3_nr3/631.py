#include<iostream>
#include<cstdio>
using namespace std;
int inf=1000000;
int res;
int t,n,m;
int ar[10];
char visit[10];
char take[110];
void f (int k,int d)
{
    if(k==n)
    {
       if(res>d)res=d;
    }
    else
    {
         
        for(int i=0;i<n;i++)
        {
          if(!visit[i])
          {
             visit[i]=1;
             int dd=0;
             for(int j=ar[i]-1;j>=1;j--)
             {
               if(take[j]==0)dd++;
               else break;
             }
             for(int j=ar[i]+1;j<=m;j++)
             {
               if(take[j]==0)dd++;
               else break;
             }
             take[ar[i]]=1;
             f(k+1,d+dd);
             visit[i]=0;
             take[ar[i]]=0;
          }
        }
    }
}
         
main()
{
      freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w+",stdout);
      scanf("%d",&t);
      for(int k=1;k<=t;k++)
      {
         scanf("%d%d",&m,&n);
         for(int i=0;i<n;i++)
           scanf("%d",&ar[i]);
         memset(visit,0,sizeof(visit));
         memset(take,0,sizeof(take));
         res=inf;
         f(0,0);
         printf("Case #%d: %d\n",k,res);
      }
      return 0;
}
