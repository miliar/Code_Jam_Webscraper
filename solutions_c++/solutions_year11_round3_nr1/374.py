#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int n, m, i, j;
char a[100][100];

bool replace(int i, int j)
{
	a[i][j] = '/';
	if (j+1 < m && a[i][j+1] == '#')
		a[i][j+1] = '\\';
	else
		return false;
	if (i+1 < n)
	{
		if (a[i+1][j] == '#')
			a[i+1][j] = '\\';
		else
			return false;
		if (a[i+1][j+1] == '#')
			a[i+1][j+1] = '/';
		else return false;
	}else return false;
	return true;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int TT=1;TT<=T;++TT) {
		cin >> n >> m;

		for (i=0;i<n;++i)
			for (j=0;j<m;++j)
				scanf(" %c ", &a[i][j]);

		bool ok = true;

		for (i=0;i<n && ok; ++ i)
			for (j=0;j<m && ok; ++ j) 
				if (a[i][j] == '#')
					ok = replace(i, j);

		cout << "Case #" << TT << ":\n";
		if (!ok)
			cout << "Impossible" << endl;
		else
			for (i=0;i<n;++i)
			{
				for (j=0;j<m;++j)
					cout << a[i][j];
				cout << "\n";
			}
	}

	return 0;
}