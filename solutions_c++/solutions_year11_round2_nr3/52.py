#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<utility>
#include<sstream>
#include<vector>
#include<string>
#include<set>
#include<map>

using namespace std;

const int maxn = 2000 + 50;

int N, M;
int u[maxn], v[maxn];
int g[maxn][maxn], to[maxn][maxn];
bool vis[maxn][maxn];
vector<int> poly[maxn];
int cpoly;

void dfs(int x, int y, int cpoly)
{
	if(vis[x][y]) return;
	vis[x][y] = true;
	poly[cpoly].push_back(x);
	dfs(y, to[x][y], cpoly);
}

int flavor[maxn];
int opt[maxn];
bool occur[maxn];
int answer;

void eval(int x, int c)
{
	if(x == N)
	{
		if(c <= answer) return;
		for(int i=0; i<cpoly; i++)
		{
			memset(occur, 0, sizeof(occur));
			for(int j=0; j<poly[i].size(); j++)
				occur[flavor[poly[i][j]]] = true;

			bool check = true;
			for(int j=0; j<c; j++)
				if(occur[j] == false) check = false;

			if(!check) return;
		}

		answer = c;
		for(int j=0; j<N; j++)
			opt[j] = flavor[j];

		return;
	}

	for(int i=0; i<=c; i++)
	{
		flavor[x] = i;
		eval(x + 1, i==c ? c+1 : c);
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int ntest;
	scanf("%d", &ntest);
	for(int test = 1; test <= ntest; test++)
	{
		memset(g, 0, sizeof(g));
		memset(vis, 0, sizeof(vis));

		scanf("%d%d", &N, &M);
		for(int i=0; i<M; i++)
		{
			scanf("%d", &u[i]);
			u[i]--;
		}
		for(int i=0; i<M; i++)
		{
			scanf("%d", &v[i]);
			v[i]--;
		}
		for(int i=0; i<M; i++)
		{
			g[u[i]][v[i]] = g[v[i]][u[i]] = 1;
		}
		for(int i=0; i<N; i++)
		{
			g[i][(i+1)%N] = 2;
			g[(i+1)%N][i] = 1;
		}

		for(int i=0; i<N; i++)
		{
			int before = -1;
			for(int j=1; j<N; j++)
				if(g[i][(i+j)%N] != 0)
				{
					if(before != -1) to[before][i] = (i+j) % N;
					before = (i+j) % N;
				}
		}

		cpoly = 0;
		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				if(g[i][j] == 1 && vis[i][j] == false)
				{
					poly[cpoly].clear();
					dfs(i, j, cpoly);
					cpoly++;
				}

		answer = 0;
		eval(0, 0);

		printf("Case #%d: %d\n", test, answer);
		for(int i=0; i<N; i++)
		{
			printf("%d", opt[i] + 1);
			if(i == N-1) printf("\n");
			else printf(" ");
		}
	}
	return 0;
}
