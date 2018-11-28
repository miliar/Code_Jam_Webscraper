#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = (1<<29);

LL f[10000000],a[200],m;
int n;

int main(){
  int ca; scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    scanf("%lld%d",&m,&n);
    for (int i=0; i<n; i++) scanf("%lld",&a[i]);
    sort(a,a+n);

    LL ans = (m-2000000)/a[n-1];
    if (m<2000000) ans=0;
    else m -= a[n-1]*ans;

    for (int i=0; i<=m; i++) f[i]=1ll<<60;
    f[0]=0;
    for (int i=0; i<n; i++){
      for (int j=a[i]; j<=m; j++){
        f[j] = min(f[j], f[j-a[i]]+1);
      }
    }
    if (f[m] >= 1ll<<60) printf("Case #%d: IMPOSSIBLE\n",tt);
    else printf("Case #%d: %lld\n",tt,f[m]+ans);
  }
  return 0;
}
