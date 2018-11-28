#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int w, q;
char a[21][21];


void Load()
{
	cin >> w >> q;
	int i, j;
	for (i = 0; i < w; i++)
	{
	 	for (j = 0; j < w; j++)
	 		cin >> a[i][j];
	}
}


#define SHIFT (100)
#define MAX 300

int was[21][21][500];
string ans[21][21][500];


const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};


string nans[500];
int nwas[500];

void Solve()
{
	memset(was, 0, sizeof(was));
	int i, j, k, kk, ii, jj, d, dd, iii, jjj;
	string s;
	char c1, c2;
	int f = 1;

	for (i = 0; i < w; i++)
		for (j = 0; j < w; j++)
			if (a[i][j] != '-' && a[i][j] != '+')
			{
				was[i][j][(int)a[i][j]-'0'+SHIFT] = 1;
				ans[i][j][(int)a[i][j]-'0'+SHIFT] = a[i][j];

			}

	while (f)
	{
		f = 0;
		for (i = 0; i < w; i++)
		{
			for (j = 0; j < w; j++)
			{
				if (a[i][j] == '-' || a[i][j] == '+')
					continue;
				for (k = 0; k < MAX; k++)
				{
					if (was[i][j][k] == 0) continue;
					for (d = 0; d < 4; d++) for (dd = 0; dd < 4; dd++)
					{
						ii = i + dx[d];
						jj = j + dy[d];
						if (ii < 0 || jj < 0 || ii >= w || jj >= w) continue;
						iii = ii + dx[dd];
						jjj = jj + dy[dd];
						if (iii < 0 || jjj < 0 || iii >= w || jjj >= w) continue;

						c1 = a[ii][jj];
						c2 = a[iii][jjj];
						if (c1 == '-')
							kk = k - ((int)c2 -'0');
						else kk = k + ((int)c2-'0');
						if (kk < 0 || kk >= MAX) continue;
						s = (ans[i][j][k] + c1) + c2;
						if (was[iii][jjj][kk] == 0 || ans[iii][jjj][kk].size() > s.size() || (ans[iii][jjj][kk].size() == s.size() && ans[iii][jjj][kk] > s))
						{
							ans[iii][jjj][kk] = s;
//							cerr << s << "\n";
							f = 1;
							was[iii][jjj][kk] = 1;
						}
					}
				}
			}
		}
	}

	memset(nwas, 0, sizeof(nwas));

	for (i = 0; i < w; i++)
	{
		for (j = 0; j < w; j++)
		{
			if (a[i][j] == '-' || a[i][j] == '+')
				continue;
			for (k = 0; k < MAX; k++)
			{
				if (was[i][j][k] == 0) continue;
				if (nwas[k] == 0 || nans[k].size() > ans[i][j][k].size() || ( nans[k].size() == ans[i][j][k].size() && nans[k] > ans[i][j][k]))
				{
					nans[k] = ans[i][j][k];
					nwas[k] = 1;
				}
    		}
		}
	}

	for (i = 0; i < q; i++)
	{
		cin >> j;
		cout << nans[j+SHIFT] << "\n";
	}

}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ":\n";
		Solve();
	}
	return 0;
}
