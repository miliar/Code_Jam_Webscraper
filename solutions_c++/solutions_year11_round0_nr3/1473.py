#include<iostream>
#include<algorithm>
#define inf 1000000010
using namespace std;
int a[1010];
int main()
{
     freopen("C-large.in","r",stdin);
     freopen("C-large.out","w",stdout);

     int t,n;
     int i,j,k;

     scanf("%d",&t);
     for(i=1;i<=t;i++)
     {
          scanf("%d",&n);
          int minn=inf;
          int summ=0;
          int sum[30]={0};

          for(j=0;j<n;j++)
          {
               scanf("%d",&a[j]);
               minn=min(minn,a[j]);
               summ+=a[j];
               }

          for(j=0;j<=20;j++)
          {
               for(k=0;k<n;k++)
               sum[j]^=((a[k]&(1<<j))/(1<<j));
               }

          /*for(j=0;j<=20;j++)
          printf("%d ",sum[j]);
          printf("\n");*/

          int can=1;
          for(j=0;j<=20;j++)
          {
               if(sum[j]%2)
               can=0;
               }

          if(can)
          printf("Case #%d: %d\n",i,summ-minn);
          else
          printf("Case #%d: NO\n",i);
          }
     }
