#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t;
int n,k,ss;
int u[100];

struct node{
       int a[25];}s[100];
int cmp(node a,node b)
{
    int i;
   
    return a.a[ss]>b.a[ss];
}  

int cc(node a,node b)
{
    int i;
    for(i=0;i<k;i++)
    if(a.a[i]<=b.a[i])
    return 0;
    return 1;
}  
int main()
{
    int i,j,kk,tt;
    int ans,ans1;
   freopen("C-small-attempt3.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    for(tt=1;tt<=t;tt++)
    {
                        scanf("%d%d",&n,&k);
                        for(i=0;i<n;i++)
                          for(j=0;j<k;j++)
                          scanf("%d",&s[i].a[j]);
                          ans=100000;
                          for(ss=0;ss<k;ss++)
                          {
                                             sort(s,s+n,cmp);
                          ans1=0;
                          int sum=0;
                          int o;
                          memset(u,0,sizeof(u));
                          node aa;
                          while(sum<n)
                          {
                                      o=0;
                                      for(i=0;i<n;i++)
                                      if(u[i]==0)
                                      {
                                                 if(!o||cc(aa,s[i]))
                                                 {
                                                                    u[i]=1;
                                                     aa=s[i];
                                                     sum++;
                                                     o=1;
                                                 }
                                                           
                                      }
                                      ans1++;
                          }
                          if(ans1<ans)
                          ans=ans1;
                          }
                          printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
                          
                          
                        
