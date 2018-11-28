#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,n,i,j,k,r,c[505][505],md=100003;
long long f[505][505];
int main() {
   freopen("Cl.in","r",stdin);
   freopen("Cl.out","w",stdout);
   for (i=0; i<505; i++) {
     c[i][0]=1;
     for (j=1; j<=i; j++) c[i][j]=(c[i-1][j]+c[i-1][j-1])%md;
   }
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d",&n); r=0;
     for (i=2; i<=n; i++) {
       f[i][1]=1;
       for (j=2; j<i; j++) {
         f[i][j]=0;
         for (k=1; k<j; k++) if (j-k<=i-j) f[i][j]=(f[i][j]+f[j][k]*c[i-j-1][j-k-1])%md;
       }
     }
     for (i=1; i<n; i++) r=(r+f[n][i])%md;
     printf("Case #%d: %d\n",tt,r);
   }
   return 0;
}
