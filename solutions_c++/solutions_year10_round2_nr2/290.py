#include <iostream>

using namespace std;

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    int n, k, b, Time;
    cin >> n >> k >> b >> Time;
    int x[100], v[100];
    for (int i = 0; i < n; i++)
    {
      cin >> x[i];
    }
    for (int i = 0; i < n; i++)
    {
      cin >> v[i];
    }
    int ans = 0;
    int cnt = k;
    for (int i = n-1; i >= 0; i--)
    {
      if (b - x[i] > Time * v[i])
      {
        ans += cnt;
      }
      else
      {
        cnt--;
        if (cnt == 0) break;
      }
    }
    if (cnt > 0)
    {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    cout << ans << endl;
  }
  return 0;
}