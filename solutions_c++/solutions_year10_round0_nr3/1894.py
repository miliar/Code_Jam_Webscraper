#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(){
  int tn;
  scanf("%d",&tn);
  for (int ii=1;ii<=tn;ii++){
    long long r,k,n;
    scanf("%lld%lld%lld",&r,&k,&n);
    long long g[n], pre[n], skip[n];
    for (int i=0;i<n;i++){
      scanf("%lld",&g[i]);
    }
    for (int i=0;i<n;i++){
      pre[i] = g[i];
      skip[i]= 0;
      for (int j=1;j<n;j++){
        int tmp = (i+j)%n;
        if (pre[i]+g[tmp] <= k){
          pre[i] = pre[i]+g[tmp];
          skip[i] = j;
        }else{
          break;
        }
      }
    }
    long long p=0, ans=0;
    for (int i=0;i<r;i++){
      ans += pre[p];
      p = (p+skip[p]+1);
      if (p>=n)p=p%n;
    }
    printf("Case #%d: %lld\n", ii, ans);
  }
  return 0;
}
