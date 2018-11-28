#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
    int i,j,k,n,m=0,cs;
    freopen("D-large.in","r",stdin);
    freopen("D.out","w",stdout);
    scanf("%d",&cs);
    while (cs--)
    {
          k=0;
          scanf("%d",&n);
          for (i=1;i<=n;i++)
          {
              scanf("%d",&j);
              if (j!=i)
              k++;
          }
          printf("Case #%d: %d\n",++m,k);
    }
}
    
