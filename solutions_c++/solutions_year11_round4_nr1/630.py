#include<iostream>
#include<algorithm>
using namespace std;
int a[1000010];
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);

     int T,x,s,r,m,n,b,e,w;
     int t,i,j;

     scanf("%d",&T);
     for(t=1;t<=T;t++)
     {
          scanf("%d%d%d%d%d",&x,&s,&r,&m,&n);
          int ind=0;
          for(i=0;i<n;i++)
          {
               scanf("%d%d%d",&b,&e,&w);
               for(j=0;j<e-b;j++)
               a[ind++]=w;
               }
          for(i=ind;i<x;i++)
          a[i]=0;
          sort(a,a+x);

          /*for(i=0;i<x;i++)
          printf("%d ",a[i]);
          printf("\n");*/

          double used=0,left=0;
          int mark=x;
          int check=0;
          for(i=0;i<x;i++)
          {
               if(used+(double)1/(double)(a[i]+r)<=m)
               {
                    a[i]+=r;
                    used+=(double)1/(double)a[i];
                    }
               else
               {
                    mark=i;
                    left=1-(m-used)*(a[i]+r);
                    used=m;

                    check=1;
                    break;
                    }
               }

          double ans=0;
          if(check)
          ans=left/(double)(a[mark]+s);

          for(i=mark+1;i<x;i++)
          ans+=(double)1/(double)(a[i]+s);

          printf("Case #%d: %.9lf\n",t,ans+used);
          }

     return 0;
     }
