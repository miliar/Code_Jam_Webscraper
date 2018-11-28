#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cassert>
using namespace std;
typedef long long ll;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,k,n) for(int i = (k); i < (int)(n); ++i)
#define FOREQ(i,k,n) for(int i = (k); i <= (int)(n); ++i)
#define FORIT(i,c) for(__typeof((c).begin())i=(c).begin(); i!=(c).end(); ++i)
#define SZ(v) (int)((v).size())
#define MEMSET(v,h) memset((v),(h),sizeof(v))

bool eq(char val, char expected) {
  return val == 'T' || val == expected;
}

char const cc[2] = {'X', 'O'};

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; ++t) {
    string board[4];
    for(auto &line: board) cin >> line;

    bool won[2] = {0, 0}, incomp = 0;
    REP(j, 4) REP(i, 4)if(board[j][i] == '.') incomp = 1;

    REP(a, 2) {
      auto const c = cc[a];
      REP(j, 4) {
        bool wo = 1;
        REP(i, 4) wo &= eq(board[j][i], c);
        won[a] |= wo;
      }
      REP(i, 4) {
        bool wo = 1;
        REP(j, 4) wo &= eq(board[j][i], c);
        won[a] |= wo;
      }
      {
        bool wo = 1;
        REP(i, 4) wo &= eq(board[i][i], c);
        won[a] |= wo;
      }
      {
        bool wo = 1;
        REP(i, 4) wo &= eq(board[3-i][i], c);
        won[a] |= wo;
      }
    }

    assert(!(won[0] && won[1]));
    cout << "Case #" << t << ": ";
    if(won[0]) {
      cout << "X won" << endl;
    } else if(won[1]) {
      cout << "O won" << endl;
    } else if(incomp) {
      cout << "Game has not completed" << endl;
    } else {
      cout << "Draw" << endl;
    }
  }
}
