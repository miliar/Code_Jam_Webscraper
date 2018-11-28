#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;

ll gcd(ll a, ll b) {
  return a == 0 ? b : gcd(b % a, a);
}

const int kMin = 1;
const int kMax = 2000000;

int T, A, B;
set<int> rots[kMax + 1];

int CountDigit(int n) {
  int digit = 0;
  for (; n != 0; n /= 10, ++digit);
  return digit;
}

int Rotate(int n, int digit) {
  int a = n / 10;
  int b = n % 10;
  for (int i = 0; i < digit - 1; ++i) b *= 10;
  int ret = a + b;
  return ret;
}

void Prepare() {
  for (int n = kMin; n <= kMax; ++n) {
    int digit = CountDigit(n);
    int m = n;
    for (int i = 0; i < digit - 1; ++i) {
      m = Rotate(m, digit);
      if (digit == CountDigit(m) && m > n) rots[n].insert(m);
    }
  }
}

int main() {
  Prepare();
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int ans = 0;
    cin >> A >> B;
    for (int n = A; n <= B; ++n) {
      set<int>::iterator it = rots[n].begin();
      while (it != rots[n].end()) {
	if (*it <= B) ++ans;
	++it;
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
