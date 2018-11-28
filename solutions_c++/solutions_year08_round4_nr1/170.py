#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define DEBUG(format, args...) { fprintf(stderr, format, ## args); fflush(stderr); }
#define PRINT(format, args...) { fprintf(stdout, format, ## args); DEBUG(format, ## args); }

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int MAX_NODES=10008;
const int INF=1000000000;

int N;
int op[MAX_NODES];
int ch[MAX_NODES];
int vl[MAX_NODES];
int mz[MAX_NODES][2];

bool isInterior(int n);
int recurse(int n, int v);

int main() {
  int i, j, A, t, T, V;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d %d", &N, &V);
    for (i=1; i<=(N-1)/2; i++)
      scanf("%d %d", op+i, ch+i);
    for (j=1; j<=(N+1)/2; j++)
      scanf("%d", vl+i+j-1);
    memset(mz, -1, sizeof mz);
    if ((A=recurse(1, V))!=INF)
      PRINT("Case #%d: %d\n", t, A)
    else
      PRINT("Case #%d: IMPOSSIBLE\n", t)
  }
  return 0;
}

bool isInterior(int n) {
  return n<=(N-1)/2;
}

int recurse(int n, int v) {
  int &A=mz[n][v];
  if (A<0) {
    A=INF;
    if (isInterior(n)) {
      int ca=(op[n]==1 ? 0 : 1);
      int co=(op[n]==0 ? 0 : 1);
      if (op[n]==1 || ch[n])
        if (v==0) {
          A=min(A, ca+recurse(2*n, 0)+recurse(2*n+1, 0));
          A=min(A, ca+recurse(2*n, 0)+recurse(2*n+1, 1));
          A=min(A, ca+recurse(2*n, 1)+recurse(2*n+1, 0));
        }
        else
          A=min(A, ca+recurse(2*n, 1)+recurse(2*n+1, 1));
      if (op[n]==0 || ch[n])
        if (v==0)
          A=min(A, co+recurse(2*n, 0)+recurse(2*n+1, 0));
        else {
          A=min(A, co+recurse(2*n, 0)+recurse(2*n+1, 1));
          A=min(A, co+recurse(2*n, 1)+recurse(2*n+1, 0));
          A=min(A, co+recurse(2*n, 1)+recurse(2*n+1, 1));
        }
    }
    else
      A=(vl[n]==v ? 0 : INF);
  }
  return A;
}
