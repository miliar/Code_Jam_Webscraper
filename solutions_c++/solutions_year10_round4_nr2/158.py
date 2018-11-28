#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,n,i,j,nn,a[5000],b[5000][2],c[5000],f[5500][12];
int solve(int i, int j) {
  if (f[i][j]>=0) return f[i][j];
  f[i][j]=c[i];
  if (b[i][0]>nn) f[i][j]+=solve(b[i][0],j);
  if (b[i][1]>nn) f[i][j]+=solve(b[i][1],j);
  if (j<a[i]) {
    int r=0;
    if (b[i][0]>nn) r+=solve(b[i][0],j+1);
    if (b[i][1]>nn) r+=solve(b[i][1],j+1);
    f[i][j]=min(f[i][j],r);
  }
  return f[i][j];
}
int main() {
   freopen("Bl.in","r",stdin);
   freopen("Bl.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d",&n); n=(1<<n); nn=n-1;
     for (i=0; i<n; i++) { scanf("%d",&a[i]); b[i][0]=b[i][1]=-1; }
     for (i=0; i+1<n; i+=2) {
       scanf("%d",&c[n]);
       b[n][0]=i; b[n][1]=i+1;
       for (j=0; j<12; j++) f[n][j]=-1;
       a[n++]=min(a[i],a[i+1]);
     }
     printf("Case #%d: %d\n",tt,solve(n-1,0));
   }
   return 0;
}
