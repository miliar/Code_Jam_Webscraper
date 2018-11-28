#include <iostream>
#include <string>
#include <vector>
#include <queue>

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define pb push_back
#define mp make_pair
using namespace std;

const int di[] = {-1, 0, 0, 1};
const int dj[] = { 0, -1, 1, 0};

int t, w, h, alt[101][101];
vector<pair<int, int>> m[101][101];
char us[101][101];

void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(int it = 1; it <= t; ++it)
	{
		scanf("%d %d", &h, &w);
		forn(i, h)
			forn(j, w)
				scanf("%d", &alt[i][j]);
		forn(i, h)
			forn(j, w)
			{
				int bestIdx = -1, maxDif = -1000000;
				forn(idx, 4)
				{	
					int x = i + di[idx];
					int y = j + dj[idx];
					if(0 <= x && x < h && 0 <= y && y < w && alt[i][j] > alt[x][y])
					{
						if(maxDif < alt[i][j] - alt[x][y])
						{
							maxDif = alt[i][j] - alt[x][y];
							bestIdx = idx;
						}
					}
				}
				if(bestIdx != -1)
				{
					int x = i + di[bestIdx], y = j + dj[bestIdx];
					m[i][j].pb(mp(x, y));
					m[x][y].pb(mp(i, j));
				}
		}
		
		memset(us, 0, sizeof us);
		char letter = 'a';
		forn(i, h)
			forn(j, w)
				if(!us[i][j])
				{
					us[i][j] = letter;
					queue<pair<int, int>> q;
					q.push(mp(i, j));
					while(!q.empty())
					{
						pair<int, int> nx = q.front();
						q.pop();
						forn(id, m[nx.first][nx.second].size())
						{
							pair<int, int> vx = m[nx.first][nx.second][id];
							if(!us[vx.first][vx.second])
							{
								q.push(vx);
								us[vx.first][vx.second] = letter;
							}
						}
					}
					++letter;
				}

		printf("Case #%d:\n", it);
		forn(i, h)
		{
			forn(j, w)
				printf("%c ", us[i][j]);
			printf("\n");
		}
		
		forn(i, h)
			forn(j, w)
				m[i][j].clear();

	}
}