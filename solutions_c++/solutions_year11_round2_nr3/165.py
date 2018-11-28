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

int U[3000], V[3000];

int used[100];
bool ok[100];
bool u_m[100];

vector<vector<int> > A;

int C[100];
bool c_u[100];
bool check(int c) {

  forn (i, A.size()) {
    memset(c_u, 0, sizeof c_u);
    forn (j, A[i].size())
      c_u[C[A[i][j]]] = true;

    forn (j, c) if (!c_u[j]) return false;
  }

  return true;
}

bool done;
int n;
void color(int start, int c) {
  if (start == n) {
    if (check(c) && !done) {
      cout << c << endl;
      forn (i, n)
        cout << (C[i] + 1) << " ";
      cout << endl;
      done = true;
    }
    return;
  }

  forn (i, c) {
    C[start] = i;
    color(start + 1, c);
  }
}

int main() {
  int _t; cin >> _t;
  cout.precision(15);
  cout << fixed;

  forn (__t, _t) {
    cout << "Case #" << (__t + 1) << ": ";

    int m; cin >> n >> m;
    forn (i, m) {cin >> U[i]; U[i]--; }
    forn (i, m) {cin >> V[i]; V[i]--; }

    assert(n < 10);
    forn (i, n) ok[i] = true;
    forn (i, m) u_m[i] = false;

    A.clear();

    forn (i, m) {
      int a = U[i], b = V[i];
      if (a > b) swap(a, b);
      used[a]++; used[b]++;
    }

    while (true) {
      bool f = false;
      forn (i, m) if (!u_m[i]) {
        f = true;

        int a = U[i], b = V[i];
        if (a > b) swap(a, b);

        bool ok1 = true;
        for (int j = a + 1; j < b && ok1; j++) ok1 = !used[j];

        if (ok1) {
          vector<int> add;
          add.push_back(a); add.push_back(b);
          for (int j = a + 1; j < b && ok1; j++) if (ok[j]) {
            ok[j] = false;
            add.push_back(j);
          }

          A.push_back(add);
        }

        bool ok2 = true;
        for (int j = (b + 1) % n; j != a && ok2; j = (j + 1) % n) ok2 = !used[j];

        if (ok2) {
          vector<int> add;
          add.push_back(a); add.push_back(b);
          for (int j = (b + 1) % n; j != a && ok2; j = (j + 1) % n) if (ok[j]) {
            ok[j] = false;
            add.push_back(j);
          }

          A.push_back(add);
        }

        if (ok1 || ok2) {
          u_m[i] = true;
          used[a]--;
          used[b]--;
        }
      }

      if (!f) break;
    }

    done = false;
    for (int c = n; !done; c--) color(0, c);
  }
  

  return 0;
}
