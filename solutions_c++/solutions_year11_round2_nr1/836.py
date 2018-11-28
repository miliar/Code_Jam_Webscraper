#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

#define FOR(i, N, M)  for(int i = (int)(N); i <= (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)

#define MAXN 101

bool win[MAXN][MAXN];
bool play[MAXN][MAXN];
double WP[MAXN], OWP2[MAXN], OWP[MAXN][MAXN], OOWP[MAXN];

inline void solve() { 
  int N; cin >> N;
  char ch;
  FOR(i,0,N-1) FOR(j,0,N-1){
    cin >> ch;
    if(ch == '\n') {--j; continue; }
    play[i][j] = ch != '.';
    win[i][j] = ch == '1';
  }

  REP(i, N){
    int cnt = 0, wins = 0;
    REP(j, N) {
      if(play[i][j]) ++cnt;
      else continue;
      if(win[i][j]) ++wins;
    }
    WP[i] = wins / double(cnt);
    assert(cnt != 0);
    
    REP(j, N) {
      int owin = wins, ocnt = cnt;
      if(play[i][j]){
        ocnt --;
        if(win[i][j])
          owin --;
      }
      assert(ocnt != 0);
      OWP[i][j] = owin / double(ocnt);
    }
  }

  REP(i, N) {
    double sum = 0;
    int cnt = 0;
    REP(j, N) if(play[i][j]) {
      ++cnt;
      sum += OWP[j][i];
    }
    OWP2[i] = sum / cnt;
  }

  REP(i, N){
    double sum = 0;
    int cnt = 0;
    REP(j, N) if(play[i][j]) {
      ++cnt;
      sum += OWP2[j];
    }
    OOWP[i] = sum / cnt;
  }

  REP(i, N){
    double RPI = .25 * WP[i] + .5 * OWP2[i] + .25 * OOWP[i];
    printf("%.6lf\n", RPI);
    //cout  << RPI << endl;
  }
}

int main() {
  int TESTS;
  cin >> TESTS;
  FOR(test, 1, TESTS) {
    cout << "Case #" << test << ": " << endl;
    solve();
  }
} 
