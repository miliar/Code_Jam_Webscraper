#include<iostream>
using namespace std;
int x1,y1,x2,y2;
int i,j,k,l,flag,m,n,s,cn,ci;

int main()
{
  freopen("b.in","r",stdin);
  freopen("b_small.out","w",stdout);
  scanf("%d",&cn);
  ci=0;
  while (cn--)
  {
    ci++;
    scanf("%d %d %d",&n,&m,&s);
    flag=1;
    for (i=0;i<=n && flag;i++)
      for (j=0;j<=m && flag;j++)
        for (k=0;k<=n && flag;k++)
          for (l=0;l<=m;l++)
            if (abs(i*l-j*k)==s)
            {
              flag=0;
              x1=i;
              y1=j;
              x2=k;
              y2=l;
              break;
            }
    printf("Case #%d: ",ci);
    if (flag) printf("IMPOSSIBLE\n");
    else printf("0 0 %d %d %d %d\n",x1,y1,x2,y2);
  }
  return 0;
}