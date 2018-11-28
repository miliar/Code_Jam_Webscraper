#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t, cn, n, i, j, ans;
	vector<int> a, b;

	cin >> t;

	for (cn = 1; cn <= t; cn++)
	{
		ans = 0;
		cin >> n;

		a.resize(n);
		b.resize(n);

		for (i = 0; i < n; i++)
			cin >> a[i] >> b[i];

		for (i = 0; i < n; i++)
			for (j = 0; j < n; j++)
			{
				if (i == j)
					continue;

				if (a[i] == b[i])
					if (min(a[j], b[j]) < a[i] && max(a[j], b[j]) > a[i])
						ans++;

				if (a[i] < b[i])
					if (a[i] < a[j] && b[i] > b[j] || a[j] < a[i] && b[j] > b[i])
						ans++;

				if (a[i] > b[i])
					if (a[i] > a[j] && b[i] < b[j] || a[j] > a[i] && b[j] < b[i])
						ans++;
			}


		cout << "Case #" << cn << ": " << ans / 2 << endl;
	}

	return 0;
}
