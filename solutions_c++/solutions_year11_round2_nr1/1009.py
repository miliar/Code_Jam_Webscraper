#include <stdio.h>
#define N 105
char g[N][N];
int n;
double WP(int x) {
  int tot=0;
  int win=0;
  for(int i=0; i<n; ++i)  {
    if(g[x][i]!='.') ++tot;
    if(g[x][i]=='1') ++win;
  }
//  printf("WP %d %d %d\n", x, win, tot);
  return 1.0*win/tot;
}
double OWP(int x) {
  int tot=0;
  double sum=0;
  for(int i=0; i<n; ++i) {
    if(g[x][i] != '.') {
      ++tot;
      char old=g[i][x];
      g[i][x]='.';
      sum += WP(i);
      g[i][x]=old;
    }
  }
//  printf("OWP %d %.2f %d\n", x, sum, tot);
  return sum/tot;
}
double OOWP(int x) {
  int tot=0;
  double sum=0;
  for(int i=0; i<n; ++i)
    if(g[x][i] != '.') {
      sum += OWP(i);
      tot++;
    }
//  printf("OOWP %d %.2f %d\n", x, sum, tot);
  return sum/tot;
}
double RPI(int x) { return 0.25*WP(x)+0.50*OWP(x)+0.25*OOWP(x); }
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<=casn; ++cas) {
    scanf("%d", &n);
    for(int i=0; i<n; ++i) scanf("%s", g[i]);
    printf("Case #%d:\n", cas);
    for(int i=0; i<n; ++i) printf("%.10f\n", RPI(i));
  }
  return 0;
}

