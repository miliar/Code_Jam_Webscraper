#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

ifstream fin;
ofstream fout;

const int MAXN = 17;
const int MAXT = 1024;

int id [MAXN][MAXN][4];
int dist [MAXN][MAXN][MAXT][MAXT];

struct rec 
{
	 int x, y, p1, p2;
	 rec (){}
	 rec (int x, int y, int p1, int p2)
	 {
		 this->x = x;
		 this->y = y;
		 this->p1 = p1;
		 this->p2 = p2;

		 if (x == 0 || y == 0)
		 {
			int t = 0;
		 }
	 }
};

rec pos [MAXN * MAXN * 4];

int dx [] = {0, 1, 0, -1};
int dy [] = {-1, 0, 1, 0};

int getr (int dir)
{
	if (dir == 0) return 2; 
	if (dir == 1) return 3; 
	if (dir == 2) return 0; 
	if (dir == 3) return 1; 
}

int main (int argc, char * argv [])
{

	if (argc  == 1)
	{
		fin.open("input.txt");
		fout.open("output.txt");
	}
	else
	{
		fin.open(argv[1]);
		fout.open(argv[2]);
	}

	int tests = 0;
	fin >> tests;

	while (tests -- > 0)
	{
		
		int n, m;
		char a[24][24];
		
		fin >> n >> m;

		for (int i = 0; i < n; ++ i)
		{
			string s;
			fin >> s;
			s = '#' + s + '#';
			strcpy(a[i + 1], s.c_str());
		}
		string s = "";
		for (int i = 0; i < m + 2; ++ i) s += '#';
		strcpy(a[0], s.c_str());
		strcpy(a[n + 1], s.c_str());

		memset (id, 0xff, sizeof (id));

		int num = 1;
		int x1, y1, x2, y2;
		for (int i = 1; i <= n; ++ i)
			for (int j = 1; j <= m; ++ j)
				if (a[i][j] != '#')
				{
					if (a[i][j] == 'X') x2 = i, y2 = j;
					if (a[i][j] == 'O') x1 = i, y1 = j;
				
					int x, y;

					for (int p = 0; p < 4; ++ p)
					{
						x = i;
						y = j;
						while (a[x][y] != '#')
						{
							x += dx [p];
							y += dy [p];

							if (a[x][y] == '#')
							{
								if (id [x][y][p] == -1)
								{
									id[x][y][p] = num;
									pos[num].x = x;
									pos[num].y = y;
									pos[num].p1 = p;
									++ num;
								}
								break;
							}
						}
					}
				}

		if (num >= MAXN * MAXN * 4)
		{
			cout << 'e' << endl; 
		}

		for (int i = 0; i <= n + 1; ++ i)
			for (int j = 0; j <= m + 1; ++ j)
				for (int x = 0; x <= num; ++ x)
					for (int y = 0; y <= num; ++ y) dist [i][j][x][y] = 1000000000;

		dist [x1][y1][0][0] = 0;

		vector <rec> que [2];
		int curr = 0;
		que[curr].push_back(rec(x1, y1, 0, 0));

		int res = 1000000000;
		int step = 0;
		while (true)
		{
			++ step;
			if (que[0].size() + que[1].size() == 0) break;

			int cnt = que[curr].size();
			que[1 - curr].clear();

			int xx, yy;
			rec newpos;
			for (int i = 0; i < cnt; ++ i)
			{
				rec pos = que[curr][i];

				for (int dir = 0; dir < 4; ++ dir)
					if (a[pos.x + dx[dir]][pos.y + dy [dir]] != '#')
					{
						xx = pos.x + dx [dir];	
						yy = pos.y + dy [dir];	
					
						if (dist[xx][yy][pos.p1][pos.p2] > dist [pos.x][pos.y][pos.p1][pos.p2] + 1)
						{
							dist[xx][yy][pos.p1][pos.p2] = dist [pos.x][pos.y][pos.p1][pos.p2] + 1;
							if (xx == x2 && yy == y2)
							{
								res = min (res, dist[xx][yy][pos.p1][pos.p2]);
							}
							if (dist[xx][yy][pos.p1][pos.p2] < res) 
								que[1 - curr].push_back (rec(xx, yy, pos.p1, pos.p2));
						}
					}
					else if (id [pos.x + dx[dir]][pos.y + dy[dir]][dir] == pos.p1 && pos.p2 != 0)
					{
						xx = ::pos[pos.p2].x;
						yy = ::pos[pos.p2].y;
						xx  -= dx [::pos[pos.p2].p1];
						yy  -= dy [::pos[pos.p2].p1];

						if (dist[xx][yy][pos.p1][pos.p2] > dist [pos.x][pos.y][pos.p1][pos.p2] + 1)
						{
							dist[xx][yy][pos.p1][pos.p2] = dist [pos.x][pos.y][pos.p1][pos.p2] + 1;
							if (xx == x2 && yy == y2)
							{
								res = min (res, dist[xx][yy][pos.p1][pos.p2]);
							}
							if (dist[xx][yy][pos.p1][pos.p2] < res) 
								que[1 - curr].push_back (rec(xx, yy, pos.p1, pos.p2));
						}					

					}

				for (int dir = 0; dir < 4; ++ dir)
				{
					xx = pos.x;
					yy = pos.y;

					while (a[xx][yy] != '#')
					{
						xx += dx [dir];
						yy += dy [dir];
					}

					int num = id[xx][yy][dir];

					if (num != pos.p2 && (pos.p1 == 0 || pos.p2 != 0))
					if (dist[pos.x][pos.y][num][pos.p2] > dist [pos.x][pos.y][pos.p1][pos.p2])
					{
						dist[pos.x][pos.y][num][pos.p2] = dist [pos.x][pos.y][pos.p1][pos.p2];
						if (dist[pos.x][pos.y][num][pos.p2] < res) 
							que[1 - curr].push_back (rec(pos.x, pos.y, num, pos.p2));
					}
					if (num != pos.p1 && (pos.p2 == 0 || pos.p1 != 0))
					if (dist[pos.x][pos.y][pos.p1][num] > dist [pos.x][pos.y][pos.p1][pos.p2])
					{
						dist[pos.x][pos.y][pos.p1][num] = dist [pos.x][pos.y][pos.p1][pos.p2];
						if (dist[pos.x][pos.y][pos.p1][num] < res) 
							que[1 - curr].push_back (rec(pos.x, pos.y, pos.p1, num));
					}
				}
			}

			curr = 1 - curr;
		}

		static int caseNum = 0;
		if (res == 1000000000)
			fout << "Case #" <<  (++ caseNum) << ": " << "THE CAKE IS A LIE" << endl;
		else 
			fout << "Case #" <<  (++ caseNum) << ": " << res << endl;
	
		cout << caseNum << endl;
}

	return 0;
}