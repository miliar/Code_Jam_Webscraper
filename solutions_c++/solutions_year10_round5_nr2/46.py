#include <cstdio>
#include <cassert>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long int64;

vector<int> lens;

int64 solve(int64 L)
{
  int m = lens[0];
  int n = lens.size();
  int ile[111111];
  int64 suma[111111];
  bool done[111111] = {};
  ile[0] = 0;
  suma[0] = 0;
  int const INF = 1 << 30;
  for (int i = 1; i < m; i++) {
    ile[i] = INF;
    suma[i] = 0;
  }
  priority_queue<pair<int64, int>, vector<pair<int64, int> >, greater<pair<int64, int> > > Q;
  Q.push(make_pair(0, 0));
  while (!Q.empty()) {
    int x = Q.top().second;
    Q.pop();
    if (done[x]) continue;
    done[x] = true;
    for (int a = 1; a < n; a++) {
      int y = (x + lens[a]) % m;
      int d = 1;
      d -= (x + lens[a]) / m;
      assert(d >= 0);
      if (ile[y] > ile[x] + d) {
        ile[y] = ile[x] + d;
        suma[y] = suma[x] + lens[a];
        Q.push(make_pair(ile[y], y));
      }
    }
  }
  if (ile[L % m] < INF && suma[L % m] <= L) {
    return ile[L % m] + L / lens[0];
  } else return -1;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int case_ = 1; case_ <= T; case_++) {
    int64 L;
    int n;
    scanf("%lld %d", &L, &n);
    lens.clear();
    for (int i = 0; i < n; i++) {
      int x;
      scanf("%d", &x);
      lens.push_back(x);
    }
    sort(lens.begin(), lens.end());
    reverse(lens.begin(), lens.end());
    printf("Case #%d: ", case_);
    int64 res = solve(L);
    if (res < 0) puts("IMPOSSIBLE");
    else printf("%lld\n", res);
  }
}
