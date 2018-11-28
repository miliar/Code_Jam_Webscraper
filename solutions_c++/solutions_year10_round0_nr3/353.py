#include <algorithm>
#include <cstdio>
using namespace std;

typedef long long ll;

int main() {
  int cases;
  scanf("%i", &cases);
  for (int numcase = 1; numcase <= cases; ++numcase) {
    ll r, k;
    int n;
    scanf("%lli%lli%i", &r, &k, &n);

    ll g[n], a[n], b[n];
    for (int i = 0; i < n; ++i)
      scanf("%lli", &g[i]);

    for (int i = 0; i < n; ++i) {
      ll sum = 0;
      int j;
      for (j = i; j < i + n; ++j) {
        ll s = sum + g[j % n];
        if (s <= k) sum = s;
        else break;
      }
      a[i] = j % n;  // next group
      b[i] = sum;    // money earned
    }

    int pos = 0, startcycle, endcycle;
    int visited[n], index;
    ll sum[n];

    fill(&visited[0], &visited[n], -1);
    sum[0] = 0;
    for (index = 0; index < r && visited[pos] < 0; ++index) {
      visited[pos] = index;
      sum[index + 1] = sum[index] + b[pos];
      pos = a[pos];
    }

    ll total = 0;
    if (r <= index) total = sum[r];
    else {
      endcycle = index;
      startcycle = visited[pos];
      total = sum[startcycle] + (sum[endcycle] - sum[startcycle]) * ((r - startcycle) / (endcycle - startcycle));
      r = (r - endcycle) % (endcycle - startcycle);
      total += sum[r + startcycle] - sum[startcycle];
    }
    printf("Case #%i: %lli\n", numcase, total);
  }
  return 0;
}
