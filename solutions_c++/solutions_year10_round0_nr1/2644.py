#include <cassert>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

bool a[2][256];


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testn;
	cin >> testn;

	for (int testi = 1; testi <= testn; ++testi)
	{
		long long n, k;
		cin >> n >> k;

		bool res = true;

		for (int i = 0; i < n; ++i)
		{
			if ((k & (1 << i)) == 0)
			{
				res = false;
				break;
			}
		}

		cout << "Case #" << testi << ": " << (res ? "ON" : "OFF") << endl;
	}

	return 0;
}