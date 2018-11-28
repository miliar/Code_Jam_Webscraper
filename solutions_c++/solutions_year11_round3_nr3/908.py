#include <iostream>

using namespace std;

int A[10005];

int main()
{
	int n, t, l, h, x, ok;
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		int ok, i;
		cout << "Case #" << k << ": ";
		cin >> n >> l >> h;
		for (int i = 1; i <= n; ++i)
			cin >> A[i];

		ok = 0;
		for (i = l; i <= h && !ok; ++i)
		{
			ok = 1;
			for (int j = 1; j <= n && ok; ++j)
				if (i % A[j] && A[j] % i) ok = 0;
		}
		if (ok) cout << i - 1 << '\n';
		else cout << "NO\n";
	}

	return 0;
}
