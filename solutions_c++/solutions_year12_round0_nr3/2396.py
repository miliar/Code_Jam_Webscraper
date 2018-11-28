#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int N = 2000001;
const int maxn = 10;
int siz, a, b;
char numa[maxn], numb[maxn];
bool vis[N];

void change(int x, char *p)
{
	int i, j;
	char tmp[maxn];

	for (i = 0; x; i++)
	{
		tmp[i] = x % 10 + '0';
		x /= 10;
	}

	siz = i;
	for (j = 0, i--; i >= 0; j++, i--)
		p[j] = tmp[i];
	p[j] = '\0';
}

int to_num(char *p)
{
	int i, total = 0;

	for (i = 0; i < siz; i++)
		total = total * 10 + p[i] - '0';
	return total;
}

int solve()
{
	int i, total = 1, n, m;
	char tmp[maxn];

	n = to_num(numa);
	vis[n] = true;
	for (i = 1; i < siz; i++)
	{
		strcpy(tmp, numa + i);
		strncat(tmp, numa, i);
		if (tmp[0] == '0')
			continue;

		m = to_num(tmp);
		if (n < m && m <= b && !vis[m])
		{
			vis[m] = true;
			total++;
		}
	}
	
	return total * (total - 1) / 2;
}

int main()
{
	int t, i, ans, cas = 1;

	freopen("C-large.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> t;
	while (t--)
	{
		memset(vis, 0, sizeof(vis));
		scanf("%d%d", &a, &b);
		ans = 0;
		for (i = a; i < b; i++)
		{
			if (!vis[i])
			{
				change(i, numa);
				ans += solve();
			}
		}
		printf("Case #%d: %d\n", cas++, ans);
	}

	return 0;
}