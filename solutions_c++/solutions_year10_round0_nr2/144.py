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

int n;
ll a[maxn];

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    scanf("%d", &n);
    forn(i, n)
      scanf("%I64d", &a[i]);

    ll r = abs(a[0] - a[1]);
    for (int i = 2; i < n; i++)
      r = __gcd(r, abs(a[0] - a[i]));

    ll res = 0;
    if (r != 0)
      res = (r - (a[0] % r)) % r;
    fprintf(stderr, "r = %I64d\n", r);
    forn(i, n)
      fprintf(stderr, "%I64d %I64d\n", a[i], abs(a[0] - a[i]));

    printf("Case #%d: %I64d\n", tt, res);
  }
  return 0;
}
