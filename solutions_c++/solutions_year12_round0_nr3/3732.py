#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

int T, A, B;
bool vis[2000001];

int main()
{
  cin >> T;
  for (int tc = 1; tc <= T; ++tc)
  {
    memset(vis, false, sizeof vis);
    cin >> A >> B;
    int pow10 = 1;
    while (pow10*10 <= A)
      pow10 *= 10;
    ll ans = 0;
    
    for (int i = A; i <= B; ++i)
    if (!vis[i])
    {
      int j = i, cnt = 0;
      do {
	if (A <= j && j <= B && !vis[j])
	{
	  vis[j] = true;
	  cnt++;
	}
	j = j/10 + (j%10)*pow10;
      } while (j != i);
      ans += cnt*(cnt-1)/2;
    }
    cout << "Case #" << tc << ": " << ans << endl;
  }
}