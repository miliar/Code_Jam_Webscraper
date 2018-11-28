#include <cstdio>
#include <algorithm>
using namespace std;
int t,tt,i,j,d,p,n,m,a[555][555],s1[555][555],s2[555][555];
long long x,y;
char st[555];
int main() {
  freopen("Bs.in","r",stdin);
  freopen("Bs.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%*d",&n,&m);
    for (i=1; i<=n; i++) {
      scanf("%s",st);
      for (j=1; j<=m; j++) {
        a[i][j]=st[j-1]-'0';
        s1[i][j]=s1[i-1][j]+a[i][j];
        s2[i][j]=s2[i][j-1]+a[i][j];
      }
    }
    for (d=min(n,m); d>2; d--) {
      for (i=1; i+d<=n+1; i++) {
        for (j=1; j+d<=m+1; j++) {
          for (x=p=0; p<d; p++) if (p==0 || p==d-1) {
            x+=(s2[i+p][j+d-2]-s2[i+p][j])*(d-2*p-1);
          } else {
            x+=(s2[i+p][j+d-1]-s2[i+p][j-1])*(d-2*p-1);
          }
          for (y=p=0; p<d; p++) if (p==0 || p==d-1) {
            y+=(s1[i+d-2][j+p]-s1[i][j+p])*(d-2*p-1);
          } else {
            y+=(s1[i+d-1][j+p]-s1[i-1][j+p])*(d-2*p-1);
          }
          if (x==0 && y==0) break;
        }
        if (j+d<=m+1) break;
      }
      if (i+d<=n+1) break;
    }
    printf("Case #%d: ",t);
    if (d>2) printf("%d\n",d); else puts("IMPOSSIBLE");
  }
  return 0;
}
