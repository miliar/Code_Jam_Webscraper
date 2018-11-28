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
#include <cmath>  
#include <list>  
using namespace std;  

#define PB push_back  
#define MP make_pair  
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  
typedef long long ll;  


void solve()
{
  int n;
  scanf("%d",&n);
  vector<int> wins;
  vector<int> loses;
  vector<double> wp;
  vector<double> owp;
  vector<double> oowp;
  vector<vector<int> > checked;
  vector<string> winlose;

  checked.resize(n);
  for(int i = 0; i < n; ++i) {
    char buf[1024];
    scanf("%s",buf);
    winlose.PB(buf);
    int win = 0;
    int lose = 0;
    for(int j = 0; j < n; ++j) {
       if(buf[j] == '1') ++win;
       else if(buf[j] == '0') ++lose;
       if(buf[j] != '.') {
         checked[i].PB(j);
       }
    }
    wp.PB(double(win) / double(win+lose));
    wins.PB(win);
    loses.PB(lose);
  }
  for(int i = 0; i < n; ++i) {
    double towp = 0.;
    REP(j,SZ(checked[i])) {
      int win = wins[checked[i][j]];
      int lose = loses[checked[i][j]];
      if(winlose[i][checked[i][j]] == '1') --lose;
      else --win;
      towp += double(win) / double(win+lose);
    }
    owp.PB(towp / SZ(checked[i]));
  }
  for(int i = 0; i < n; ++i) {
    double towp = 0.;
    REP(j,SZ(checked[i])) {
      towp += owp[checked[i][j]];
    }
    oowp.PB(towp / SZ(checked[i]));
  }
  REP(i,n) {
    printf("%.12lf\n",wp[i] * 0.25 + 0.5 * owp[i] + 0.25 * oowp[i]);
  }
}


int main(int argc, char *argv[])
{
  int kase;
  scanf("%d", &kase);
  FORE(i,1,kase) {
    printf("Case #%d:\n",i);
    solve();
  }

  return 0;
}
