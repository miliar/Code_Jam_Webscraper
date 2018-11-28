#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int d[10005], l[10005], maxd[10005], got[100005], N;

inline int	read()
{
	char ch = getchar(); int x = 0; bool flag = 0;
	for (; ch != '-' && (ch < '0' || ch > '9'); ch = getchar());
	if (ch == '-') 	{	flag = 1;	ch = getchar();	}
	for (; ch >= '0' && ch <= '9'; ch = getchar()) x = x * 10 + ch - '0';
	if (flag) return - x; return x;
}

inline void	Main()
{
	N = read();
	for (int i = 1; i <= N; ++ i)
	{
		d[i] = read();
		l[i] = read();
		maxd[i] = 0;
		got[i] = 0;
	}
	d[N + 1] = read(); got[N + 1] = 0;
	maxd[1] = d[1];
	got[1] = 1;
	for (int i = 1; i <= N; ++ i)	if (got[i])
	{
		int tmp = min(maxd[i], l[i]);
		for (int j = i + 1; j <= N + 1 && d[j] - d[i] <= tmp; ++ j)
		{
			got[j] = 1;
			maxd[j] = max(maxd[j], d[j] - d[i]);
		}
	}
	if (got[N + 1])	printf("YES\n");	else printf("NO\n");
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T = read();
	for (int t = 1; t <= T; ++ t)
	{
		printf("Case #%d: ", t);
		Main();
	}
	return 0;
}
