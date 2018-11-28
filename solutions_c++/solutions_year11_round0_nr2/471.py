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

int T, C, D, N;
string cs[36], ds[28], s;

int main() {
  cin >> T;
  REP(turn, T) {
    cin >> C;
    REP(i, C) cin >> cs[i];
    cin >> D;
    REP(i, D) cin >> ds[i];
    cin >> N;
    cin >> s;
    vector<char> rs;
    REP(i, N) {
      rs.push_back(s[i]);
      // combine
      for (bool success = true; success && rs.size() >= 2; ) {
        success = false;
        REP(j, C) if (cs[j][0] == rs[rs.size() - 2]
                      && cs[j][1] == rs[rs.size() - 1] ||
                      cs[j][1] == rs[rs.size() - 2]
                      && cs[j][0] == rs[rs.size() - 1] ) {
          rs.pop_back();
          rs.pop_back();
          rs.push_back(cs[j][2]);
          success = true;
        }
      }
      // oppose
      bool oppose = false;
      REP(j, rs.size()) REP(k, j) {
        REP(l, D) if (rs[j] == ds[l][0] && rs[k] == ds[l][1] ||
                      rs[j] == ds[l][1] && rs[k] == ds[l][0] ) {
          oppose = true;
        }
      }
      if (oppose) rs.clear();
    }
    printf("Case #%d: [", turn + 1);
    REP(i, rs.size()) {
      printf("%c", rs[i]);
      if (i != rs.size() - 1) printf(", ");
    }

    puts("]");
  }
  return 0;
}
