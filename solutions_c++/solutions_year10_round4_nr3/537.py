#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#define all(c) (c).begin(), (c).end() 
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

using namespace std;
int test, t, n, r;
const int MAXN = 200;
int g[MAXN][MAXN], p[MAXN][MAXN];

void init()
{
}

void process()
{

}

void print()
{
	printf ("Case #%d: \n", test + 1);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (test = 0; test < t; test++) 
	{
		scanf("%d", &n);
		memset(g, 0, sizeof(g));
		for (int i = 0; i < n; i++)
		{
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x++)
				for (int y = y1; y <= y2; y++)
					g[x][y]=1;
		}

		int count = 0;

		while (true)
		{
			int c = 0;
			for(int i = 1; i < MAXN; i++)
				for(int j = 1; j < MAXN; j++)
					c += g[i][j];
			if(c==0) break;

			memset(p, 0,sizeof(MAXN));
			for(int i = 2; i < MAXN; i++)
			{
				p[1][i] = g[1][i];
				if(!g[1][i-1])
					p[1][i] = 0;
				p[i][1]=g[i][1];
				if(!g[i-1][1])
					p[i][1] = 0;
			}
			p[1][1]=0;
			for(int i = 2;i < MAXN; i++)
				for(int j = 2; j < MAXN; j++)
					if(g[i][j])
						p[i][j] = g[i-1][j] | g[i][j-1];
					else
						p[i][j] = g[i-1][j] & g[i][j-1];
			memcpy(g, p, sizeof(g));
			count++;
		}
		printf("Case #%d: %d\n", test + 1, count);
	}
	return 0;
}