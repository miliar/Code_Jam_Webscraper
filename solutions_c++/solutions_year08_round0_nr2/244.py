#include <cstdio>
#include <algorithm>

using namespace std;

int n;
int adj[200][200];
int cx[200], cy[200], px[200], py[200];

int path(int x)
{
	int y;
	for (y = 0; y < n; ++y)
		if (!py[y] && adj[x][y] != 0) 
		{
			py[y] = 1;
		  	if (cy[y] == -1 || path(cy[y])) {
				cy[y] = x; cx[x] = y;
				return 1;
			}
		}
	return 0;
}

int matching(){
	int cnt = 0;

	fill(cx,cx + n, -1);
	fill(cy,cy + n, -1);
	for (int x = 0; x < n; ++x)
		if(cx[x] == -1)
		{
			fill(px, px + n, 0);
			fill(py, py + n, 0);
			if(path(x)) cnt++;
		}
	return cnt;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j, t;
	int na, nb, r;
	int time[200][2];
	int cs = 0;

	scanf("%d", &r);
	while(r--)
	{
		scanf("%d", &t);
		scanf("%d %d", &na, &nb);
		n = na + nb;
		for(i = 0; i < n; ++i)
		{
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			time[i][0] = a * 60 + b;
			time[i][1] = c * 60 + d;
		}
		fill(adj[0], adj[n], 0);
		for(i = 0; i < n; ++i)
		{
			for(j = 0; j < n; ++j)
			{
				if(i < na && j < na) continue;
				if(i >= na && j >= na) continue;
				adj[i][j] = (time[i][1] + t <= time[j][0]) ? 1 : 0;
			}
		}
		i = matching();
		int s1 = 0, s2 = 0;
		for(i = 0; i < n; ++i)
		{
			if(cx[i] != -1 && cy[i] != -1) continue;
			int f = 0;
			if(cx[i] == -1 && cy[i] == -1) f = 1;
			else if(cy[i] == -1) f = 1;
			if(f)
			{
				if(i < na) s1++;
				else s2++;
			}
		}
		printf("Case #%d: %d %d\n", ++cs, s1, s2);
	}
	return 0;
}