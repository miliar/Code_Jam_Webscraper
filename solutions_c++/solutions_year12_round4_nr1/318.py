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

int R[11000];
int D[11000];
int L[11000];

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0 ; t < T; ++t) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
      scanf("%d%d", &D[i], &L[i]);
    int X;
    scanf("%d", &X);

    CLEAR(R, -1);
    R[0] = D[0];
    for (int i = 0; i < N; ++i) {
      if (R[i] == -1)
        continue;
      for (int j = i+1; j < N; ++j)
        if (D[j] - D[i] <= R[i]) {
          int nr = min(D[j] - D[i], L[j]);
          if (R[j] == -1 || R[j] < nr)
            R[j] = nr;
        }
    }
    bool found = false;
    for (int i = 0; i < N; ++i)
      if (R[i] != -1 && X - D[i] <= R[i])
        found = true;
    printf("Case #%d: %s\n", t+1, found ? "YES" : "NO");


    fprintf(stderr, "%d/%d\n", t+1, T);
  }

  return 0;
};
