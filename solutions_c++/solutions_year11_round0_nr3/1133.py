#include<stdio.h>
#define maxn ~0U>>2
using namespace std;
int T,lc;
int a,n,minn,sum,x;
int main()
{
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);
  int i,j,k;
  scanf("%d",&T);
  for(lc=1;lc<=T;lc++){
    minn=maxn,sum=0,x=0;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
      scanf("%d",&a);
      if(minn>a) minn=a;
      sum+=a,x^=a;}
    if(x!=0)
      printf("Case #%d: NO\n",lc);
    else
      printf("Case #%d: %d\n",lc,sum-minn);
  }
  scanf("%d",&n);
  return 0;
}
