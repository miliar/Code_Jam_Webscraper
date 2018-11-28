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

#define MAX 1000010

int P[MAX] = {0};
Int Pr[MAX];
int kpr;

void seive() {
  Int i, j;
  kpr = 0;
  P[0] = P[1] = 1;
  for (i = 2; i < MAX; ++i)
    if (P[i] == 0) {
      Pr[kpr++] = i;
      for (j = i*i; j < MAX; j += i)
        P[j] = 1;
    }
}

Int F(Int N) {
  if (N == 1)
    return 0;
  Int res = 1;
  for (int i = 0; Pr[i]*Pr[i] <= N; ++i) {
    Int pr = Pr[i];
    Int m = pr * pr;
    int k = 0;
    while (m <= N) {
      ++k;
      m*= pr;
    }
    res += k;
  }
  return res;
}


int main()
{
  seive();

  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    Int N;
    scanf("%lld", &N);
    Int res = F(N);
    printf("Case #%d: %lld\n", t+1, res);

    fprintf(stderr, "%d/%d\n", t+1, T);
  }

  return 0;
};
