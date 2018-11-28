#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) (a).begin(),(a).end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

struct portal
{
	portal(int a =-1, int b = -1) : r(a), c(b) {}
	bool operator<(const portal& p) const{
		return make_pair(make_pair(r,c), side) < make_pair(make_pair(p.r,p.c), p.side);
	}
	int r; int c; int side;
};

struct state
{
	bool operator<(const state& s) const 
	{
		return make_pair(make_pair(r,c), make_pair(p[0], p[1])) < make_pair(make_pair(s.r,s.c), make_pair(s.p[0],s.p[1]));
	}
	int r, c;
	portal p[2];
};

int main()
{
	freopen("B.in", "r", stdin);
	
	int T;
	cin >> T;
	For (LOL, 1, T+1)
	{
		int R, C;
		cin >> R >> C;
		
		char grid[20][20];
		memset(grid, '#', sizeof grid);
		
		int dx[4] ={0,0,1,-1};
		int dy[4] ={1,-1,0,0};
		
		int sr,sc,dr,dc;
		
		For (i, 1, R+1)
			For (j, 1, C+1)
			{
				cin >> grid[i][j];
				if (grid[i][j] == 'O') sr = i, sc = j;
				if (grid[i][j] == 'X') dr = i, dc = j;
			}
			
		R+=2, C+=2;
			
		portal last[4][20][20];
		For (i, 0, R)
			For (j, 0, C)
				if (grid[i][j] == '#')
					last[3][i][j] = portal(i,j);
				else
					last[3][i][j] = last[3][i][j-1];
				
		For (i, 0, R)
			for (int j = C-1; j >= 0; j--)
				if (grid[i][j] == '#')
					last[2][i][j] = portal(i,j);
				else
					last[2][i][j] = last[2][i][j+1];

		For (j, 0, C)
			For (i, 0, R)
				if (grid[i][j] == '#')
					last[1][i][j] = portal(i,j);
				else
					last[1][i][j] = last[1][i-1][j];

		For (j, 0, C)
			for (int i = R-1; i>= 0; i--)
				if (grid[i][j] == '#')
					last[0][i][j] = portal(i,j);
				else
					last[0][i][j] = last[0][i+1][j];					
		
		int ans = -1;
		
		map<state,int> dis;
		dis[(state){sr,sc,portal(),portal()}] = 0;
		deque<state> bfs;
		bfs.push_back((state){sr,sc,portal(),portal()});
		while (!bfs.empty())
		{
			state x = bfs.front(); bfs.pop_front();
			int r = x.r, c = x.c;

			int d = dis[x];
						if (r == dr && c == dc)
			{
				ans = d;
				break;
			}
			
			//cout << r << " " << c << " " << d << endl;
			//cout	<< x.p[0].r << " " << x.p[0].c << " " << x.p[0].side << endl;
			//cout	<< x.p[1].r << " " << x.p[1].c << " " << x.p[1].side << endl << endl;
			
			//shoot a portal?
			For (i, 0, 4)
				For (j, 0, 2)
				{
					state y = x;
					y.p[j] = last[i][r][c];
					y.p[j].side = i^1;
					if (y.p[0] < y.p[1]) swap(y.p[0], y.p[1]);
					if (!dis.count(y))
						dis[y] = d, bfs.push_front(y);
				}
				
			//walk?
			For (i, 0, 4)
			{
				int nr = r + dy[i], nc = c + dx[i];
				if (grid[nr][nc] != '#')
				{
					state y = x;
					y.r = nr, y.c = nc;
					if (!dis.count(y))
						dis[y] = d+1, bfs.push_back(y);
				}
				else
				{
					//cout << "considering" << nr << " "<< nc << " " << i << endl;
					For (j, 0, 2)
						if (nr == x.p[j].r && nc == x.p[j].c && i == (1^x.p[j].side) && x.p[!j].r != -1)
						{
							state y = x;
							y.r = x.p[!j].r + dy[x.p[!j].side], y.c = x.p[!j].c + dx[x.p[!j].side];
							//cout << "tele " << y.r << " "<< y.c << endl;
							if (!dis.count(y))
								dis[y] = d+1, bfs.push_back(y);
						}
				}
			}
		}
		
		printf("Case #%d: ", LOL);
		if (ans == -1)
			puts("THE CAKE IS A LIE");
		else
		cout << ans << endl;
	}
	
	return 0;
}