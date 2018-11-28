#include <cstdio>
#include <vector>

using namespace std;

int n, m;
int bin[10];
int sol[10];
vector< pair<int, int> > g[100];
int s;

void recur(int cnt, int sel)
{
    if(cnt == n)
	{
		for(int i = 0; i < m; ++i)
		{
			int a = 0;
			for(int j = 0; j < (int)g[i].size(); ++j)
			{
				pair<int, int> p;
				p = g[i][j];
				if(bin[p.first - 1] == p.second) a++;
			}
			if(a == 0) return;
		}
		if(sel < s) 
		{
			s = sel;
			for(i = 0; i < n; ++i) sol[i] = bin[i];
		}
		return;
	}
	recur(cnt + 1, sel);
	bin[cnt] = 1;
	recur(cnt + 1, sel + 1);
	bin[cnt] = 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int r;
	int i, j, cs = 0;
	scanf("%d", &r);
	while(r--)
	{
		scanf("%d %d", &n, &m);
        for(i = 0; i < m; ++i)
		{
			g[i].clear();
			int t;
			scanf("%d", &t);
			for(j = 0; j < t; ++j)
			{
				pair<int, int> p;
				scanf("%d %d", &p.first, &p.second);
				g[i].push_back(p);
			}
		}
		for(i = 0; i < n; ++i) bin[i] = 0;
		s = 10000;
		recur(0, 0);
		printf("Case #%d: ", ++cs);
		if(s == 10000)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			for(i = 0; i < n; ++i)
				printf("%d%c", sol[i], ((i < n - 1) ? ' ' : '\n'));
		}
	}
	return 0;
}