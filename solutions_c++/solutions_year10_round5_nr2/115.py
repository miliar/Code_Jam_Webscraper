#include <cstdio>
#include <memory.h>
#include <algorithm>
using namespace std;
int t,tt,i,j,k,p,n,a[105],d,f[105][11000];
long long m,r;
int nod(int a, int b) { return (b==0)?a:nod(b,a%b); }
int main() {
   freopen("Bs.in","r",stdin);
   freopen("Bs.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%I64d%d",&m,&n); r=m+1;
     for (i=0; i<n; i++) {
       scanf("%d",&a[i]);
     }
     d=10050;
     memset(f,120,sizeof(f)); f[0][0]=0;
     for (i=0; i<n; i++) for (j=0; j<d; j++) if (f[i][j]!=f[0][10999]) {
       for (k=0, p=j; p<d; k++, p+=a[i]) f[i+1][p]=min(f[i+1][p],f[i][j]+k);
     }
     for (i=0; i<n; i++) for (j=m%a[i]; j<d; j+=a[i]) if (f[n][j]!=f[0][10999]) {
       r=min(r,f[n][j]+(m-j)/a[i]);
     }
     printf("Case #%d: ",tt);
     if (r==m+1) puts("IMPOSSIBLE"); else printf("%I64d\n",r);
   }
   return 0;
}
