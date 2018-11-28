#include <iostream>
#include <fstream>
#include <vector>

using namespace std;





int f[300][300];


void Load()
{
	int n;
	memset(f,0,sizeof(f));
	cin >> n;
	int i;
	for (i = 0; i < n; i++)
	{
		int a, b, c, d, q, p;
		cin >> a >> c >> b >> d;		
		for (p = a; p <= b; p++)
			for (q = c; q <= d; q++)
				f[p][q] = 1;
	}

/*	for (int ii = 0; ii < 10; ii++)
	{
		for (int jj = 0; jj < 10; jj++)
			cerr << f[ii][jj];
		cerr << "\n";	
	}
	cerr << "\n";
*/
}

void Solve()
{
	int turn = 0;
	int was = true;
	int i, j;
	while (was)
	{	



		was = false;
		for (i = 1; i <= 150; i++)
			for (j = 1; j <= 150; j++)
			{
				if (f[i-1][j] == 0 && f[i][j-1] == 0 && f[i][j] == 1) f[i][j] = 2;
			}

		for (i = 150; i > 0; i--)
			for (j = 150; j > 0; j--)
			{
				if (f[i-1][j] != 0 && f[i][j-1] != 0 && f[i][j] == 0) f[i][j] = 1;
			}

		for (i = 150; i > 0; i--)
			for (j = 150; j > 0; j--)
			{
				if (f[i][j] == 2) f[i][j] = 0;
				if (f[i][j] == 1) was = true;
			}

	   turn++;
	}
	cout << turn << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
