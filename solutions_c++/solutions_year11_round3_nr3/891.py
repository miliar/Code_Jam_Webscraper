#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int i, t, n, low, high;

	cin >> t;
	for (i = 0; i < t; i++)
	{
		cin >> n >> low >> high;
		vector<int> vi(n);
		for (int j = 0; j < n; j++)
		{
			cin >> vi[j];
		}

		int k = low;
		for (; k <= high; k++)
		{
			int j = 0;
			for (; j < n; j++)
			{
				if ((k % vi[j]) == 0 || (vi[j] % k) == 0)
					continue;
				break;
			}

			if (j == n)
				break;
		}

		cout << "Case #" << i+1 << ": ";
		if (k <= high) cout << k << endl;
		else cout << "NO\n";
	}

	return 0;
}
