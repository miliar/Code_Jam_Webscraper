#include <stdio.h>
#include <string.h>
int n,l,k,m,t,tt,i,j,r;
char s[5010][20],e[900];
bool a[20][250],q;
int main() {
   freopen("Al.in","r",stdin);
   freopen("Al.out","w",stdout);
   scanf("%d%d%d\n",&n,&m,&t);
   for (i=0; i<m; i++) gets(s[i]);
   for (tt=1; tt<=t; tt++) {
      gets(e); l=strlen(e); q=false;
      for (i=k=0; i<l; i++) if (e[i]=='(') { k++; q=true; } else if (e[i]==')') q=false; else {
         if (!q) k++;
         a[k][e[i]]=true;
         if (k>n) break;
      }
      r=0;
      if (k==n) {
         for (i=0; i<m; i++) {
            q=true;
            for (j=0; j<n; j++) if (!a[j+1][s[i][j]]) { q=false; break; }
            if (q) r++;
         }
      }
      printf("Case #%d: %d\n",tt,r);
      for (i=k=0; i<l; i++) if (e[i]=='(') { k++; q=true; } else if (e[i]==')') q=false; else {
         if (!q) k++;
         a[k][e[i]]=false;
      }
   }
   return 0;
}
