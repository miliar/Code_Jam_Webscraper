#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <queue>
#include <set>
using namespace std;
typedef long long ll;

const int N = 128;

int check(char c1, char c2, char c3, char c4) {
  if (c1 == '.' || c2 == '.' || c3 == '.' || c4 == '.') return 0;
  int ans = 0;
  if (c1 == 'O' || c2 == 'O' || c3 == 'O' || c4 == 'O') ans |= 1;
  if (c1 == 'X' || c2 == 'X' || c3 == 'X' || c4 == 'X') ans |= 2;
  if (ans == 3) ans = 0;
  return ans;
}
int main()
{
#ifdef _ZZZ_
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
#endif
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; ++tt) {
    char g[8][8];
    for(int i = 0; i < 4; ++ i) {
      scanf("%s", g[i]);
    }
    bool finish = true;
    for(int i = 0;finish && i < 4; ++ i) {
      for(int j = 0; j < 4; ++ j) {
        if (g[i][j] == '.') {
          finish = false;
          break;
        }
      }
    }

    int outcome = 0; // draw
    for(int i = 0;outcome == 0 &&  i < 4; ++ i) {
      int tmp = check(g[i][0], g[i][1], g[i][2], g[i][3]);
      if (tmp != 0) {
        outcome = tmp;
      }
    }
    for(int i = 0;outcome == 0 &&  i < 4; ++ i) {
      int tmp = check(g[0][i], g[1][i], g[2][i], g[3][i]);
      if (tmp != 0) {
        outcome = tmp;
      }
    }
    if (outcome == 0) {
      int tmp = check(g[0][0], g[1][1], g[2][2], g[3][3]);
      if (tmp != 0) {
        outcome = tmp;
      }
    }

    if (outcome == 0) {
      int tmp = check(g[0][3], g[1][2], g[2][1], g[3][0]);
      if (tmp != 0) {
        outcome = tmp;
      }
    }
    cout << "Case #" << tt << ": ";
    if (outcome == 0) {
      cout << (finish ? "Draw" : "Game has not completed") << endl;
    } else {
      cout << ((outcome == 2) ? "X won" : "O won") << endl;
    }
  }

  return 0;
}










