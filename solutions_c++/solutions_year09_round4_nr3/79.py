#include <iostream>
#include <fstream>
#include <string>
#define MAX 17
using namespace std;

ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

#define cin fin
#define cout fout

int ans;
int n, k;
int data[MAX][25];
int map[MAX][MAX];
int color[MAX];

bool cross(int a, int b)
{
	bool ok = true;
	for (int i = 0; i < k-1; i++)
	{
		if (!(data[a][i] > data[b][i] && data[a][i+1] > data[b][i+1]))
		{
			ok = false;
			break;
		}
	}

	if (ok == true) return false;

	ok = true;
	for (int i = 0; i < k-1; i++)
	{
		if (!(data[a][i] < data[b][i] && data[a][i+1] < data[b][i+1]))
		{
			ok = false;
			break;
		}
	}

	if (ok == true) return false;

	return true;
}

void dfs(int now, int cost)
{
	if (cost > ans) return;
	if (now >= n)
	{
		ans = cost;
		return;
	}

	int canuse[MAX];
	memset(canuse, 0, sizeof(canuse));

	for (int i = 0; i < now; i++)
		if (map[i][now] == 1) canuse[color[i]] = 1;

	for (int i = 0; i <= cost; i++)
		if (canuse[i] == 0) 
		{
			color[now] = i;
			dfs(now+1, cost);
		}

	color[now] = cost+1;
	dfs(now+1, cost+1);
}

int main()
{
	int cases;

	cin >> cases;
	for (int i = 1; i <= cases; i++)
	{
		cin >> n >> k;
		for (int j = 0; j < n; j++)
			for (int h = 0; h < k; h++)
				cin >> data[j][h];

		memset(map, 0, sizeof(map));
		for (int j = 0; j < n; j++)
			for (int h = j+1; h < n; h++)
				if (cross(j,h)) map[j][h] = map[h][j] = 1;

		ans = MAX;
		color[0] = 0;
		dfs(1, 0);

		cout << "Case #" << i << ": " << ans+1 << endl;
	}

	return 0;
}

