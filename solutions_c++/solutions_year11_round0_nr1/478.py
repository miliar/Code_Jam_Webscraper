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


int T, N;
char who[100];
int pos[100];

int main() {
  cin >> T;
  REP(turn, T) {
    cin >> N;
    REP(i, N) {
      cin >> who[i] >> pos[i];
      --pos[i];
    }
    int ans = 0;
    int opos = 0, bpos = 0;
    REP(i, N) {
      int nexto = opos, nextb = bpos;
      bool sameo = false, sameb = false;
      if (who[i] == 'O') {
        if (pos[i] == opos) sameo = true;
        nexto = pos[i];
        for (int j = i + 1; j < N; ++j) {
          if (who[j] == 'B') {
            nextb = pos[j];
            break;
          }
        }
      } else {
        if (pos[i] == bpos) sameb = true;
        nextb = pos[i];
        for (int j = i + 1; j < N; ++j) {
          if (who[j] == 'O') {
            nexto = pos[j];
            break;
          }
        }
      }
      // move o, move b
      int dx = abs(opos - nexto), dy = abs(bpos - nextb);
      if (who[i] == 'O') {
        ans += dx + 1;
        opos = nexto;
        ++dx;
        if (dy <= dx) {
          bpos = nextb;
        } else {
          if (nextb < bpos) bpos -= dx;
          else bpos += dx;
        }
      } else {
        ans += dy + 1;
        bpos = nextb;
        ++dy;
        if (dx <= dy) {
          opos = nexto;
        } else {
          if (nexto < opos) opos -= dy;
          else opos += dy;
        }
      }
      //      cout << opos << ' ' << bpos << endl;
    }
    printf("Case #%d: %d\n", turn + 1, ans);
  }
  return 0;
}
