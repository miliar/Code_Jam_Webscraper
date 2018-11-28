#include <iostream>
#include <fstream>
#include <vector>

using namespace std;




int n, k;
int pr[111][111];
int gr[111][111];


void Load()
{
	cin >> n >> k;
	int i, j;
	for (i = 0; i < n; i++)
		for (j = 0; j < k; j++)
			cin >> pr[i][j];
}




int a[111][111];
int was[111];
int w[111];


int dfs(int v)
{
	was[v] = 1;
	int i;
	for (i = 0; i < n; i++)
	{
		if (a[v][i] == 0) continue;
		if (w[i] == -1)
		{
			w[i] = v;
			return 1;
		}
		else if (was[w[i]] == 0)
		{
			if (dfs(w[i]))
			{
				w[i] = v;
				return 1;
			}
		}
	}
	return 0;
}





void Solve()
{
	int i, j, q;
	memset(gr, 0, sizeof(gr));
	memset(a, 0, sizeof(a));
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			for (q = 0; q < k; q++)
			{
				if (pr[i][q] <= pr[j][q])
				{
					gr[i][j] = 1;
				}
			}
		}
	}

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			if (gr[i][j] == 1 && gr[j][i] == 0)
			{
				a[i][j] = 1;	
			}
		}
	}
	memset(w, -1, sizeof(w));
	int ans = 0;
	for (i = 0; i < n; i++)
	{
		memset(was, 0, sizeof(was));
		if (dfs(i))
			ans++;
	}

	cout << n - ans << "\n";

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
