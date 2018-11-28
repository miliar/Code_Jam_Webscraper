#include<algorithm>
#include<cstdio>
using namespace std;
long long a[1111];
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int n;
    scanf("%d",&n);
    int i;
    for(i=0;i<n;++i)scanf("%I64d",a+i);
    int j;
    long long gcdd=max(*a-a[1],a[1]-*a);
    for(i=0;i<n;++i)
      for(j=0;j<i;++j)
        gcdd=__gcd(gcdd,max(a[i]-a[j],a[j]-a[i]));
    printf("Case #%d: %I64d\n",testi,(gcdd-*a%gcdd)%gcdd);
  }
  return 0;
}