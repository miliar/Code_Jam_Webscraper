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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int INF = 10005;
int gr[105][105];
char g[105][105];
int dir[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};
int n, m, cnt;

struct State
{
	int r, c;
};
vector<State> Vec;

void DFS(int R, int C)
{
	int p, temp, rr, cc, r, c;
	State ste;
	temp = gr[R][C];
	ste.r = R, ste.c = C;
	Vec.push_back(ste);
	rr = -1, cc = -1;
	for (p = 0; p < 4; p++)
	{
			r = R+dir[p][0];
			c = C+dir[p][1];
			if(r>=0 && r<n && c>=0 && c<m)
			{
				if(temp > gr[r][c])
				{
						temp = gr[r][c];
						rr = r;
						cc = c;
					}
				}
	}
	if(rr == -1 && cc == -1)
		return;
	DFS(rr,cc);
}

int main()
{
	freopen("bin.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	int i, j, k, t,r, c, temp, p, rr, cc, nsize;
	scanf("%d",&t);
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d:\n",i);
		scanf("%d%d",&n,&m);
		for (j = 0; j < n; j++)
		{
			for (k = 0; k < m; k++)
			{
				scanf("%d",&gr[j][k]);
				g[j][k] = '#';
			}
		}
		g[0][0] = 'a';
		cnt = 0;
		Vec.clear();
		DFS(0,0);
		nsize = Vec.size();
		for (p = 0; p < nsize; p++)
			g[Vec[p].r][Vec[p].c] = g[0][0];
		for (j = 0; j < n; j++)
		{
			for (k = 0; k < m; k++)
			{
				if(g[j][k] == '#')
				{
					Vec.clear();
					DFS(j,k);
					nsize = Vec.size();
					r = Vec[nsize-1].r, c= Vec[nsize-1].c;
					if(g[r][c] == '#')
						g[r][c] = 'a'+(++cnt);
					for (p = 0; p < nsize; p++)
						g[Vec[p].r][Vec[p].c] = g[r][c];
				}
			}
		}
		for (j = 0; j < n; j++)
		{
			for (k = 0; k < m; k++)
			{
				printf("%c ",g[j][k]);
			}
			printf("\n");
		}
	}
	return 0;
}
