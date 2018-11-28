#include <iostream>
#include <cstdio>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair <int, int> pii;
typedef double db;
const int N  = 100000 + 5;
const db INF = 1e9;
double a[N];
int n, m;
db solve()
{
  double p = 1;
  double p1 = 1;
  double p2 = 1;
  double p22 = 1;
  cin >> m >> n;
  for (int i = 0; i < m; i++)
  {
    cin >> a[i];
    p *= a[i];
    if (i < m - 1) p1 *= a[i];
    if (i < m - 2) p2 *= a[i];
    if (i < m - 2) p22 *= a[i];
  }
  p1 *= (1 - a[m - 1]);
  if (m >= 2)
  {
    p2 *= (1 - a[m - 1]) * (1 - a[m - 2]);
    p22 *= (1 - a[m - 2]) * a[m - 1];
  }
  double v1 = INF, v2 = INF, v3 = INF, v4 = INF;
  v1 = (n - m + 1) * p + (2 * n - m + 2) * (1 - p);
  v2 = (n - m + 3) * (p + p1) + (2 * n - m + 4) * (1 - p - p1);
  if (m >= 2) v3 = (n - m + 5) * (p + p1 + p2 + p22) + (2 * n - m + 6) * (1 - p - p1 - p2 - p22);
  v4 = n + 2;
  //printf("%.5f\n%.5f\n%.5f\n%.5f\n", v1, v2, v3, v4);
  return min(min(v1, v2), min(v3, v4));
}
int main()
{
  freopen("A-small-attempt1.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tests;
  cin >> tests;
  for (int i = 1; i <= tests; i++)
    printf("Case #%d: %.6f\n", i, solve());
  return 0;
}
