#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int t,tt,n,m,i,j,ii,jj,x,y,c,r,rr;
char s[120][120];
bool q;
int main() {
   freopen("Al.in","r",stdin);
   freopen("Al.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d",&n); rr=0;
     for (i=1; i<=n; i++) rr-=i;
     for (i=n-1; i>0; i--) rr-=i;
     n=2*n-1; gets(s[0]); r=n*10;
     for (i=0; i<n; i++) for (j=0; j<n; j++) s[i][j]=' ';
     for (i=0; i<n; i++) { gets(s[i]); s[i][strlen(s[i])]=' '; }
     for (ii=0; ii<n; ii++) for (jj=0; jj<n; jj++) {
       q=true; c=0;
       for (i=0; i<n; i++) {
         x=ii+(ii-i);
         for (j=0; j<n; j++) {
           y=jj+(jj-j);
           if (s[i][j]!=' ') {
             c=max(c,abs(i-ii)+abs(j-jj)+1);
             if (x>=0 && x<n && s[x][j]!=' ' && s[i][j]!=s[x][j]) q=false;
             if (y>=0 && y<n && s[i][y]!=' ' && s[i][j]!=s[i][y]) q=false;
           }
         }
       }
       if (q && c<r) r=c;
     }
     for (i=1; i<=r; i++) rr+=i;
     for (i=r-1; i>0; i--) rr+=i;
     printf("Case #%d: %d\n",tt,rr);
   }
   return 0;
}
