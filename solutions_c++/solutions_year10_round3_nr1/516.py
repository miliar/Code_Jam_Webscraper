#include <stdio.h>
int main()
{
    int t,n,i,j;
    int x[1100],y[1100];
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.txt","w",stdout);
    scanf("%d",&t);
    for (i=1;i<=t;i++)
    {
          scanf("%d",&n);
          for (j=0;j<n;j++)
             scanf("%d%d",&x[j],&y[j]);
          printf("Case #%d: ",i);
          if (n==1)
             printf("0\n");
          else
          {
              if (x[0]>x[1])
              {
                  if (y[0]<y[1])
                     printf("1\n");
                  else
                     printf("0\n");
              }
              else
              {
                  if (y[0]<y[1])
                     printf("0\n");
                  else
                     printf("1\n");
              }
          }
    }
    return 0;
}
