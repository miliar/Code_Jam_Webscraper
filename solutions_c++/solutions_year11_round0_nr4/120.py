#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>

#define F(i,a,b) for(int i=a;i<b;++i)
#define rep(i,b) F(i,0,b)
#define all(a) a.begin(),a.end()

using namespace std;

#define DPN 1001
int dp[DPN];

int main() {
  memset(dp, 0, sizeof(dp));
  dp[0] = 0;
  
  int T;
  scanf("%d", &T);
  rep(t, T) {
    int N;
    scanf("%d", &N);
    int c[N];
    rep(i, N) scanf("%d", c + i);
    int der = 0;
    rep(i, N) {
      if (i+1 != c[i]) ++der;
    }
    printf("Case #%d: %d\n", t+1, der);
  }
}
