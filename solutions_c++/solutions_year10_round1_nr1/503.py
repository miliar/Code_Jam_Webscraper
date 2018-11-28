#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
#include <memory>
#include <cstring>
#include <climits>
#include <cassert>
#include <list>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBGN(x) cout << #x << " = " << x << endl;
#define DBG(x) cout << #x << " = " << x << ", ";
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

int m[55][55], tmp[55][55];
int N, K;

void print_table() {
  REP(i, N) {
    REP(j, N) {
      char c;
      if (m[i][j] == 0) {
        c = '.';
      } else if (m[i][j] == 1) {
        c = 'R';
      } else {
        c = 'B';
      }
      cout << c;
    }
    cout << endl;
  }
  cout << endl;
}

void rotate() {
  memset(tmp, 0, sizeof(tmp));
  REP(i, N) REP(j, N) {
    tmp[i][j] = m[N - 1 - j][i];
  }
  REP(i, N) REP(j, N) {
    m[i][j] = tmp[i][j];
  }
}

void gravity() {
  REP(j, N) {
    size_t offset = 0;
    vector<int> vals;
    FORD(i, N - 1, 0) {
      if (m[i][j]) {
        vals.PB(m[i][j]);
      }
    }
    while (SIZE(vals) < N) {
      vals.PB(0);
    }
    FORD(i, N - 1, 0) {
      m[i][j] = vals[N - 1 - i];
    }
  }
}

inline bool ok(int i, int j) {
  return ((i >= 0) && (i < N) && (j >= 0) && (j < N));
}

int check_val(const vector<int>& v) {
  if (SIZE(v) < K)
    return false;
  int res = 0;
  vector<int> cnt(2, 0);
  REP(i, SIZE(v)) {
    if (v[i] == 0) {
      cnt[0] = cnt[1] = 0;
    } else if (v[i] == 1) {
      ++cnt[0];
      cnt[1] = 0;
      if (cnt[0] == K) {
        res |= 1;
      }
    } else if (v[i] == 2) {
      ++cnt[1];
      cnt[0] = 0;
      if (cnt[1] == K) {
        res |= 2;
      }
    }
  }
  return res;
}

string doit() {
  //  print_table();
  rotate();
  //  print_table();
  gravity();
  //  print_table();
  vector<int> vals;
  int res = 0;
  // horizontal
  REP(i, N) {
    vals.clear();
    REP(j, N) {
      vals.PB(m[i][j]);
      res |= check_val(vals);
    }
  }
  // vertical
  REP(j, N) {
    vals.clear();
    REP(i, N) {
      vals.PB(m[i][j]);
      res |= check_val(vals);
    }
  }
  // diag
  // up - right
  int jj = 0;
  REP(ii, N) {
    vals.clear();
    int i = ii;
    int j = jj;
    while (ok(i, j)) {
      vals.PB(m[i][j]);
      --i;
      ++j;
    }
    res |= check_val(vals);
  }
  int ii = N - 1;
  REP(jj, N) {
    vals.clear();
    int i = ii;
    int j = jj;
    while (ok(i, j)) {
      vals.PB(m[i][j]);
      --i;
      ++j;
    }
    res |= check_val(vals);
  }
  // down - right
  jj = 0;
  REP(ii, N) {
    vals.clear();
    int i = ii;
    int j = jj;
    while (ok(i, j)) {
      vals.PB(m[i][j]);
      ++i;
      ++j;
    }
    res |= check_val(vals);
  }
  ii = 0;
  REP(jj, N) {
    vals.clear();
    int i = ii;
    int j = jj;
    while (ok(i, j)) {
      vals.PB(m[i][j]);
      ++i;
      ++j;
    }
    res |= check_val(vals);
  }
  if (res == 0) {
    return "Neither";
  } else if (res == 1) {
    return "Red";
  } else if (res == 2) {
    return "Blue";
  } else {
    assert(res == 3);
    return "Both";
  }
}

int main()
{
  freopen(FIN, "r", stdin);
  freopen(FOUT, "w", stdout);

  int tests;
  cin >> tests;
  REP(z, tests) {
    cin >> N >> K;
    memset(m, 0, sizeof(m));
    REP(i, N) {
      string s;
      cin >> s;
      REP(j, N) {
        if (s[j] == 'R') {
          m[i][j] = 1;
        } else if (s[j] == 'B') {
          m[i][j] = 2;
        }
      }
    }
    cout << "Case #" << z + 1 << ": ";
    cout << doit();
    cout << endl;
  }

  fclose(stdin);
  fflush(stdout);
  fclose(stdout);
  return 0;
}
