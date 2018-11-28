#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,r,n,i,j,x[50];
char a[50][50];
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&t);
  for (tt=1; tt<=t; tt++) {
    scanf("%d\n",&n); r=0;
    for (i=1; i<=n; i++) {
      gets(a[i]+1); x[i]=0;
      for (j=1; j<=n; j++) if (a[i][j]=='1') x[i]=j;
    }
    for (i=1; i<=n; i++) {
      for (j=i; j<=n; j++) if (x[j]<=i) break;
      r+=j-i;
      while (j>i) { swap(x[j],x[j-1]); j--; }
    }
    printf("Case #%d: %d\n",tt,r);
  }
  return 0;
}
