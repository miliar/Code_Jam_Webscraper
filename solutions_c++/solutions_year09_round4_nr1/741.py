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

int nTestCases;
int N, ans;
vector<int> v;

void read_input()
{
  cin >> N >> ws;
  v.resize(N);
  FOR (i, N) {
    string s;
    getline(cin, s);
    v[i] = 0;
    FOR (j, N) if (s[j] == '1') v[i] = j;
  }
}

void solve()
{
  vector<int> perm;
  FOR (i, N) perm.push_back(i);

  ans = 0;
  FOR (i, N) {
    int k = 0;
    FOR3 (j, i, N) if (v[perm[j]] <= i) { k = j; break; }
    for (int j = k; j > i; --j) {
      swap(perm[j], perm[j - 1]);
      ++ans;
    }
  }
}

int main()
{
  cin >> nTestCases;
  REP (i, nTestCases) {
    read_input();
    solve();
    cout << "Case #" << i << ": " << ans << endl;
  }

  return 0;
}
