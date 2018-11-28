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

/*
#define x first
#define y second
//*/

inline int nextint() {
  int res = 0;
  int neg = 1;

  char c = 0; while (c != '-' && (c < '0' || c > '9')) c = getchar();
  if (c == '-') c = '0', neg = -1;
  while (c >= '0' && c <= '9') {
    res = res * 10 + c - '0';
    c = getchar();
  }
  return neg * res;
}

#ifdef _DEBUG
  #define dbg(x) { cerr << #x << " = " << x << endl; }
#else
  #define dbg(x) ;
#endif

#define forn(_i,_n) for (int _i = 0; _i < (int)(_n); ++_i)
#define mp make_pair

#define SIZE 550
int data[SIZE][SIZE];
ll sum[SIZE][SIZE];
ll wxsum[SIZE][SIZE];
ll wysum[SIZE][SIZE];

ll get_sum(int i, int j, int size) {
  return sum[i + size][j + size] + sum[i][j] -
    sum[i + size][j] - sum[i][j + size];
}

ll get_fsum(int i, int j, int size) {
  ll result = get_sum(i, j, size);

  result -= data[i][j] + data[i + size - 1][j] + data[i + size - 1][j + size - 1] + data[i][j + size - 1];

  return result;
}

ll get_xsum(int i, int j, int size) {
  ll result = wxsum[i + size][j + size] + wxsum[i][j] -wxsum[i + size][j] - wxsum[i][j + size];

  result -= i * get_sum(i, j, size);

  result -= (size - 1) * (data[i + size - 1][j] + data[i + size - 1][j + size - 1]);

  return result;
}

ll get_ysum(int i, int j, int size) {
  ll result = wysum[i + size][j + size] + wysum[i][j] - wysum[i + size][j] - wysum[i][j + size];

  result -= j * get_sum(i, j, size);

  result -= (size - 1) * (data[i][j + size - 1] + data[i + size - 1][j + size - 1]);

  return result;
}

int main() {
  cout.precision(15);
  cout << fixed;

  int _T; cin >> _T;
  for (int _t = 1; _t <= _T; _t++) {
    cerr << _t << " ";

    cout << "Case #" << _t << ": ";
    
    int r, c, d;
    cin >> r >> c >> d;
    forn (i, r) forn (j, c) {
      char _c = 0; while (_c < '0' || _c > '9') _c = getchar();
      data[i][j] = _c - '0';
    }

    memset(sum, 0, sizeof (sum));
    memset(wxsum, 0, sizeof (wxsum));
    memset(wysum, 0, sizeof (wysum));

    forn (i, r) forn (j, c) {
      sum[i + 1][j + 1] = sum[i][j + 1];
      forn (_j, j + 1) sum[i + 1][j + 1] += data[i][_j];

      wxsum[i + 1][j + 1] = wxsum[i][j + 1];
      forn (_j, j + 1) wxsum[i + 1][j + 1] += i * data[i][_j];

      wysum[i + 1][j + 1] = wysum[i][j + 1];
      forn (_j, j + 1) wysum[i + 1][j + 1] += _j * data[i][_j];
    }

    int ans = 0;

    forn (i, r) forn (j, c) for (int size = 3; i + size <= r && j + size <= c; size++) {
      ll sx = get_xsum(i, j, size); 
      ll sy = get_ysum(i, j, size);
      ll s = get_fsum(i, j, size);

      ll c2x = size - 1, c2y = size - 1;
      if (2 * sx == s * c2x && 2 * sy == s * c2y) ans = max(ans, size);
    }

    if (ans < 3) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
    
   
  }

  return 0;
}
