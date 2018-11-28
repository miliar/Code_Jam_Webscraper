#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int neigh[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

int main()
{
	freopen("watersheds.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;

	for (int ti = 0; ti < t; ti++)
	{
		int h, w;
		cin >> h >> w;

		vector< vector<int> > a(h, vector<int>(w, 0));

		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				cin >> a[i][j];
			}
		}

		vector< vector<int> > c(h, vector<int>(w, 0));
		queue< pair<int, int> > q;

		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				for (int k = 0; k < 4; k++)
				{
					int ny = i + neigh[k][0];
					int nx = j + neigh[k][1];
					if (ny >= 0 && ny < h && nx >= 0 && nx < w)
					{
						if (a[ny][nx] < a[i][j])
							c[i][j]++;
					}
				}
				if (c[i][j] == 0)
				{
					q.push(make_pair(i, j));
				}
			}
		}
		
		
		int sinks = 0;
		vector< vector<int> > s(h, vector<int>(w, -1));

		while (q.size() > 0)
		{
			int vy = q.front().first;
			int vx = q.front().second;
			q.pop();

			int value = a[vy][vx];
			for (int k = 0; k < 4; k++)
			{
				int ny = vy + neigh[k][0];
				int nx = vx + neigh[k][1];
				if (ny >= 0 && ny < h && nx >= 0 && nx < w)
				{
					if (a[ny][nx] < value)
					{
						value = a[ny][nx];
						s[vy][vx] = s[ny][nx];
					}

					if (a[ny][nx] > a[vy][vx])
					{
						c[ny][nx]--;
						if (c[ny][nx] == 0)
							q.push(make_pair(ny, nx));
					}
				}
			}
			if (value == a[vy][vx])
				s[vy][vx] = sinks++;
		}

		cout << "Case #" << ti + 1 << ":" << endl;
		char nextLabel = 'a';
		vector<char> sinkLabel(sinks, 0);
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w; j++)
			{
				if (sinkLabel[s[i][j]] == 0)
				{
					sinkLabel[s[i][j]] = nextLabel;
					nextLabel++;
				}
				
				if (j > 0) cout << " ";
				cout << sinkLabel[s[i][j]];
			}
			cout << endl;
		}
	}

	return 0;
}
