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

int R[1010];
int Ind[1010];
int X[1010];
int Y[1010];

int findY(int x, int ind) {
  int r = R[ind];
  int y = -r;
  for (int i = 0; i < ind; ++i) {
    if (x+r <= X[i] - R[i] || x-r >= X[i] + R[i])
      continue;
    y = max(y, Y[i] + R[i]);
  }
  return y + r;
}

int main()
{
  int T, t;
  scanf("%d", &T);
  for (t = 0; t < T; ++t) {
    int N, W, L;
    scanf("%d%d%d", &N, &W, &L);
    for (int i = 0; i < N; ++i)
      scanf("%d", &R[i]);
    vector<PII> vp;
    vp.clear();
    for (int i = 0; i < N; ++i)
      vp.PB(PII(R[i], i));
    sort(ALL(vp));
    reverse(ALL(vp));
    for (int i = 0; i < N; ++i) {
      R[i] = vp[i].first;
      Ind[vp[i].second] = i;
    }
    for (int i = 0; i < N; ++i) {
      int bx, by;
      bx = 0;
      by = findY(bx, i);
      int nx, ny;
      for (int j = 0; j < i; ++j) {
        nx = X[j] + R[j] + R[i];
        ny = findY(nx, i);
        if (nx >= 0 && nx <= W && ny >= 0 && ny <= L) {
          if (ny < by || ny == by && nx < bx) {
            bx = nx;
            by = ny;
          }
        }
      }
      if (by > L) {
        fprintf(stderr, "\n!!! Error\n");
        exit(0);
      }
      X[i] = bx;
      Y[i] = by;
    }
    printf("Case #%d:", t+1);
    for (int i = 0; i < N; ++i)
      printf(" %d %d", X[Ind[i]], Y[Ind[i]]);
    printf("\n");
    /*
    for (int i = 0; i < N; ++i) {
      if (X[i] < 0 || X[i] >= W || Y[i] < 0 || Y[i] >= L) {
        fprintf(stderr, "\n!!! Error1\n");
        exit(0);
      }
      for (int j = i+1; j < N; ++j) {
        Int d2 = (X[i] - X[j]) * (Int)(X[i] - X[j]) + (Y[i] - Y[j]) * (Int)(Y[i] - Y[j]);
        if (d2 < (R[i] + R[j]) * (Int)(R[i] + R[j])) {
          fprintf(stderr, "\n!!! Error2\n");
          exit(0);
        }
      }
    }
    */
    fprintf(stderr, "\n%d/%d\n", t+1, T);
  }

  return 0;
};
