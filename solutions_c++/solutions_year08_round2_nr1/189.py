#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <cstdio>



using namespace std;


int n;

long long p[3][3];


void Load()
{
	cin >> n;
	long long a, b, c, d, x0, y0, m;
	cin >> a >> b >> c >> d >> x0 >> y0 >> m;
	long long x, y;
	x = x0; y = y0;
	memset(p, 0, sizeof(p));
	p[x0%3][y0%3]++;
	for (int i = 0; i < n-1; i++)
	{
		x = (a*x + b) % m;
		y = (c*y + d) % m;
		p[x%3][y%3]++;
	}
	for (int j = 0; j < 3; j++) cerr << p[j][0] << ' ' << p[j][1] << ' ' << p[j][2] << '\n';

}


void Solve()
{
	long long ans = 0, cur;
	int i1, i2, i3, j1, j2, j3;
	cur = 0;
	for (i1 = 0; i1 < 3; i1++)
	{
		for (j1 = 0; j1 < 3; j1++)
		{
			for (i2 = 0; i2 < 3; i2++)
			{
				for (j2 = 0; j2 < 3; j2++)
				{
					if (i2 == i1 && j2 == j1) continue;
					for (i3 = 0; i3 < 3; i3++)
					{
						for (j3 = 0; j3 < 3; j3++)
						{
							if (i3 == i1 && j3 == j1) continue;
							if (i2 == i3 && j2 == j3) continue;
							if ((i1 + i2 + i3) % 3 == 0 && (j1 + j2 + j3) % 3 == 0)
								cur +=  p[i1][j1] * p[i2][j2] * p[i3][j3];
						}
					}
				}
			}
		}
	}

	ans += cur / 6;

	cerr << "* " << ans << "\n";

	cur = 0;
	for (i1 = 0; i1 < 3; i1++)
		for (j1 = 0; j1 < 3; j1++)
			cur += p[i1][j1] * (p[i1][j1] - 1) * (p[i1][j1]-2) / 6;
	ans += cur;
	
	cerr << "^ " << cur << "\n";
	
	cur = 0;
	for (i1 = 0; i1 < 3; i1++)
	{
		for (j1 = 0; j1 < 3; j1++)
		{
			for (i2 = 0; i2 < 3; i2++)
			{
				for (j2 = 0; j2 < 3; j2++)
				{
					if (i2 == i1 && j2 == j1) continue;
					if ((i1 + i1 + i2) % 3 == 0 && (j1 + j1 + j2) % 3 == 0)
					{
						cur += (p[i1][j1] * (p[i1][j1] - 1) * p[i2][j2]) / 2;
					}
				}
			}
		}
	}	
	ans += cur;

	cerr << "# " << cur << "\n";


	cout << ans;
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int nt, tt;

	cin >> nt;

	for (tt = 1; tt <= nt; tt++)
	{
    	Load();
    	cout << "Case #" << tt << ": ";
    	Solve();
    	cout << "\n";
    }
	return 0;
}