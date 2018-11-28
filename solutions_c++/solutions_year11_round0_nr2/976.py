#include <stdio.h>
int t,tt,n,m,x,y,i,j,k;
char a[44][7],b[44][7],s[111],r[111];
bool q;
int main() {
  freopen("Bl.in","r",stdin);
  freopen("Bl.out","w",stdout);
  scanf("%d",&t);
  for (tt=1; tt<=t; tt++) {
    scanf("%d",&x); for (i=0; i<x; i++) scanf("%s",a[i]);
    scanf("%d",&y); for (i=0; i<y; i++) scanf("%s",b[i]);
    scanf("%d",&n); scanf("%s",s);
    for (i=m=0; i<n; i++) {
      r[++m]=s[i];
      while (m>1) {
        q=true;
        for (j=0; j<x; j++) if ((a[j][0]==r[m] && a[j][1]==r[m-1]) || (a[j][0]==r[m-1] && a[j][1]==r[m])) {
          r[--m]=a[j][2]; q=false; break;
        }
        if (q) break;
      }
      if (m>1) {
        q=true;
        for (j=0; j<y; j++) for (k=1; k<m; k++) 
          if ((b[j][0]==r[m] && b[j][1]==r[k]) || (b[j][0]==r[k] && b[j][1]==r[m])) {
            m=0; q=false; break;
          }
      }
    }
    printf("Case #%d: [",tt);
    for (i=1; i<=m; i++) {
      putchar(r[i]);
      if (i<m) printf(", ");
    }
    puts("]");
  }
  return 0;
}
