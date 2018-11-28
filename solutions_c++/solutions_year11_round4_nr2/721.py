#include <stdio.h>
#define N 15
char g[N][N];
#define eps 1e-8
bool eq(double a, double b) {
  return a-b<eps && a-b>-eps;
}
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<= casn; ++cas) {
    int n, m, d;
    int res=0;
    scanf("%d%d%d", &n, &m, &d);
    
    for(int i=0; i<n; ++i) scanf("%s", g[i]);
    for(int i=0; i<n; ++i) {
      for(int j=0;j<m; ++j) {
        for(int ii=i+1; ii<n; ++ii) {
          for(int jj=j+1; jj<m; ++jj) {
            if(jj-j!=ii-i) continue;
            
            double x=0;
            double y=0;
            double mess=0;
            for(int ki=i; ki<=ii; ++ki) {
              for(int kj=j; kj<=jj; ++kj) {
                if(ki==i && kj==j || ki==i && kj==jj || ki==ii && kj==jj || ki==ii && kj==j) continue;
                x+=ki*(g[ki][kj]-'0'+d);
                y+=kj*(g[ki][kj]-'0'+d);
                mess+=(g[ki][kj]-'0'+d);
              }
            }
            x/=mess;
            y/=mess;
            if(eq(x, (ii+i)/2.0) && eq(y, (jj+j)/2.0) && res < ii-i+1) {
              res=ii-i+1;
            }
          }
        }
      }
    }
    if(res >= 3) printf("Case #%d: %d\n", cas, res);
    else printf("Case #%d: IMPOSSIBLE\n", cas);
  }
  return 0;
}

