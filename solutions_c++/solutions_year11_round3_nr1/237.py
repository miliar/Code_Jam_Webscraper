#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define eps (1e-6)

void dumpV(vector<int> v) {
  cout << "v{";
  REP(i, v.size()){
    cout << v[i] << " ";
  }
  cout << "}" << endl;
}

void solve()
{
  int R, C;
  cin >> R >> C;
  vector<vector<char > > b(R, vector<char>(C));
  REP(i, R) {
    REP(j, C) {
      cin >> b[i][j];
    }
  }
  REP(i, R-1) {
    REP(j, C-1) {
      if(b[i][j]=='#' && b[i+1][j]=='#' && b[i][j+1]=='#' && b[i+1][j+1]=='#') {
        b[i][j] = '/';
        b[i][j+1] = '\\';
        b[i+1][j] = '\\';
        b[i+1][j+1] = '/';
      }
    }
  }
  REP(i, R) {
    REP(j, C) {
      if(b[i][j]=='#') {
        cout << "Impossible" << endl;
        return;
      }
    }
  }
  REP(i, R) {
    REP(j, C) {
      cout << b[i][j];
    }
    cout << endl;
  }
}

int main()
{
  int T;
  cin >> T;
  for(int i=0;i<T;i++) {
    cout << "Case #" << (i+1) << ":" << endl;
    solve();
  }
}
