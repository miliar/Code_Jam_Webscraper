#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> a, b;
	a.reserve(1024);
	b.reserve(1024);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testNum;
	cin >> testNum;

	for (int testId = 1; testId <= testNum; testId++)
	{
		int n;		
		cin >> n;

		a.resize(n);
		b.resize(n);

		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
		}

		for (int i = 0; i < n; i++)
		{
			cin >> b[i];
		}

		sort(a.begin(), a.end(), greater<int>());
		sort(b.begin(), b.end(), less<int>());

		long long res = 0;

		for (int i = 0; i < n; i++)
		{
			res += a[i] * b[i];
		}

		cout << "Case #" << testId << ": " << res << endl;
	}

	return 0;
}