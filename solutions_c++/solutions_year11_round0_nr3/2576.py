#include <cstdio>
#include <algorithm>
using namespace std;
int t,n,c[1000],xor_sum,ans;
int main()
{
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&t);
 for (int i=1;i<=t;++i)
 {
  printf("Case #%d: ",i);
  scanf("%d",&n);
  scanf("%d",&xor_sum);
  c[0]=xor_sum;
  for (int j=1;j<n;++j)
  {
   scanf("%d",&c[j]);
   xor_sum^=c[j];
  }
  if (xor_sum!=0) { printf("NO\n"); continue; }
  sort(c,c+n);
  ans=0;
  for (int j=1;j<n;++j) ans+=c[j];
  printf("%d\n",ans);
 }
}