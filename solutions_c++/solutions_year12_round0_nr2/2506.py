#include <cstdio>
#include <algorithm>
#include <memory.h>
using namespace std;
int n,m,k,tt,T,i,j,a[111],f[111][111];
bool good;
int main() {
  freopen("Bl.in","r",stdin);
  freopen("Bl.out","w",stdout);
  scanf("%d",&tt);
  for (T=1; T<=tt; T++) {
    scanf("%d%d%d",&n,&m,&k);
    for (i=0; i<n; i++) scanf("%d",&a[i]);
    memset(f,255,sizeof(f));
    f[0][0]=0;
    for (i=0; i<n; i++) for (j=m; j>=0; j--) if (f[i][j]>=0) {
      f[i+1][j]=f[i][j]+int(3*k<=a[i] || (k>0 && 3*k-2<=a[i]));
      if (j<m && 28>=a[i] && a[i]>=2) {
        good=(k>1 && 3*k-4<=a[i]) || (k>0 && k<10 && 3*k-1<=a[i]) || (k<9 && 3*k+2<=a[i]);
        f[i+1][j+1]=max(f[i+1][j+1],f[i][j]+int(good));
      }
    }
    printf("Case #%d: %d\n",T,max(0,f[n][m]));
  }
  return 0;
}
