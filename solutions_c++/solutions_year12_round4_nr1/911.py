#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>

#define FOR(i, m, n) for (int i=m; i<n; i++)
typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int N;
ll d[20000];
ll l[20000];
ll res[20000];

void solve() {
  scanf("%d", &N);
  FOR (i, 0, N) {
    scanf("%lld %lld", &d[i], &l[i]);
  }
  FOR (i, 0, N+1) res[i] = -1;
  scanf("%lld", &d[N]); l[N] = 0;
  res[0] = d[0];
  FOR (i, 0, N) {
    FOR (j,i+1, N+1) {
      if (res[j]==-1 && d[i]+res[i]>=d[j] && d[j]-d[i]<=l[i])
	res[j] = d[j]-d[i];
    }
    //printf("%d ", res[i]);
  }
  //printf("\n");
  if (res[N]==-1) printf("NO\n");
  else printf("YES\n");
}

int main()
{
  int t; scanf("%d", &t);
  FOR (i, 0, t) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}
