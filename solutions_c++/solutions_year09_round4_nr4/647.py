#include <algorithm>
#include <iostream>
#include <iomanip>
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
#include <complex>
#include <limits>
#include <cassert>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef complex<double> C;

const double pi = 3.141592653589793238462643383279;
const double napier = 2.718281828459045235360287471352;
const C eye = C(0, 1);

#define FOREACH(it, col) for (typeof((col).begin()) it = (col).begin(); it != (col).end(); ++it)
#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define FOR3(i, m, n) for (int i = (int)m; i < (int)(n); ++i)
#define REP(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()

struct Plant {
  double x, y, r;
};

int nTestCases;
int N;
vector<Plant> plants;
double ans;

void read_input()
{
  cin >> N;
  plants.resize(N);
  FOR (i, N) {
    cin >> plants[i].x >> plants[i].y >> plants[i].r;
  }
}

double find_r(int i, int j) {
  Plant &p = plants[i];
  Plant &q = plants[j];
  return 0.5 * (sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)) + p.r + q.r);
}

void solve()
{
  if (N == 1)
    ans = plants[0].r;
  if (N == 2)
    ans = max(plants[0].r, plants[1].r);
  if (N == 3) {
    ans = 10000000;
    ans = min(ans, max(plants[0].r, find_r(1, 2)));
    ans = min(ans, max(plants[1].r, find_r(0, 2)));
    ans = min(ans, max(plants[2].r, find_r(0, 1)));
  }
}

int main()
{
  cin >> nTestCases;
  REP (i, nTestCases) {
    read_input();
    solve();
    cout.precision(16);
    cout << "Case #" << i << ": " << ans << endl;
  }

  return 0;
}
