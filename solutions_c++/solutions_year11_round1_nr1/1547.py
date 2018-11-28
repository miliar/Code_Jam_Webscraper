#include <iostream>

using namespace std;

int gcd(int a, int b)
{
	if(b == 0) return a;
	return gcd(b, a % b);
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int k, i, t, n, pd, pg;
	cin >> t;
	for(i = 1 ; i <= t ; i++)
	{
		cin >> n >> pd >> pg;
		k = gcd(pd, 100);
		cout << "Case #" << i << ": ";
		if(n < 100 / k)
			cout << "Broken\n";
		else
		{
			if(pg == 0)
			{
				if(pd == 0) cout << "Possible\n";
				else cout << "Broken\n";
			}
			else if(pg == 100)
			{
				if(pd == 100) cout << "Possible\n";
				else cout << "Broken\n";
			}
			else cout << "Possible\n";
		}
	}
	return 0;
}
