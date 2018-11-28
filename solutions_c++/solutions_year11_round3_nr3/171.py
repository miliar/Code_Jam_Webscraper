#include <iostream>

using namespace std;

int t,n,m,M;

int mas[1000];

int main()
{
	freopen("C31.in", "rt", stdin);
	freopen("C31.out", "wt", stdout);

	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		cin >> n >> m >> M;

		for (int j = 0; j < n; j++)
		{
			cin >> mas[j];
		}

		int lab;
		int rez = -1;

		for (int j = m; j <= M; j++)
		{
			lab = 1;

			for (int k = 0; k < n && lab; k++)
			{
				if ((mas[k] % j > 0) && (j % mas[k] > 0))
				{
					lab = 0;
				}
			}

			if (lab)
			{
				rez = j;
				break;
			}
		}

		cout << "Case #" << i << ": ";

		if (rez == -1)
		{
			cout << "NO" << endl;
		}
		else
		{
			cout << rez << endl;
		}
	}

	return 0;
}