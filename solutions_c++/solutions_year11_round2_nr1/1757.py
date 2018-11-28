// -std=gnu++0x
#include <vector>
#include <cstdio>
#include <set>

using namespace std;

#define foreach(e,c) for (auto e=c.begin();e!=c.end();++e)

double wpx(int w, int c, char g) {
  if (g == '1') --w, --c;
  if (g == '0') --c;
  return 1.0*w/c;
}

int main() {
  int tests; scanf("%d",&tests);
  for (int t=1;t<=tests;++t) {
    printf("Case #%d:\n",t);
    int n; scanf("%d",&n);
    int i, j, k;
    vector<vector<char> > G(n,vector<char>(n));
    for (i=0;i<n;++i) for(j=0;j<n;++j) scanf(" %c",&G[i][j]);
    vector<set<int> > op(n);
    vector<int> cnt(n), win(n);
    vector<double> owp(n), oowp(n);
    for (i=0;i<n;++i) for(j=0;j<n;++j) {
      win[i] += G[i][j] == '1';
      if (G[i][j]!='.') {
        op[i].insert(j);
        ++cnt[i];
      }
    }
    for (i=0;i<n;++i) {
      foreach(x,op[i]) owp[i] += wpx(win[*x], cnt[*x], G[*x][i]);
      owp[i] /= op[i].size();
    }
    for (i=0;i<n;++i) {
      foreach(x,op[i]) oowp[i] += owp[*x];
      oowp[i]/=op[i].size();
    }
    for (i=0;i<n;++i) {
      //printf("wp=%f owp=%f oowp=%f\n",wpx(win[i],cnt[i],'.'),owp[i],oowp[i]);
      printf("%.10f\n",.25*wpx(win[i],cnt[i],'.')+.5*owp[i]+.25*oowp[i]);
    }
  }
}
