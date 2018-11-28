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

int K[11000];

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    CLEAR(K, 0);
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
      int x;
      scanf("%d", &x);
      K[x]++;
    }

    if (N == 0) {
      printf("Case #%d: 0\n", t+1);
      continue;
    }

    int res = 1000000;
    priority_queue<int, VInt, greater<int> > Q;
    for (int i = 1; i <= 10001; ++i) {
      int k = K[i];
      while (Q.size() > k) {
        int x = Q.top();
        Q.pop();
        res = min(res, i - x);
      }
      while (Q.size() < k) {
        Q.push(i);
      }
    }
    printf("Case #%d: %d\n", t+1, res);
  }

  return 0;
};
