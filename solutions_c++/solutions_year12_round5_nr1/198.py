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

struct Level {
  int ind;
  int t;
  int p;
  bool operator < (const Level& L) const {
    if (p == 0 && L.p == 0)
      return ind < L.ind;
    if (p != L.p)
      return p > L.p;
    if (t != L.t)
      return t < L.t;
    return ind < L.ind;
  }
};

Level L[1010];

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0 ; t < T; ++t) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
      scanf("%d", &L[i].t);
    for (int i = 0; i < N; ++i)
      scanf("%d", &L[i].p);
    for (int i = 0; i < N; ++i)
      L[i].ind = i;
    sort(L, L+N);
    printf("Case #%d:", t+1);
    for (int i = 0; i < N; ++i)
      printf(" %d", L[i].ind);
    printf("\n");
  }

  return 0;
};
