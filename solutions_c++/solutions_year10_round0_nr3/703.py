#include <cstdio>
using namespace std;
int t,tt,i,j,e,y,r,rr,k,n,a[2010],b[2010];
long long s[2010],d,cs,ss,z,x;
int main() {
   freopen("Cl.in","r",stdin);
   freopen("Cl.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d%d%d",&r,&k,&n); rr=r;
     for (ss=i=0; i<n; i++) { scanf("%d",&a[i]); ss+=a[i]; b[i]=0; }
     if (k>=ss) { printf("Case #%d: %I64d\n",tt,ss*r); continue; } else s[0]=0;
     for (i=1, j=0; rr>0; i++) {
       cs=0; z=k; s[i]=0;
       while (z>=a[j]) {
         z-=a[j]; cs+=a[j];
         if (++j==n) j=0;
       }
       s[i]=s[i-1]+cs;
       if (b[j]!=0) {
         d=s[i]-s[b[j]]; e=i-b[j];
         x=(rr-1)/e; y=(rr-1)%e;
         printf("Case #%d: %I64d\n",tt,s[i]+x*d+s[b[j]+y]-s[b[j]]);
         break;
       } else b[j]=i;
       rr--;
     }
     if (rr==0) printf("Case #%d: %I64d\n",tt,s[i-1]);
   }
   return 0;
}
