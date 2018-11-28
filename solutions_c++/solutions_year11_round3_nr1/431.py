//#define debug#include <algorithm>
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

int main() {

  int t;
  string peta[55];

  cin >> t;
  REP(i,t) {
    int r,c;
    bool gagal = false;
    cin >> r >> c;
    REP(j, r) cin >> peta[j];
    REP(j, r) REP(k, c) {
      if(peta[j][k] == '#') {
        if(j == r-1 || k == c-1
          || peta[j][k+1] != '#' || peta[j+1][k] != '#' || peta[j+1][k+1] != '#') {
          gagal = true;
          goto udah;
        }
        peta[j][k] = peta[j+1][k+1] = '/';
        peta[j+1][k] = peta[j][k+1] = '\\';
      }
    }

    udah:;
    cout << "Case #" << i+1 << ":\n";
    if(gagal) {
      cout << "Impossible\n";
    } else {
      REP(j, r) {
        REP(k, c) cout << peta[j][k];
        cout << "\n";
      }
    }
  }

  return 0;
}

