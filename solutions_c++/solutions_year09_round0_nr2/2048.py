#include <iostream>
#include <memory.h>
#include <numeric>
#include <utility>
#include <vector>

using namespace std;

int n, w, h;
int map[200][200];
char was[200][200];
vector< pair<int, int> > edge[200][200];

void visit(int r, int c)
{
	int m = 21000;
	bool f = false;
	int i, j, minc, minr;
	
	was[r][c] = 1;
	for (i = -1; i <= 1; i++)
		for (j = -1; j <= 1; j++) 
			if ((i != 0 || j != 0) && (i == 0 || j == 0))
			{
				int nr = r + i;
				int nc = c + j;
				if (nr >= 0 && nc >= 0 && nr < h && nc < w && map[nr][nc] < m)
				{
					m = map[nr][nc];
					minr = nr;
					minc = nc;
					f = true;
				}
			}
	if (f && m < map[r][c])
	{
		edge[r][c].push_back(make_pair(minr, minc));
		edge[minr][minc].push_back(make_pair(r, c));
//		cout << r << " " << c << " " << minr << " " << minc << endl;
		visit(minr, minc);
	}
}

void visit2(int r, int c, char l)
{
	was[r][c] = l;
	for (int i = 0; i < edge[r][c].size(); i++)
	{
		pair<int, int> dest = edge[r][c][i];
		if (was[dest.first][dest.second] == 0)
			visit2(dest.first, dest.second, l);
	}
}

int main()
{
	int i, j, k;
	char letter = 'a';
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> n;
	for (i = 0; i < n; i++)
	{
		cin >> h >> w;
		memset(map, 255, sizeof(map));
						
		for (j = 0; j < h; j++)
			for (k = 0; k < w; k++) 
			{
				cin >> map[j][k];
				edge[j][k].clear();
			}
				
		memset(was, 0, sizeof(was));
		for (j = 0; j < h; j++)
			for (k = 0; k < w; k++)
				if (was[j][k] == 0) 
				{
					visit(j, k);
				}

		memset(was, 0, sizeof(was));
		letter = 'a';
		for (j = 0; j < h; j++)
			for (k = 0; k < w; k++)
				if (was[j][k] == 0)
				{
					//cout << "visit:" << j << " " << k << endl;
					visit2(j, k, letter);				
					letter++;
				}
		cout << "Case #" << i + 1 << ":" << endl;
		for (j = 0; j < h; j++) 
		{
			for (k = 0; k < w; k++)
				cout << (char)was[j][k] << " ";
			cout << endl;
		}
	}		
	return 0;
}
