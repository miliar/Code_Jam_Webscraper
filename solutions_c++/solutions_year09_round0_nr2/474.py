#include <iostream>
#include <vector>

using namespace std;

const int MAXALT = 10000;
const int dy[] = {-1, 0, 0, 1};
const int dx[] = {0, -1, 1, 0};

vector<vector<int> > map;
vector<vector<char> > ans;
char cb;

int SinkDir(const int &y, const int &x)
{
	char ans = -1;
	int mh = map[y][x];

	if (mh > MAXALT)
		return ans;

	for (int i = 0; i < 4; i++)
		if (map[y + dy[i]][x + dx[i]] < mh)
		{
			mh = map[y + dy[i]][x + dx[i]];
			ans = i;
		}

	return ans;
}

void DFS(const int &y, const int &x)
{
	if (ans[y][x])
		return;

	int d = SinkDir(y, x);
	if (d < 0)
	{
		ans[y][x] = cb;
		cb++;
		return;
	}

	DFS(y + dy[d], x + dx[d]);
	ans[y][x] = ans[y + dy[d]][x + dx[d]];
}

int main()
{
	int t, h, w, i, j, cn;

	cin >> t;

	for (cn = 1; cn <= t; cn++)
	{
		cb = 'a';

		cin >> h >> w;
		
		map.resize(h + 2);
		for (i = 0; i < h + 2; i++)
			map[i].assign(w + 2, MAXALT + 1);

		ans.resize(h + 2);
		for (i = 0; i < h + 2; i++)
			ans[i].assign(w + 2, 0);

		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
				cin >> map[i + 1][j + 1];

		for (i = 0; i < h; i++)
			for (j = 0; j < w; j++)
				DFS(i + 1, j + 1);

		cout << "Case #" << cn << ":\n";
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
				cout << ans[i + 1][j + 1] << ' ';
			cout << endl;
		}
	}

	return 0;
}
