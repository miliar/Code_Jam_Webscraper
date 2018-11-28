#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }


int xabs(int a) { return a < 0 ? -a : +a; }
int d[101][101][101];

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n; scanf("%d", &n);
		vector< pii > a(n);
		int cells = 100;
		for(int i = 0; i < n; ++i)
		{
			string s;
			int p;
			cin >> s >> p;
			int q;
			if(s == "B")
				q = 0;
			else
				q = 1;
			a[i] = mp(q, p - 1);
		}
		memset(d, -1, sizeof d);
		d[0][0][0] = 0;
		queue< pair<int, pii> > q;
		q.push(mp(0, mp(0, 0)));
		while(q.size())
		{
			int p = q.front().X;
			int x = q.front().Y.X;
			int y = q.front().Y.Y;
			q.pop();
			if(p == n)
				break;

			for(int dx = -1; dx <= 1; ++dx) 
			for(int px = 0; px <= 1;++ px) if((px == 1 && dx == 0 && a[p].X == 0 && a[p].Y == x) || px == 0)
				for(int dy = -1; dy <= 1; ++dy)
				for(int py = 0; py <= 1 - px; ++py) if((py == 1 && dy == 0 && a[p].X == 1 && a[p].Y == y) || py == 0)
				{
					int nx = x + dx;
					int ny = y + dy;
					if(nx < 0 || ny < 0 || nx >= cells || ny >= cells)
						continue;
					int np = p + px + py;
					if(d[np][nx][ny] == -1)
					{
						d[np][nx][ny] = d[p][x][y] + 1;
						q.push(mp(np, mp(nx, ny)));
					}
				}
		}
		int best = -1;
		for(int i = 0; i < 100; ++i)
			for(int j = 0; j < 100; ++j)
				if(d[n][i][j] != -1)
				{
					if(best == -1 || best > d[n][i][j])
						best = d[n][i][j];
				}
		printf("Case #%d: %d\n", z + 1, best);
	}
	return 0;
}
#endif

