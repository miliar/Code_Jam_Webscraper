#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 50 + 5;
char m[MAXN][MAXN];

int main()
{
	int t;
	cin >> t;
	for(int T=1; T<=t; T++)
	{
		memset(m, 0, sizeof m);
		int r, c;
		cin >> r >> c;
		for(int i=1; i<=r; i++)
			for(int j=1; j<=c; j++)
				cin >> m[i][j];
		bool ok = true;
		for(int i=1; i<=r; i++)
			for(int j=1; j<=c; j++)
				if(m[i][j] == '#')
				{
					if(m[i+1][j] != '#' || m[i][j+1] != '#' || m[i+1][j+1] != '#')
						ok = false;
					m[i][j] = '/';
					m[i+1][j] = '\\';
					m[i][j+1] = '\\';
					m[i+1][j+1] = '/';
				}

		cout << "Case #" << T << ": " << endl;
		if(!ok)
			cout << "Impossible" << endl;
		else
		{
			for(int i=1; i<=r; i++)
			{
				for(int j=1; j<=c; j++)
					cout << m[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}

