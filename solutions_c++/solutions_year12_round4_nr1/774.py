#include<stdio.h>
#include<string.h>
#include<algorithm>
#define MAXD 10010
#define INF 0x3f3f3f3f
using namespace std;
struct Line
{
	int d, len;
	bool operator < (const Line &t) const
	{
		return d < t.d;
	}
}line[MAXD];
int N, f[MAXD], D;
void init()
{
	int i;
	scanf("%d", &N);
	line[0].d = 0;
	for(i = 1; i <= N; i ++)
		scanf("%d%d", &line[i].d, &line[i].len);
	sort(line + 1, line + 1 + N);
	scanf("%d", &D);
	++ N;
	line[N].d = D, line[N].len = INF;
}
void solve()
{
	int i, j, k;
	memset(f, 0x3f, sizeof(f));
	f[1] = 0;
	for(i = 1; i < N; i ++)
	{
		if(f[i] == INF)
			continue;
		for(j = i + 1; j <= N && line[j].d - line[i].d <= line[i].d - f[i]; j ++)
		{
			k = max(line[i].d, line[j].d - line[j].len);
			if(k < f[j])
				f[j] = k;
		}
	}
	printf("%s\n", f[N] == INF ? "NO" : "YES");
}
int main()
{
	int t, tt;
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for(tt = 0; tt < t; tt ++)
	{
		init();
		printf("Case #%d: ", tt + 1);
		solve();
	}
	return 0;
}
