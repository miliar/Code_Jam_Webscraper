#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
struct data
{
   int d,l,most,flag;
}a[123456];
int mm(int aa,int bb)
{
    if (aa>bb)
    return aa;
    return bb;
}
int main()
{
    int cs,j,k,n,m;
    int q=0;
    freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout);
    scanf("%d",&cs);
    while (cs--)
    {
          scanf("%d",&n);
          memset(a,-1,sizeof(a));
          for (int i=0;i<n;i++)
          {
              scanf("%d%d",&a[i].d,&a[i].l);
          }scanf("%d",&m);
          int h=1;
          a[0].flag=1;
          a[0].most=a[0].d;
          for (int i=0;i<n;i++)
          { 
              if (a[i].flag==1)
              {
                  while (h<n&&a[i].d+a[i].most>=a[h].d)
                  {
                       a[h].flag=1;
                       a[h].most=a[h].d-mm(a[i].d,a[h].d-a[h].l);
                       h++;
                  }
              }
          }
          bool yy=false;
          for (int i=0;i<n;i++)
          {
              if (a[i].flag==1&&a[i].most+a[i].d>=m)
              yy=true;
          }
          printf("Case #%d: ",++q);
          
          if (yy)puts("YES");else puts("NO");
    }
}
          
