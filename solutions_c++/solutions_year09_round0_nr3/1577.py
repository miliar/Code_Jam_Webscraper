#include <iostream>
#include <algorithm>
#include <vector>
#include <complex>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <bitset>
#include <queue>
#include <iomanip>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef complex<double> C;

const double pi = 3.141592653589793238462643383279;
const double napier = 2.718281828459045235360287471352;
const C eye = C(0, 1);

#define FOR(i,n) for (unsigned i = 0; i < (n); ++i)
#define REP(i,n) for (unsigned i = 1; i <= (n); ++i)
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).begin(), (v).end()

int N;

int cnt;
int s[19];
string text;
string phrase = "welcome to code jam";

void dfs(int d) {
  if (d == 19) {
    ++cnt;
    return;
  }

  int len = text.size();
  int pos = 0;
  if (d > 0)
    pos = s[d - 1] + 1;
  if (pos >= len)
    return;

  for (int i = pos; i < len; ++i) {
    if (text[i] == phrase[d]) {
      s[d] = i;
      dfs(d + 1);
    }
  }
}

int main()
{
  cin >> N >> ws;
  FOR (i, N) {
    cout << "Case #" << i + 1 << ": ";
    getline(cin, text);
    cnt = 0;
    dfs(0);
    cout << setw(4) << setfill('0') << cnt << endl;
  }

  return 0;
}
