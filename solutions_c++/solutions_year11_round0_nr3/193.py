#include<stdio.h>
#define maxn ~0U>>2
using namespace std;
int T,cas;
int a,n,minn,sum,x;
int main()
{
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
  int i,j,k;
  scanf("%d",&T);
  for(cas=1;cas<=T;cas++){
    minn=maxn,sum=0,x=0;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
      scanf("%d",&a);
      if(minn>a) minn=a;
      sum+=a,x^=a;}
    if(x!=0)
      printf("Case #%d: NO\n",cas);
    else
      printf("Case #%d: %d\n",cas,sum-minn);
  }
  scanf("%d",&n);
  return 0;
}
