#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;

#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

typedef long long ll;

int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int N;
    scanf("%d", &N);
    vector<ll> X(N), Y(N);
    rep (i, N) cin >> X[i];
    rep (i, N) cin >> Y[i];
    sort(all(X));
    sort(all(Y));
    reverse(all(Y));
    ll ans = 0;
    rep (i, N) ans += X[i] * Y[i];
    printf("Case #%d: %lld\n", t, ans);
  }
  return 0;
}
