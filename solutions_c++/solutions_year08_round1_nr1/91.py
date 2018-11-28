#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

long long a[1001], b[1001];

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++) 
  {
    printf("Case #%d:", tt);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
      cin >> a[i];
    for (int i = 0; i < n; i++)
      cin >> b[i];
    sort(a, a + n);
    sort(b, b + n);
    long long res = 0;
    for (int i = 0; i < n; i++)
      res += a[i] * (b[n - i - 1]);
    cout << " " << res << endl;
  }

  return 0;
}