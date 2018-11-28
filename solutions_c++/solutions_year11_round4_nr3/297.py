#include <iostream>

using namespace std;

int nprimes[1000002];

int main()
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  for (int i = 2; i <= 1000000; i++)
  {
  	if (!nprimes[i])
  		for (int j = i + i; j <= 1000000; j += i)
  			nprimes[j] = 1;
  }
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		__int64 n;
		cin >> n;
		int ans = n > 1 ? 1 : 0;
		for (__int64 i = 2; i * i <= n; i++)
		{	
			if (nprimes[i]) continue;
			for (int c = i; n / c >= i; c *= i, ans++);
		}
		cout << ans;
    cout << endl;
  }
  return 0;
}