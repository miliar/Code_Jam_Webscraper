#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;
#define pb          push_back
#define all(a)      (a).begin(),(a).end()
#define sz(a)       (int)((a).size())
#define REP(i,j,k)  for(int i=j;i<k;++i)
#define rep(i,n)    for(int i=0;i<n;++i)

int main () {
  int T; scanf("%d", &T);

  rep (tc, T) {
    int N; scanf("%d", &N);
    vector<int> v(N);
    rep (i, N) scanf("%d", &v[i]);
    sort(all(v));

    int s = 0;
    REP (i, 1, N) s += v[i];
    int x = 0;
    REP (i, 1, N) x ^= v[i];
    if (v[0]-x) printf("Case #%d: NO\n", tc+1);
    else        printf("Case #%d: %d\n", tc+1, s);
  }
  return 0;
}
