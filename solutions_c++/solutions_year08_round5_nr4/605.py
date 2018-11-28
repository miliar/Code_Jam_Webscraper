#include<iostream>
using namespace std;
int f[200][200],a[200][200];
int i,j,k,h,w,r,cn,ci;

int main()
{
  freopen("d_small.out","w",stdout);
  scanf("%d",&cn);
  ci=0;
  while (cn--)
  {
    ci++;
    scanf("%d %d %d",&h,&w,&r);
    memset(f,0,sizeof(f));
    for (i=0;i<r;i++)
    {
      scanf("%d %d",&j,&k);
      f[j][k]=1;
    }
    printf("Case #%d: ",ci);
    memset(a,0,sizeof(a));
    a[1][1]=1;
    for (i=1;i<=h;i++)
      for (j=1;j<=w;j++) if (!f[i][j])
      {
        a[i+1][j+2]+=a[i][j];
        a[i+1][j+2]%=10007;
        a[i+2][j+1]+=a[i][j];
        a[i+2][j+1]%=10007;
      }
    printf("%d\n",a[h][w]);
  }
  return 0;
}