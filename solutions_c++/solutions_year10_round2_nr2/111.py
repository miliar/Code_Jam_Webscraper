#include <cstdio>
using namespace std;
int t,tt,i,j,e,r,n,k,x[55],v[55],a[55];
long long b,m;
int main() {
   freopen("Bl.in","r",stdin);
   freopen("Bl.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d%d%I64d%I64d",&n,&k,&b,&m);
     for (i=0; i<n; i++) { scanf("%d",&x[i]); x[i]=b-x[i]; a[i]=0; }
     for (i=0; i<n; i++) scanf("%d",&v[i]);
     for (i=n-1, e=r=0; i>=0 && e<k; i--) if (x[i]<=m*v[i]) {
       e++; a[i]=1;
       for (j=i; j<n; j++) if (a[j]==0) r++;
     }
     printf("Case #%d: ",tt);
     if (e<k) puts("IMPOSSIBLE"); else printf("%d\n",r);
   }
   return 0;
}
