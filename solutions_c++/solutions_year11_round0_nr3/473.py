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

int T, N, S;
int C[1000];

int main() {
  cin >> T;
  REP(turn, T) {
    cin >> N;
    REP(i, N) cin >> C[i];
    sort(C, C + N);
    S = accumulate(C, C + N, 0);
    int exor = 0;
    REP(i, N) exor ^= C[i];
    if (exor == 0) {
      int ans = S - C[0];
      printf("Case #%d: %d\n", turn + 1, ans);
    } else {
      printf("Case #%d: NO\n", turn + 1);
    }
  }
  return 0;
}
