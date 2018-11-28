#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>

#define F(i,a,b) for(int i=a;i<b;++i)
#define rep(i,b) F(i,0,b)
#define all(a) a.begin(),a.end()

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  rep(t, T) {
    int N;
    scanf("%d", &N);
    int c[N];
    rep(i, N) {
      scanf("%d", c + i);
    }

    int x = 0;
    rep(n, N) {
      x ^= c[n];
    }
    if (x != 0) {
      printf("Case #%d: NO\n", t+1);
    } else {
      sort(c, c+N);
      int sum = 0;
      rep(n, N) {
        sum += c[n];
      }
      printf("Case #%d: %d\n", t+1, sum-c[0]);
    }
  }
}
