#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;


int N;
Int D[10010], L[10010];

Int dp[10010];

Int main2() {
  int N; cin >> N;
  REP(i, N) {
      cin >> D[i] >> L[i];
  }
  Int goal; cin >> goal;
  
  const int inf = 1001001001;
  bool res = false;
  REP(i, N + 2) dp[i] = -inf;

  dp[0] = 0;
  for (int n = 0; n < N; n++) {
      if (dp[n] >= D[n] - L[n]) {
          Int len = D[n] - dp[n];
          for (int j = n + 1; j < N; j++) {
              if (D[j] <= D[n] + len) {
                  int nj = max(D[n], D[j] - L[j]);
                  if (dp[j] == -inf || dp[j] > nj) {
                      dp[j] = nj;
                  }
              } else
                  break;
          }
          if (D[n] + len >= goal) {
              res = true;
          }
      }
  }

  if (res)
      cout << "YES" << endl;
  else
      cout << "NO" << endl;

  return 0;
}

int main() {
  int TNO; scanf("%d\n", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
      
    printf("Case #%d: ", tno);
    main2();
  }
  return 0;
}

// ./a.exe < B-large.in | tee B-large.res
