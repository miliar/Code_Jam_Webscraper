#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int i,j,k,n,m,a[11111];
int main()
{
    int T,p=0,l,h;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
         p++;
         
          scanf("%d%d%d",&n,&l,&h);
          for (i=1;i<=n;i++)
          scanf("%d",&a[i]);
          printf("Case #%d: ",p);
          for (i=l;i<=h;i++)
          {
              bool flag=false;
              for (j=1;j<=n;j++)
              if (i%a[j]&&a[j]%i)
              flag=true;
              if (!flag)
              {
                  printf("%d\n",i);break;
              }
          }
          if (i>h)
          { puts("NO");
          }
         }
         }
