#include <fstream>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
 
#define X first
#define Y second

bool found;
vector<bool> used;
vector<vector<int> > g;

void dfs(int v)
{
	if (!found)
	{
		used[v] = true;

		int n = g[v].size();
		for (int i = 0; i < n; i++)
		{
			if (!used[g[v][i]])
			{
				dfs(g[v][i]);
			}
			else
			{
				found = true;
			}
		}
	}
}
 
int main()
{
		//freopen("output.txt", "w", stdout);
        ifstream cin("input.txt");
		ofstream cout("output.txt");

		int T;
		cin >> T;
		for (int tc = 0; tc < T; tc++)
		{ 
			int n, m;
			cin >> n;

			g.resize(n);
			for (int i = 0; i < n; i++)
			{
				cin >> m;
				g[i].resize(m);
				for (int j = 0; j < m; j++)
				{
					cin >> g[i][j];
					g[i][j]--;
				}
			}

			found = false;
			for (int i = 0; i < n && !found; i++)
			{
				used.assign(n, false);
				dfs(i);

				if (found)
				{
					cout << "Case #" << tc + 1 << ": Yes" << endl;
				}
			}

			if (!found)
			{
				cout << "Case #" << tc + 1 << ": No" << endl;
			}
		}
 
        return 0;
}
