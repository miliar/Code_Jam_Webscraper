// Philip_PV

#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cassert>
#include <ctime>
#include <memory.h>
//#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<double, double> pdd;
typedef pair<int, int> pii;

#ifdef _DEBUG
  #define dbg(x) { cerr << #x << " = " << x << endl; }
#else
  #define dbg(x) ;
#endif

#define forn(_i,_n) for (int _i = 0; _i < (int)(_n); ++_i)
#define mp make_pair

#define SIZE 5

int r, c;
vector<pii> g[SIZE][SIZE];

void add(int i, int j, int x, int y) {
  i += r; j += c;
  x += r; y += c;

  i %= r; j %= c;
  x %= r; y %= c;

  g[i][j].push_back(mp(x, y));
  g[x][y].push_back(mp(i, j));
}

char data[SIZE][SIZE];


int main() {
  cout.precision(15);
  cout << fixed;
  int _T; cin >> _T;
  for (int _t = 1; _t <= _T; ++_t) {
    cout << "Case #" << _t << ": ";


    cin >> r >> c;
    forn (i, r) forn (j, c) {
      char c = 0;
      while (c != '|' && c != '-' && c != '\\' && c != '/') c = getchar();
      data[i][j] = c;
    }

    cerr << "*" << endl;
    int cnt = r * c;
    int ans = 0;

    forn (mask, 1 << cnt) {
      int m = mask;
      forn (i, r) forn (j, c) g[i][j].clear();
    forn (i, r) forn (j, c) {
      char c = data[i][j];

      if (c == '|') {
        if (m & 1) add(i, j, i + 1, j);
        else add(i, j, i - 1, j);
      } else if (c == '-') {
        if (m & 1) add(i, j, i, j + 1);
        else add(i, j, i, j - 1);
      } else if (c == '\\') {
        if (m & 1) add(i, j, i + 1, j + 1);
        else add(i, j, i - 1, j - 1);
      } else if (c == '/') {
        if (m & 1) add(i, j, i + 1, j - 1);
        else add(i, j, i - 1, j + 1);
      }    
      m >>= 1;
    }

      bool ok = true;
      forn (i, r) forn (j, c)
        if (g[i][j].size() != 2) ok = false;
      if (ok) ans++;

    }

    cout << ans << endl;


  }

  

  return 0;
}
