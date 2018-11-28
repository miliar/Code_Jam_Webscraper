#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int m, n, r;
		cin >> m >> n >> r;
		VVI a(m+2, VI(n+2, 0));
		a[0][0] = 1;
		for (int i=0; i<r; i++)
		{
			int y, x;
			cin >> y >> x;
			a[y-1][x-1] = -1;
		}
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++)
				if (a[i][j] > 0)
				{
					a[i][j] = a[i][j] % 10007;
					if (a[i+2][j+1] >= 0)
					{
						a[i+2][j+1] += a[i][j];
					}
					if (a[i+1][j+2] >= 0)
					{
						a[i+1][j+2] += a[i][j];
					}
				}
		cout << "Case #" << kase << ": " << a[m-1][n-1] << endl;
	}
	return 0;
}
