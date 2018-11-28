#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)

void solve()
{
  int N;
  cin >> N;
  vector<vector<char> > table(N, vector<char>(N));
  REP(i, N) {
    REP(j, N) {
      cin >> table[i][j];
    }
  }
  vector<int> win(N), lose(N);
  vector<double> WP(N), OWP(N), OOWP(N);
  REP(i, N) {
    REP(j, N) {
      if(table[i][j]=='.') continue;
      if(table[i][j]=='0') {
        lose[i]++;
      } else {
        win[i]++;
      }
    }
    WP[i] = (double)(win[i])/(win[i]+lose[i]);
    //cout << "WP " << WP[i] << endl;
  }
  REP(i, N) {
    REP(j, N) {
      if(table[i][j]=='.') continue;
      if(table[i][j]=='0') {
        OWP[i] += double(win[j]-1)/(win[j]+lose[j]-1);
      } else {
        OWP[i] += double(win[j])/(win[j]+lose[j]-1);
      }
    }
    OWP[i] /= (win[i]+lose[i]);
    //cout << "OWP " << OWP[i] << endl;
  }
  REP(i, N) {
    REP(j, N) {
      if(table[i][j]=='.') continue;
      OOWP[i] += OWP[j];
    }
    OOWP[i] /= (win[i]+lose[i]);
    printf("%1.10lf\n", (0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]));
    //cout << (0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]) << endl;
  }
}

int main()
{
  int T;
  cin >> T;
  for(int i=0;i<T;i++) {
    cout << "Case #" << (i+1) << ":" << endl;
    solve();
    cout << endl;
  }
}
