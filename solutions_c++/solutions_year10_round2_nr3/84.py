#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define PRUSH(stream, format, args...) do { fprintf(stream, format, ## args); fflush(stream); } while (0)
#define DEBUG(format, args...) do { PRUSH(stderr, format, ## args); } while (0)
#define PRINT(format, args...) do { PRUSH(stdout, format, ## args); DEBUG(format, ## args); } while (0)

#define SIZE(__c) (int)(__c).size()
#define FOREACH(__i, __c) for (typeof(__c.begin()) __i=__c.begin(); __i!=__c.end(); ++__i)

typedef signed long long int i64;

const int MAX=503;
const i64 MOD=100003;

i64 ch[MAX][MAX];
i64 sw[MAX];
i64 mz[MAX][MAX];

i64 choose(int n, int k);
i64 recurse(int n, int N);

int main() {
  int i, j;
  ch[0][0]=1;
  for (i=1; i<MAX; i++) {
    ch[i][0]=1;
    for (j=1; j<=i; j++) {
      ch[i][j]=ch[i-1][j-1]+ch[i-1][j];
      ch[i][j]%=MOD;
    }
  }
  memset(mz, -1, sizeof mz);
  for (i=2; i<MAX; i++)
    for (j=1; j<i; j++) {
      recurse(i, j);
      sw[i]+=mz[i][j];
      sw[i]%=MOD;
    }
  int N, t, T;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%d", &N);
    PRINT("Case #%d: %lld\n", t, sw[N]);
  }
  return 0;
}

i64 choose(int n, int k) {
  if (k>n)
    return 0;
  else
    return ch[n][k];
}

i64 recurse(int n, int N) {
  i64 &A=mz[n][N];
  if (A<0) {
    A=0;
    if (n>N)
      if (n==1)
        A=1;
      else if (N==1)
        A=1;
      else
        for (int i=1; i<=N-1; i++) {
          A+=choose(n-N-1, N-i-1)*recurse(N, i);
          A%=MOD;
        }
  }
  return A;
}
