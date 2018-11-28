#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

void output(int value)
{
	static int count = 0;
	cout << "Case #" << ++count << ": " << value << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int n;
		cin >> n;

		vector<int> v1(n), v2(n);
		for (int j = 0; j < n; ++j)
			cin >> v1[j];
		for (int j = 0; j < n; ++j)
			cin >> v2[j];

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());

		long long product = 0;
		for (int j = 0; j < n; ++j)
			product += v1[j] * v2[n - j - 1];

		output(product);
	}

	return 0;
}
