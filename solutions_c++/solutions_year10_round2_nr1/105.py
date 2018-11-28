#include <cstdio>
#include <cstring>
using namespace std;
int t,tt,nn,mm,n,m,i,j,ii,k,r;
char s[250][250];
int main() {
   freopen("Al.in","r",stdin);
   freopen("Al.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
     scanf("%d%d",&nn,&mm); gets(s[0]); r=0;
     for (ii=0; ii<nn; ii++) { gets(s[ii]); n=strlen(s[ii]); s[ii][n+1]=0; s[ii][n]='/'; }
     for (ii=nn; ii<nn+mm; ii++) {
       gets(s[ii]); n=strlen(s[ii]); s[ii][n]='/'; s[ii][n+1]=0; k=1;
       for (i=0; i<ii; i++) {
         m=strlen(s[i]);
         for (j=0; j<=n && j<=m; j++) if (s[i][j]!=s[ii][j]) break;
         if (j>k) k=j;
       }
       for (i=k; i<=n; i++) if (s[ii][i]=='/') r++;
     }
     printf("Case #%d: %d\n",tt,r);
   }
   return 0;
}
