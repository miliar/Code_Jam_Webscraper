#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>
#include <set>
using namespace std;

struct Node
{
	int x,y,w;
	Node()
	{}

	Node(int a, int b, int c)
	{
		 x =a ;
		 y = b;
		 w = c;
	}
};

const int MAX  = 502;
const int H  = 250;
vector <string> sq;
vector <vector <vector <string> > > dp;
vector <vector <Node> > rep;
bool added;
const int dx[4] ={0,1,0,-1};
const int dy[4] ={1,0,-1,0};
bool TryReplace(int x, int y, int w, string s)
{
	if (dp[x][y][w+H].length() == 0 || dp[x][y][w+H].length() > s.length() || dp[x][y][w+H].length() == s.length()  && dp[x][y][w+H] > s)
	{
		dp[x][y][w+H] = s;
		added = true;
		return true;
	}
	return false;
}

int main()
{
	freopen("test2.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int t;

	cin >> t;
	for (int k = 1; k <= t; k ++)
	{
		cout << "Case #" << k << ":" << endl; 
		int w,q;
		cin >> w >> q;
		sq.resize(w);
		for (int i = 0; i < w; i ++)
			cin >> sq[i];
		added = true;
		dp.assign(w, vector <vector <string> >(w  , vector <string>(MAX,"") ));
		rep.assign(2, vector <Node>());
		for (int i = 0; i < w; i ++)
				for (int j = 0; j < w; j ++)
					if (isdigit(sq[i][j]))
					{
						dp[i][j][(int)(sq[i][j]-'0')+H] += sq[i][j];
						rep[0].push_back (Node(i,j,(int)(sq[i][j]-'0')));
					}
					
		int x,y,nw;
		int now = 0;
		int nx,ny;
		char c;
		string ns;

		while (rep[now].size() > 0)
		{
			for (int i = 0; i < rep[now].size(); i ++)
			{

				for (int a = 0; a < 4; a ++)
				{
					x = rep[now][i].x+dx[a];
					y = rep[now][i].y+dy[a];
					if (x < 0 | y < 0 || x >= w || y >= w)
						continue;
					c = sq[x][y];
					for (int b = 0; b < 4; b ++)
					{
						nx = x + dx[b];
						ny = y + dy[b];
						if (nx < 0 | ny < 0 || nx >= w || ny >= w)
							continue;
						if (c == '+')
							nw = rep[now][i].w + (int)(sq[nx][ny]-'0');
						else
							nw = rep[now][i].w - (int)(sq[nx][ny]-'0');
						if (nw > H || nw < -H)
							continue;
						ns = dp[rep[now][i].x][rep[now][i].y][rep[now][i].w+H];
						ns += c;
						ns += sq[nx][ny];
						if (TryReplace(nx,ny,nw, ns))
							rep[1-now].push_back(Node(nx,ny,nw));
					}
				}
			}
			rep[now].clear();
			now = 1 - now;
		}
		for (int i = 0; i < q; i ++)
		{
			int f;
			cin >> f;
			ns = "";
			
			for (x = 0; x < w; x ++)
				for (y = 0; y < w; y ++)
					if (dp[x][y][f+H].length() != 0)
					{
						if (ns == "" || ns.length() > dp[x][y][f+H].length() || (ns.length() == dp[x][y][f+H].length() && ns > dp[x][y][f+H]))
							ns = dp[x][y][f+H];
					}
			cout << ns << endl;
		}

	}
	return 0;
}