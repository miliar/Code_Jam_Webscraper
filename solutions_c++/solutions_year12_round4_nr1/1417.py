#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
long long d[10005];
int Q[5000005];
long long R[5000005],L[10005];
int main()
{
   freopen("a.in","r",stdin);
   freopen("a.out","w",stdout);
   int T,n,D,k1,k2,far,v;
   long long r,t;
   scanf("%d",&T);
   for(int cas=1;cas<=T;cas++)
   {
        scanf("%d",&n);
          printf("Case #%d: ",cas);
        for(int i=1;i<=n;i++)
        {
           scanf("%lld%lld",&d[i],&L[i]);
        }
        scanf("%lld",&d[n+1]);L[n+1]=0;
        n++;
        if(d[1]>L[1]){puts("NO");continue;}
      
			  Q[k1=k2=far=1]=1;R[1]=d[1];
        bool flag=false;
        while(k1<=k2)
        {
            v=Q[k1];r=R[k1++];
            for(int i=v+1;i<=n&&r>=d[i]-d[v];i++)
            {
              
                 Q[++k2]=i;
                 R[k2]=min(L[i],d[i]-d[v]);
                 if(i==n){flag=true;break;}
               
            }
            if(flag)break;
        }
       
         if(flag)puts("YES");
         else puts("NO");




   }







   return 0;
}
