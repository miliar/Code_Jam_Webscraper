#include <cstdio>
#include <memory.h>
#include <algorithm>
using namespace std;
int rr,t,tt,n,i,j,l,r,h,z,m1,m2,m,x[2200],y[2200],x1[2200],x2[2200],y1[2200],y2[2200],xa,ya,xb,yb,f[2200][2200];
bool a[2200][2200],b[2200][2200];
int main() {
   freopen("Cs.in","r",stdin);
   freopen("Cs.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d",&n); m=0;
     for (i=0; i<n; i++) {
       scanf("%d%d%d%d",&x1[i],&y1[i],&x2[i],&y2[i]);
       x2[i]++; y2[i]++;
       x[m]=x1[i]; y[m++]=y1[i];
       x[m]=x2[i]; y[m++]=y2[i];
     }
/*     sort(x,x+m);
     sort(y,y+m); m1=m2=0;
     for (i=1; i<m; i++) if (x[i]!=x[m1]) x[++m1]=x[i];
     for (i=1; i<m; i++) if (y[i]!=y[m2]) y[++m2]=y[i];
     memset(a,false,sizeof(a));
     for (i=0; i<n; i++) {
       l=0; r=m1;
       while (l<r) {
         h=(l+r)/2;
         if (x[h]>=x1[i]) r=h; else l=h+1;
       }
       xa=r; l=0; r=m1;
       while (l<r) {
         h=(l+r)/2;
         if (x[h]>=x2[i]) r=h; else l=h+1;
       }
       xb=r; l=0; r=m2;
       while (l<r) {
         h=(l+r)/2;
         if (y[h]>=y1[i]) r=h; else l=h+1;
       }
       ya=r; l=0; r=m2;
       while (l<r) {
         h=(l+r)/2;
         if (y[h]>=y2[i]) r=h; else l=h+1;
       }
       yb=r;
       for (; xa<xb; xa++) for (j=ya; j<yb; j++) a[xa][j]=true;
     }
     for (i=1; i<=m1; i++) for (j=1; j<=m2; j++) a[i][j]|=((a[i-1][j])&(a[i][j-1]));
     for (r=i=0; i<m1; i++) for (j=0; j<m2; j++) if (a[i][j]) {
       if (f[i+1][j]+f[i][j+1]==0) z=y[j+1]-y[j]+x[i+1]-x[i]-1; else z=max(f[i+1][j]+y[j+1]-y[j],f[i][j+1]+x[i+1]-x[i]);
       f[i+1][j+1]=z;
       if (z>r) r=z;
     } else f[i+1][j+1]=0;
     if (tt==25) for (i=0; i<=m1; i++,puts(""))for (j=0; j<=m2; j++) printf("%d",a[i][j]);
//     if (tt==25) for (i=0; i<=m1; i++,puts(""))for (j=0; j<=m2; j++) printf("%d ",f[i][j]);
memset(a,false,sizeof(a));
for (i=0; i<n; i++) for (xa=x1[i]; xa<x2[i]; xa++) for (ya=y1[i]; ya<y2[i]; ya++) a[xa][ya]=true;
for (i=1; i<=110; i++) for (j=1; j<=110; j++) a[i][j]|=((a[i-1][j])&(a[i][j-1]));
     for (rr=i=0; i<=110; i++) for (j=0; j<=110; j++) if (a[i][j]) {
       z=max(f[i+1][j]+1,f[i][j+1]+1);
       f[i+1][j+1]=z;
       if (z>rr) rr=z;
     } else f[i+1][j+1]=0;
     if (tt==25) for (i=0; i<=110; i++,puts(""))for (j=0; j<=110; j++) printf("%d",a[i][j]);
//     if (tt==25) for (i=0; i<=110; i++,puts(""))for (j=0; j<=110; j++) printf("%d ",f[i][j]);
*/memset(a,false,sizeof(a));
memset(b,false,sizeof(b));
for (i=0; i<n; i++) for (xa=x1[i]; xa<x2[i]; xa++) for (ya=y1[i]; ya<y2[i]; ya++) a[xa][ya]=true;
for (z=1; ; z++) {
int e=0;
if (z&1) {
  for (i=1; i<=110; i++) for (j=1; j<=110; j++) if (!a[i][j]) {
    if (a[i-1][j] && a[i][j-1]) { b[i][j]=true; e++; } else b[i][j]=false;
  } else {
    if (a[i-1][j]==false && a[i][j-1]==false) b[i][j]=false; else { b[i][j]=true; e++; }
  }    
//  if (tt==25) for (i=0; i<=110; i++,puts(""))for (j=0; j<=110; j++) printf("%d",b[i][j]);
} else {
  for (i=1; i<=110; i++) for (j=1; j<=110; j++) if (!b[i][j]) {
    if (b[i-1][j] && b[i][j-1]) { a[i][j]=true; e++; } else a[i][j]=false;
  } else {
    if (b[i-1][j]==false && b[i][j-1]==false) a[i][j]=false; else { a[i][j]=true; e++; }
  }
//  if (tt==25) for (i=0; i<=110; i++,puts(""))for (j=0; j<=110; j++) printf("%d",a[i][j]);
}
//if (tt==25) puts("");
if (e==0) { break; }
}
r=z;
     printf("Case #%d: %d\n",tt,r);
//     if (r!=z) puts("!!!!!");
//     if (tt==25) break;
   }
   return 0;
}
