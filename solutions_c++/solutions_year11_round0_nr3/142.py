#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
int a[1111];
int main()
{
    int i,j,k,n,m,p=0,q,cs;
    freopen("C-large.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&cs);
    while (cs--)
    {
          p++;
          scanf("%d",&n);
          m=0;
          for (i=0;i<n;i++)
          {
              scanf("%d",&a[i]);
              m^=a[i];
          }
          sort(a,a+n);
          printf("Case #%d: ",p);
          if (m)
          puts("NO");
          else
          {
              m=0;
              for (i=1;i<n;i++)
              m+=a[i];
              printf("%d\n",m);
          }
    }
}
