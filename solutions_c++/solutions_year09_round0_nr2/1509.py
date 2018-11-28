#include <fstream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

const int step[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		int n, m;
		ifs >> n >> m;
		vector<vector<int> > a(n, vector<int>(m, 0));
		vector<vector<int> > v = a;
		for (int i =0; i < n; ++i)
			for(int j= 0; j < m; ++j)
				ifs >> a[i][j];
		for (int i =0; i < n; ++i)
			for (int j = 0; j< m; ++j)
			{
				int d = -1, best = 100000;
				for (int k = 0; k < 4; ++k)
				{
					int nx = i + step[k][0];
					int ny = j + step[k][1];
					if (nx >= 0 && ny >= 0 && nx < n && ny < m)
					{
						if (a[nx][ny] < a[i][j] && a[nx][ny] < best)
						{
							best = a[nx][ny];
							d = k;
						}
					}
				}
				v[i][j] = d;
			}
		vector<vector<int> > was(n, vector<int>(m, 0));
		int cnt = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (v[i][j] == -1)
				{
					++cnt;
					queue<pair<int,int> > q;
					q.push(make_pair(i, j));
					was[i][j] = cnt;
					while (!q.empty())
					{
						int x = q.front().first;
						int y = q.front().second;
						q.pop();
						for (int k = 0; k < 4; ++k)
						{
							int nx = x + step[k][0];
							int ny = y + step[k][1];
							if (nx >= 0 && ny >= 0 && nx < n && ny < m && v[nx][ny] != -1 && was[nx][ny] == 0)
							{
								int d = v[nx][ny];
								int xx = nx + step[d][0];
								int yy = ny + step[d][1];
								if (xx == x && yy == y)
								{
									was[nx][ny] = cnt;
									q.push(make_pair(nx, ny));
								}
							}
						}
					}
				}
		ofs << "Case #" << test+1 << ":\n";
		vector<int> lbl(cnt+1, -1); 	
		char ch = 'a';
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (j > 0) ofs << ' ';
				if (lbl[was[i][j]] == -1)
				{
					lbl[was[i][j]] = ch;
					++ch;
				}
				ofs << char(lbl[was[i][j]]);
			}
			ofs << endl;
		}
	}
	return 0;
}
