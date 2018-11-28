#include <iostream>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testn;
	cin >> testn;

	int g[1024];

	for (int testi = 1; testi <= testn; ++testi)
	{
		int r, k, n;
		cin >> r >> k >> n;

		for (int i = 0; i < n; ++i)
		{
			cin >> g[i];
		}

		int curg = 0;
		long long result = 0;

		for (int i = 0; i < r; ++i)
		{
			int prevg = curg;
			int sum = 0;

			if ((sum += g[curg]) <= k)
			{
				curg = (curg + 1) % n;

				while ((sum += g[curg]) <= k && curg != prevg)
				{
					curg = (curg + 1) % n;
				}
			}

			sum -= g[curg];
			result += sum;
		}

		cout << "Case #" << testi << ": " << result << endl;
	}

	return 0;
}