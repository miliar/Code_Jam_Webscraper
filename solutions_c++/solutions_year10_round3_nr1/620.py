#include <iostream>
using namespace std;

int a[1111], b[1111];

int main()
{
	int n, i, t, j, is, k;

	cin >> t;
	for (i = 0; i < t; i++)
	{
		cin >> n;
		for (j = 0; j < n; j++)
		{
			cin >> a[j] >> b[j];
		}

		is = 0;
		for (j = 0; j < n; j++)
		{
			for (k = j+1; k < n; k++)
			{
				if (a[j] < a[k] && b[j] > b[k])
					is++;
				else if (a[j] > a[k] && b[j] < b[k])
					is++;
			}
		}

		cout << "Case #" << i+1 << ": " << is << endl;
	}

	return 0;
}
