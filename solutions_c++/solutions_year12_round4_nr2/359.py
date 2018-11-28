#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <complex>
using namespace std;

// begin insert defines
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
typedef complex<double> Pt;
#define X real()
#define Y imag()

// end insert defines

const int N = 1000 + 10;

int n, W, L;
double r[N];
int id[N];
Pt ans[N];

bool findp(int nn)
{
  int c = 1000;
  while (c--) {
    int x = rand() % W;
    int y = rand() % L;
    int lab = 0;
    for (int i = 0; i < nn; i++) {
      if (abs(Pt(x, y) - ans[id[i]]) <
          r[id[i]] + r[id[nn]] + 1e-9) {
        lab = 1;
        break;
      }
    }
    if (!lab) {
      ans[id[nn]] = Pt(x, y);
      return true;
    }
  }
  return false;
}

bool check()
{
  ans[id[0]] = Pt(0, 0);
  int end = -1;
  for (int i = 1; i < n; i++) {
    if (r[id[i]] + ans[id[i - 1]].Y + r[id[i - 1]] <= L) {
      ans[id[i]] = Pt(0,
                      r[id[i]] +
                      ans[id[i - 1]].Y +
                      r[id[i - 1]]);
    }
    else {
      end = i;
      break;
    }
  }
  if (end == -1) return true;
  for (int i = end; i < n; i++) {
    if (!findp(i)) return false;
  }
  return true;
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  Rep(Ca, T) {
    cout << "Case #" << Ca + 1 << ":";
    cin >> n >> W >> L;
    Rep(i, n) cin >> r[i];
    Rep(i, n) id[i] = i;
    if (n == 1) {
      cout << " 0.0 0.0" << endl;
    }
    else {
      int s = 0;
      if (W > L) {
        swap(W, L);
        s = 1;
      }
      while (!check()) {
        random_shuffle(id, id + n);
      }
      if (s) {
        for (int i = 0; i < n; i++)
          cout << " " << int(ans[i].Y) << " " << int(ans[i].X);
      }
      else {
        for (int i = 0; i < n; i++)
          cout << " " << int(ans[i].X) << " " << int(ans[i].Y);
      }
      cout << endl;
    }
  }
  return 0;
}
