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


int sign(int x) {
  if (x < 0)
    return -1;
  else if (x > 0)
    return 1;
  return 0;
}

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    int N;
    scanf("%d", &N);
    vector<int> Pos[2];
    vector<bool> Turn;
    int Cur[2] = {1, 1};
    char buf[100];
    for (int i = 0; i < N; ++i) {
      int a;
      scanf("%s%d", buf, &a);
      if (buf[0] == 'O') {
	Turn.PB(0);
	Pos[0].PB(a);
      } else {
	Turn.PB(1);
	Pos[1].PB(a);
      }
    }

    int p[2] = {0, 0};
    int res = 0;
    for (int tp = 0; tp < Turn.size(); ++tp) {
      int guy = Turn[tp];
      int dist = abs(Pos[guy][p[guy]] - Cur[guy]) + 1;
      Cur[guy] = Pos[guy][p[guy]];
      res += dist;
      p[guy]++;
      int other = 1 - guy;
      if (p[other] < Pos[other].size()) {
	int dif = Pos[other][p[other]] - Cur[other];
	int od = min(dist, abs(dif));
	Cur[other] += sign(dif)*od;
      }
    }
    printf("Case #%d: %d\n", t+1, res);

  }
  
  return 0;
};
