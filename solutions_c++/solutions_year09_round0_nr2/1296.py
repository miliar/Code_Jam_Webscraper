using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector> 

int alt[105][105];
int mark[105][105];

int dr[4] = { -1,  0, 0, 1 }; // north, west, east, south
int dc[4] = {  0, -1, 1, 0 };
int lon[105][105][2];

int H, W;


void go(int r, int c, int cc)
{
	mark[r][c] = cc;
	for (int i = 0; i < 4; ++i)
	{
		int nr = r + dr[i];
		int nc = c + dc[i];
		if (nr < 0 || nc < 0 || nr == H || nc == W) continue;
		if (lon[nr][nc][0] == r && lon[nr][nc][1] == c)
			go(nr, nc, cc);
	}
}

int main()
{
	int t, i, j;
	freopen("f:/bin.txt", "r", stdin);
	freopen("f:/bo.txt", "w", stdout);
	
	cin >> t;
	for (int T = 1; T <= t; ++T)
	{
		cin >> H >> W;
		vector< pair<int, int> > sink;
		memset(alt, 0, sizeof alt);
		memset(mark, 0, sizeof mark);
		
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
				cin >> alt[i][j];
		
		memset(lon, -1, sizeof lon);
		
		for (i = 0; i < H; ++i)
		{
			for (j = 0; j < W; ++j)
			{
				int loa = 2000000, lo = 0, nxr, nxc;				
				for (int x = 0; x < 4; ++x)
				{
					int nr = i + dr[x];
					int nc = j + dc[x];
					
					if (nr < 0 || nc < 0 || nr == H || nc == W) continue;
			
					if (alt[nr][nc] < alt[i][j] && loa > alt[nr][nc]) 
					{
						loa = alt[nr][nc];
						nxr = nr;
						nxc = nc;
					}

					if (alt[nr][nc] < alt[i][j]) 
						lo = 1;

				}
				
				if (lo == 0)
					sink.push_back(make_pair(i, j));
				
				if (loa == 2000000) continue;
				lon[i][j][0] = nxr;
				lon[i][j][1] = nxc;				
			}

		}
		for (i = 0; i < sink.size(); ++i)
		{
			int R = sink[i].first;
			int C = sink[i].second;
			go(R, C, i+1);
			
		}

		char label[30];
		memset(label, 0, sizeof label);
		char x = 'a';
		for (i = 0; i < H; ++i)
		{
			for (j = 0; j < W; ++j)
			{
				if (label[mark[i][j]] == 0)
					label[mark[i][j]] = x++;
			}
		}



		cout << "Case #" << T << ":" << endl;
		
		for (i = 0; i < H; ++i)
		{
			for (j = 0; j < W; ++j)
			{
				if (j) cout << ' ';
				cout << label[mark[i][j]];
			}
			cout << endl;
		}
		
		
	}
	
}
