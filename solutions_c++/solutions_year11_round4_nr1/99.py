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

pair<double, double> A[10000];

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0 ; t  < T; ++t) {
    int S, R, tr, X, N;
    scanf("%d%d%d%d%d", &X, &S, &R, &tr, &N);
    for (int i = 0; i < N; ++i) {
      int b, e, w;
      scanf("%d%d%d", &b, &e, &w);
      int len = e-b;
      X -= len;
      A[i].first = w+S;
      A[i].second = len;
    }
    A[N].first = S;
    A[N].second = X;
    ++N;
    sort(A, A+N);
    double av = R-S;
    double tt = tr;
    double res = 0;
    for (int i = 0; i < N; ++i) {
      double v = A[i].first;
      double d = A[i].second;
      double iv = v + av;
      double it = d / iv;
      if (it > tt) {
        it = tt;
      }
      tt -= it;
      res += it;
      d -= it * iv;
      res += d / v;
    }
    printf("Case #%d: %.10lf\n", t+1, res);
  }

  return 0;
};
