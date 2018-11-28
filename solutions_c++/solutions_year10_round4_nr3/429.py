#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;

int x, y, x1, y1, x2, y2;
int w[200][200], r;
int n, m;

void init()
{
	n = 0; m = 0;
	memset(w, 0, sizeof w);
	for(int i=1; i<=r; ++i)
	{
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for(int a=x1; a<=x2; ++a)
		{
			for(int b=y1; b<=y2; ++b)
			{
				w[b][a] = 1;
			}
		}
		m = max(m, x2);
		n = max(n, y2);
	}
}

void out()
{
	for(int i=1; i<=n; ++i)
	{
		for(int j=1; j<=m; ++j) printf("%d ", w[i][j]);
		puts("");
	}
}

void solve()
{
	int t = 0, cnt = 0;
	for(int i=1; i<=n; ++i) for(int j=1; j<=m; ++j) cnt += w[i][j];

	while(cnt > 0)
	{
		t++;
		//out();
		//printf("%d %d\n", t, cnt);
		for(int i=n; i>=1; --i)
		{
			for(int j=m; j>=1; --j)
			{
				int flag = 0;
				if(i > 1 && w[i-1][j]) flag++;
				if(j > 1 && w[i][j-1]) flag++;

				if(w[i][j] && !flag)
				{
					cnt--;
					w[i][j] = 0;
				}
				if(!w[i][j] && flag == 2)
				{
					cnt++;
					w[i][j] = 1;
				}
			}
		}
		//printf("%d %d\n", t, cnt);
		//puts("");
		//out();
	}
	printf("%d\n", t);
}

int main()
{
	int t, tc = 0;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d", &r);
		init();
		printf("Case #%d: ", ++tc);
		solve();
	}
	return 0;
}

