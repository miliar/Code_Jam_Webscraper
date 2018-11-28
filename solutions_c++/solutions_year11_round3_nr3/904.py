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

int T, N, L, H;

ll gcd(ll a, ll b) {
  return a == 0 ? b : gcd(b % a, a);
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> N >> L >> H;
    vector<int> notes(N);
    for (int i = 0; i < N; ++i) {
      cin >> notes[i];
    }

    bool done = false;
    for (int note = L; note <= H; ++note) {
      bool ok = true;
      for (int i = 0; i < N; ++i) {
	if ((note % notes[i] == 0) || (notes[i] % note == 0)) {
	  continue;
	} else {
	  ok = false;
	  break;
	}
      }
      if (ok) {
	printf("Case #%d: %d\n", t, note);
	done = true;
	break;
      }
    }
    if (!done) {
      printf("Case #%d: NO\n", t);
    }
  }
}








