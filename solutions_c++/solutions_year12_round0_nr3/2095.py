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

int F(int x, int A, int B) {
  int y = x;
  int k = 10;
  while (k <= x) {
    k *= 10;
  }
  k /= 10;

  int res = 0;

  while (true) {
    bool added = false;
    if (y % 10 != 0) {
      ++res;
      added = true;
    }
    y = y%10 * k + y/10;
    if (y == x) {
      if (added)
        --res;
      break;
    }
    if (added && (y > x || y < A || y > B))
      --res;
  }
  return res;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int a, b;
    scanf("%d%d", &a, &b);
    int res = 0;
    for (int x = a; x <= b; ++x)
      res += F(x, a, b);
    printf("Case #%d: %d\n", t+1, res);
  }

  return 0;
};
