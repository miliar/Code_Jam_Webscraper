#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int maxn = 1010;

int R, k, n, a[maxn];
ll sum[maxn];
int cnt[maxn];

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    scanf("%d%d%d", &R, &k, &n);
    forn(i, n)
      scanf("%d", &a[i]);

    int pos = 0;
    ll money = 0;
    int rest = R;
    memset(cnt, 0, sizeof(cnt));
    while (rest > 0)
    {
      if (cnt[pos])
      {
        int num = abs(rest - cnt[pos]);
        ll dm = abs(money - sum[pos]);
        int t = (rest - 1) / num;

        money += dm * t;
        rest -= num * t;
      }

      sum[pos] = money, cnt[pos] = rest;
      int x = 0, y = 0;
      while (x + a[pos] <= k && y < n)
        x += a[pos++], y++, pos %= n;
      money += x, rest--;
    }

    printf("Case #%d: %I64d\n", tt, money);
  }
  return 0;
}
