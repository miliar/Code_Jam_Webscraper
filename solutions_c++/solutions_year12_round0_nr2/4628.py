#include <iostream>
#include <cmath>

using namespace std;

int main(void)
{
  int T;
  cin >> T;
  for (int _t = 0; _t < T; ++_t)
  {
    int n, s, p;
    cin >> n >> s >> p;
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
      int t;
      cin >> t;
      if (p + 2 * max(p - 1, 0) <= t)
      {
        ++ans;
        continue;
      }
      if (p + 2 * max(p - 2, 0) <= t && s > 0)
      {
        --s;
        ++ans;
      }
    }
    cout << "Case #" << _t + 1 << ": " << ans << endl;
  }
  return 0;
}
