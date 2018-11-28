# include <iostream>
# include <deque>
# include <string>
# include <memory.h> 
# include <limits.h>

using namespace std;

long long maxcandy;
long long  candy[1010];
int n;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int tests;
	cin >> tests;

	for(int tcase = 1; tcase <= tests; ++tcase)
	{
		cin >> n;
		long long  sxor = 0;
		long long  s = 0;
		long long  mincandy = INT_MAX;
		for (int i = 0; i < n; ++i)
		{
			cin >> candy[i];
			sxor ^= candy[i];
			s += candy[i];
			mincandy = min(mincandy, candy[i]);
		}

		if (sxor != 0)
		{
			cout << "Case #" << tcase << ": NO" << endl;
			continue;
		}

		cout << "Case #" << tcase << ": " << s - mincandy << endl;
	}

	return 0;
}