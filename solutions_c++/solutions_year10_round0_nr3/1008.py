#include<stdio.h>
#include<string.h>
int t,n;
long long r,k,g[1000];
int ne[1000];
long long num[1000];
int mark1[1000];
long long mark2[1000];
int main()
{
    int i, j;
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    int ca=0;
    while(t--)
    {
             
              scanf("%I64d%I64d%d",&r,&k,&n);
              long long sum=0;
              for(i=0;i<n;i++)
              {
                              scanf("%I64d",&g[i]);
                              sum+=g[i];
              }
               printf("Case #%d: ",++ca);
              if(sum<=k)
              printf("%I64d\n",r*sum);
              else
              {
                  for(i=0;i<n;i++)
                  {
                                  long long sum=0;
                                  for(j=i;;j=(j+1)%n)
                                  {
                                                     sum+=g[j];
                                                     if(sum>k)
                                                     {
                                                              ne[i]=j;
                                                              num[i]=sum-g[j];
                                                             // printf("%lld %lld\n",ne[i],num[i]);
                                                              break;
                                                     }
                                  }
                  }
                  int h=0,hi;
                  long long  sum=0;
                  long long  len,wei;
                  memset(mark1,0,sizeof(mark1));
                  memset(mark2,0,sizeof(mark2));
                  for(i=1;i<=r;i++)
                  {
                                   sum+=num[h];
                                  if(mark1[h]!=0)
                                  {
                                                 len=i-mark1[h];
                                                 wei=sum-mark2[h];
                                                 hi=h;
                                                 break;
                                  }
                                  else
                                  {
                                      mark1[h]=i;
                                      mark2[h]=sum;
                                      h=ne[h];
                                  }
                  }
                  if(i==r+1) printf("%I64d\n",sum);
                  else
                  {
                      long long ans=sum;
                      r-=i;
                      ans+=(r/len)*wei;
                      h=ne[hi];
                      for(j=1;j<=r%len;j++)
                      {
                                           ans+=num[h];
                                           h=ne[h];
                      }
                      printf("%I64d\n",ans);
                  }
              }
    }
    return 0;
}
                  
                                                 
                                  
                                                              
                                                     
              
                              
              
