#include<stdio.h>
int main()
{
    int ans,test,ctr=1,i,j,p,s,n,t[101];
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&test);
    for(;ctr<=test;ctr++)
    {
                         scanf("%d%d%d",&n,&s,&p);
                         p--;
                         p*=3;
                         for(ans=i=0;i<n;i++)
                         {
                                         scanf("%d",&t[i]);
                                         if(p)
                                         {
                                             if(t[i]>p)ans++;
                                             else if(t[i]==p)
                                             {
                                                  if(s)
                                                  {
                                                       s--;ans++;
                                                  }
                                             }
                                             else if(t[i]+1==p)
                                             {
                                                  if(s)
                                                  {
                                                       s--;ans++;
                                                  }
                                             }
                                         }
                                         else
                                         {
                                             if(t[i])ans++;
                                         }
                         }
                         printf("Case #%d: %d\n",ctr,ans);
    }
    return 0;
}                
