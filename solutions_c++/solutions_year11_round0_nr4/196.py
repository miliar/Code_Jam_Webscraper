#include<stdio.h>
using namespace std;
int T,n,cas,a,ans,i;
int main()
{
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);
  scanf("%d",&T);
  for(cas=1;cas<=T;cas++){
    scanf("%d",&n);ans=n;
    for(i=1;i<=n;i++){
      scanf("%d",&a);
      if(a==i) ans--;}
    printf("Case #%d: %d.000000\n",cas,ans);
  }
  scanf("%d",&n);
  return 0;
}
