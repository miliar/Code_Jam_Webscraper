#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

int T;
string s;
int N;

int main(void) {
  cin >> T;
  REP(t,T) {
    cin >> N;
    vector<string> in(N);
    REP(i,N) cin >> in[i];

    vector<int> op(N,0);
    REP(i,N) REP(j,N) if (in[i][j]!='.') ++op[i];

    vector<int> vic(N,0);
    REP(i,N) REP(j,N) if (in[i][j]=='1') ++vic[i];

    vector<vector<int> > g(N,vector<int>(N,0));
    REP(i,N) REP(j,N) { g[i][j] = vic[i]; if (in[i][j]=='1') --g[i][j]; }

    vector<long double> WP(N,0);
    REP(i,N) WP[i] = (long double)vic[i] / (long double) op[i];

    vector<long double> OWP(N,0);
    REP(i,N) {
      REP(j,N) if (in[i][j]!='.') OWP[i]+= (long double) g[j][i] / (long double) (op[j]-1);
      OWP[i]/= (long double) op[i];
    }

    vector<long double> OOWP(N,0);
    REP(i,N) {
      REP(j,N) if (in[i][j]!='.') OOWP[i]+= OWP[j];
      OOWP[i]/= (long double) op[i];
    }

    printf("Case #%d:\n",t+1);
    REP(i,N) printf("%.10Lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
  }
  return 0;
}
