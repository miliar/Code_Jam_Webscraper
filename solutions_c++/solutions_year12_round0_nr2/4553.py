#include <iostream>

using namespace std;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T, t, n, s, p, x,  ans;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		ans = 0;
		cin >> n >> s >> p;
		for (int i = 0; i < n; i++)
		{
			cin >> x;
			if (p == 0)
			{
				ans++;
				continue;
			}
			if (x == 0)
				continue;
			if (x >= 3 * p - 2)
				ans++;
			else
				if (s && x >= 3 * p - 4)
				{
					ans++;
					s--;
				}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
