#include <cstdio>
#include <memory.h>
#include <algorithm>
using namespace std;
const int zz=2000000;
int t,tt,n,i,j,k,c,r,fi,fr,a[2*zz],q[256],md=100003;
bool u[2*zz];
int main() {
   freopen("Cs.in","r",stdin);
   freopen("Cs.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     memset(a,0,sizeof(a)); r=0;
     scanf("%d",&n); fi=0; fr=1;
     for (i=0; i<n; i++) {
       scanf("%d%d",&j,&k); j+=zz;
       a[j]=k; u[j]=true; q[fr++]=j;
     }
     while (fi!=fr) {
       j=q[fi]; u[j]=false;
       fi=(fi+1)&255;
       if (a[j]>1) {
         c=a[j]/2; r+=c;
         a[j]-=c; a[j-1]+=c;
         if (!u[j-1]) { u[j-1]=true; q[fr]=j-1; fr=(fr+1)&255; }
         a[j]-=c; a[j+1]+=c;
         if (!u[j+1]) { u[j+1]=true; q[fr]=j+1; fr=(fr+1)&255; }
       }
     }
     printf("Case #%d: %d\n",tt,r);
   }
   return 0;
}
