#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <queue>
#include <cstring>
using namespace std;

#define loop(i,n) for (int i = 0; i < (int)(n); ++i)
#define Bounded(x,a,b) ((a) <= (x) && (x) <= (b))
#define db(x) #x << " = " << x
#define pdb(x) printf("#x = %d\n",x);
#define All(x) x.begin(),x.end()
#define sz(x) x.size()
typedef vector<int> Vi;
typedef pair<int,int> Pii;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;

void solve(int casenum) {
  int rows, cols; cin >> rows >> cols;
  vector<string> a(rows);
  loop(i,rows) cin >> a[i];

  loop(i,rows) loop(j,cols) {
    if (a[i][j] == '#') {
      if (i >= rows-1 || j >= cols-1) continue;
      if (a[i+1][j] != '#') continue;
      if (a[i][j+1] != '#') continue;
      if (a[i+1][j+1] != '#') continue;
      a[i][j] = '/';
      a[i+1][j] = '\\';
      a[i][j+1] = '\\';
      a[i+1][j+1] = '/';
    }
  }

  bool possible = true;
  loop(i,rows) loop(j,cols)
    possible = possible && a[i][j] != '#';

  printf("Case #%d:\n", casenum);
  if (possible)
    loop(i,rows)
      cout << a[i] << endl;
  else
    cout << "Impossible" << endl;
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}

