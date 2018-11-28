#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int dx[4] = {0, -1, 1, 0};
const int dy[4] = {-1, 0, 0, 1};

int main()
{
	freopen("large.in",  "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int numCase = 0; numCase < T; numCase++)
	{
		int H, W;
		cin >> H >> W;
		vector< vector<int> > mp(H, vector<int>(W, 0) );

		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
				cin >> mp[i][j];

		vector< vector<int> > basin(H, vector<int>(W, 0) );
		int num = 0;

		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++)
			{
				bool isSink = true;
				for (int dir = 0; dir < 4; dir++)
					if (i + dy[dir] < H && i + dy[dir] > -1 &&  j + dx[dir] < W && j + dx[dir] > -1)
						if (mp[i][j] > mp[i + dy[dir]][j + dx[dir]])				
							isSink = false;

				if (!isSink) continue;
				
				queue< pair<int, int> > q;
				q.push( make_pair(i, j) );

				while (!q.empty() )
				{
					pair<int, int> cur = q.front();
					basin[cur.first][cur.second] = num;
					q.pop();

					for (int dir = 0; dir < 4; dir++)
					{
						int ii = cur.first + dy[dir];
						int jj = cur.second + dx[dir];
						if (ii < H && ii > -1 && jj < W && jj > -1)
						{
							bool isFlow = true;
							if (mp[cur.first][cur.second] >= mp[ii][jj]) isFlow = false;

							for (int d = 0; d < 4; d++)
							{
								int i1 = ii + dy[d];
								int j1 = jj + dx[d];
								if (i1 < H && i1 > -1 && j1 < W && j1 > -1)
									if (mp[i1][j1] <  mp[cur.first][cur.second] || 
										(d < 3 - dir && mp[i1][j1] ==  mp[cur.first][cur.second] ) )
										isFlow = false;
							}
							if (isFlow) q.push( make_pair(ii, jj) );
						}
					}
				}
				num++;
			}
			
				
		
		vector<char> letter(26, - 1);
		char curLetter = 'a'; 
		vector<string> ans(H, string(2 * W - 1, ' ') );
		for (int i = 0;i < H; i++)
			for (int j = 0; j < W; j++)
			{
				if (letter[ basin[i][j]] == -1)
				{
					letter[ basin[i][j]] = curLetter;
					curLetter++;
				}
				ans[i][2 * j] = letter[ basin[i][j]];
			}
		
		cout << "Case #" << numCase + 1 << ":" << endl;
		for (int i = 0;i < H; i++)
			cout << ans[i] << endl;

	}


	return 0;
}