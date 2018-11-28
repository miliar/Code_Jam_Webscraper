#include <cstdio>
#include <algorithm>
using namespace std;
int i,j,k,n,t,tt,a[111],b[111];
char s[111];
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&t);
  for (tt=1; tt<=t; tt++) {
    scanf("%d",&n); a[0]=0;
    for (i=1; i<=n; i++) {
      scanf("%s",s+i); k=1;
      for (j=i-1; j>0; j--) if (s[j]==s[i]) { k=b[j]; break; }
      scanf("%d",&b[i]);
      a[i]=max(a[i-1],a[j]+abs(b[i]-k))+1;
    }
    printf("Case #%d: %d\n",tt,a[n]);
  }
  return 0;
}
