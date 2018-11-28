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

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    int N, S, p;
    scanf("%d%d%d", &N, &S, &p);
    int res = 0;
    for (int i = 0; i < N; ++i) {
      int x;
      scanf("%d", &x);
      if (x >= p + max(p-1, 0) * 2) {
        res++;
        continue;
      }
      if (S > 0 && x >= p + max(p-2, 0) * 2) {
        --S;
        ++res;
        continue;
      }
    }
    printf("Case #%d: %d\n", t+1, res);
  }

  return 0;
};
