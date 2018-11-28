#include <iostream>
using namespace std;

int main()
{
	unsigned long t, n, k, r, i, j, a, b, hold, euro, g[1002];

	cin >> t;

	for (i = 0; i < t; i++)
	{
		cin >> r >> k >> n;

		for (j = 0; j < n; j++)
			cin >> g[j];

		euro = 0;
		a = 0;
		for (j = 0; j < r; j++)
		{
			b = hold = 0;

			while(true)
			{
				if (hold + g[a] > k)
					break;

				hold += g[a];
				a = (a+1) % n;
				b++;

				if (b == n)
					break;
			}

			euro += hold;
		}

		cout << "Case #" << i+1 << ": " << euro << endl;
	}

	return 0;
}
