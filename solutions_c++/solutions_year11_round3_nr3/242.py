#include<stdio.h>
using namespace std;
int T,n,p,l,h,ans;
int a[101];
inline bool check(int x)
{
  int i,j;
  for(i=1;i<=n;i++)
    if( !(x%a[i]==0 || a[i]%x==0))
      return false;
  return true;
}
int main()
{
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
  int i,j,k;
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%d%d%d",&n,&l,&h);
    ans=-1;
    for(i=1;i<=n;i++)
      scanf("%d",&a[i]);
    for(i=l;i<=h;i++)
      if(check(i)){
        ans=i;break;}
    printf("Case #%d: ",p);
    if(ans==-1)
      printf("NO\n");
    else
      printf("%d\n",ans);
  }
  scanf("%d",&n);
  return 0;
}
