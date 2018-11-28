#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int t, r, k, n, i, j, cn;
	long long ans;
	vector<int> inp;
	vector<pair<int, int> > arr;

	cin >> t;

	for (cn = 1; cn <= t; cn++)
	{
		cin >> r >> k >> n;
		
		ans = 0;
		inp.resize(n);
		arr.assign(n, pair<int, int>());

		for (i = 0; i < n; i++)
			cin >> inp[i];

		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n && arr[i].first + inp[(i + j) % n] <= k; j++)
				arr[i].first += inp[(i + j) % n];
			arr[i].second = (i + j) % n;
		}

		j = 0;
		for (i = 0; i < r; i++)
		{
			ans += arr[j].first;
			j = arr[j].second;
		}

		cout << "Case #" << cn << ": " << ans << endl;
	}

	return 0;
}
