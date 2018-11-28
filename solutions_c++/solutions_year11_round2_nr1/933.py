# include <iostream>
# include <stdio.h>
# include <string>

using namespace std;

const int NMAX = 100;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int n;
		cin >> n;
		string a[NMAX];
		for (int i = 0; i < n; ++i)
				cin >> a[i];

		double won[NMAX];
		double total[NMAX];
		double op[NMAX];
		double oop[NMAX];
		double rpi[NMAX];

		//WP
		for (int i = 0; i < n; ++i)
		{
			won[i] = 0;
			total[i]  = 0;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] == '1')
					++won[i];
				if (a[i][j] != '.')
					++total[i];
			}
		}
		
		//OP
		for (int i = 0; i < n; ++i)
		{
			op[i] = 0;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] != '.')
					op[i] += (won[j] - (a[i][j] == '0' ? 1 : 0)) / (total[j] - 1);
			}
			op[i] /= total[i];
		}

		//OOP
		for (int i = 0; i < n; ++i)
		{
			oop[i] = 0;
			for (int j = 0; j < n; ++j)
			{
				if (a[i][j] != '.')
					oop[i] += op[j];
			}
			oop[i] /= total[i];
		}

		cout << "Case #" << test << ":" << endl;
		for (int i = 0; i < n; ++i)
			printf("%0.9lf\n", .25 * (won[i] / total[i]) + .5 * op[i] + .25 * oop[i]);
	}

	return 0;
}