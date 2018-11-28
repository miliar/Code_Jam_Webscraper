#include <iostream>

using namespace std;

char A[60][60];

int main()
{
	int n, m, t;

	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		cin >> n >> m;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= m; ++j)
				cin >> A[i][j];

		for (int i = 1; i < n; ++i)
			for (int j = 1; j < m; ++j)
				if (A[i][j] == '#' && A[i + 1][j] == '#' && A[i][j + 1] == '#' && A[i + 1][j + 1] == '#')
				{
					A[i][j] = '/';
					A[i + 1][j] = '\\';
					A[i][j + 1] = '\\';
					A[i + 1][j + 1] = '/';
				}
		int ok = 1;
		for (int i = 1; i <= n && ok; ++i)
			for (int j = 1; j <= m && ok; ++j)
				if (A[i][j] == '#') ok = 0;
		cout << "Case #" << k << ":\n";
		if (ok)
			for (int i = 1; i <= n; ++i, cout << '\n')
				for (int j = 1; j <= m; ++j)
					cout << A[i][j];
		else
			cout << "Impossible\n";

	}

	return 0;
}
