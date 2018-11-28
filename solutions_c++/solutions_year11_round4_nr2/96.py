#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

Int W[510][510];

Int SW[510][510];
Int SXW[510][510];
Int SYW[510][510];
Int XW[510][510];
Int YW[510][510];
char buf[1000];


int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    int R, C, D;
    scanf("%d%d%d", &R, &C, &D);
    for (int i = 0; i < R; ++i) {
      scanf("%s", buf);
      for (int j = 0; j < C; ++j)
        W[i][j] = D + (int)(buf[j] - '0');
    }
    for (int i = 0; i < R; ++i) {
      SW[i][0] = 0;
      SXW[i][0]= 0;
    }
    for (int i = 0; i < C; ++i) {
      SW[0][i] = 0;
      SXW[0][i]= 0;
    }
    for (int i = 1; i <= R; ++i)
      for (int j = 1; j <= C; ++j) {
        SW[i][j] = SW[i-1][j] + SW[i][j-1] - SW[i-1][j-1] + W[i-1][j-1];
        XW[i-1][j-1] =  ((i-1)*2 + 1) * W[i-1][j-1];
        SXW[i][j] = SXW[i-1][j] + SXW[i][j-1] - SXW[i-1][j-1] + XW[i-1][j-1];
        YW[i-1][j-1] = ((j-1)*2 + 1) * W[i-1][j-1];
        SYW[i][j] = SYW[i-1][j] + SYW[i][j-1] - SYW[i-1][j-1] + YW[i-1][j-1];
      }
    int res = 0;
    bool good = false;
    for (res = min(R, C); res >= 3; --res) {
      for (int x = 0; x+res <= R && !good; ++x)
        for (int y = 0; y+res <= C; ++y) {
          int ex = x + res;
          int ey = y+res;
          Int sx = SXW[ex][ey] - SXW[x][ey] - SXW[ex][y] + SXW[x][y]
            - XW[x][y] - XW[ex-1][y] - XW[x][ey-1] - XW[ex-1][ey-1]
            - (ex+x) * (SW[ex][ey] - SW[x][ey] - SW[ex][y] + SW[x][y]
            - W[x][y] - W[ex-1][y] - W[x][ey-1] - W[ex-1][ey-1]);
          Int sy = SYW[ex][ey] - SYW[x][ey] - SYW[ex][y] + SYW[x][y]
            - YW[x][y] - YW[ex-1][y] - YW[x][ey-1] - YW[ex-1][ey-1]
            - (ey+y) * (SW[ex][ey] - SW[x][ey] - SW[ex][y] + SW[x][y]
            - W[x][y] - W[ex-1][y] - W[x][ey-1] - W[ex-1][ey-1]);
          if (sx == 0 && sy == 0) {
            good = true;
            break;
          }
        }
      if (good)
        break;
    }
    printf("Case #%d: ", t+1);
    if (good)
      printf("%d\n", res);
    else
      printf("IMPOSSIBLE\n");


    fprintf(stderr, "%d/%d\n", t+1, T);
  }

  return 0;
};
