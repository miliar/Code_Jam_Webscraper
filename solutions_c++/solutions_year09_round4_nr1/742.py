#include <stdio.h>
#include <vector>

using namespace std;

int t, n;
vector< vector<char> > matrix;
vector<int> indexes;
vector<int> dists;
vector<bool> used;
char c;
int rez;
int val;

int Find(int num)
{
	int m = -1;
	for (int i = 0; i < n; i++)
		if (matrix[num][i] == '1')
			m = max(m, i);
	return m;
}

int main()
{
	freopen("asmall.in", "r", stdin);
	freopen("asmall.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		matrix.clear();
		scanf("%d\n", &n);
		matrix.resize(n);
		for (int j = 0; j < n; j++)
		{
			matrix[j].resize(n);
			for (int u = 0; u < n; u++)
				scanf("%c", &matrix[j][u]);
			scanf("%c", &c);
		}

		rez = 0;
		
		indexes.clear();
		indexes.resize(n);
		for (int i = 0; i < n; i++)
			indexes[i] = Find(i);

		used.clear();
		used.resize(n, false);
		dists.clear();
		dists.resize(n, -1);

		for (int j = 0; j < n; j++)
		{
			//if (indexes[j] > j)
			{
				for (int u = max(indexes[j], 0); u < n; u++)
				{
					if (!used[u])
					{
						used[u] = true;
						dists[j] = u;
						break;
					}
				}
			}
		}

		for (int j = n - 1; j >= 0; j--)
		{
			if (dists[j] == -1)
				continue;

			val = -1;
			int tmp = 0;
			int dir = 1;
			int mn = n + 1, mx = -1;

			for (int u = 0; u < n; u++)
				if (dists[u] != u)
				{
					if (dists[u] < mn)
					{
						mn = dists[u];
						val = u;
					}
					if (dists[u] > mx)
					{
						mx = dists[u];
						val = u;
					}
				}
			if (val == -1)
				break;

			while(dists[val] != val)
			{
				if (dists[val] < val)
					dir = -1;
				else
					dir = 1;
				tmp = dists[val];
				dists[val] = dists[val + dir];
				dists[val + dir] = tmp;
				val += dir;
				rez++;
			}
		}
		

		printf("Case #%d: %d\n", i + 1, rez);
	}
	return 0;
}