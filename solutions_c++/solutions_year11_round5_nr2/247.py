#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAXN = 1010;
const int MAXM = 10010;

int n;
int a[MAXM], b[MAXM], c[MAXM];


void init()
{
	scanf("%d", &n);
	memset(a, 0, sizeof(a));
	for (int i=1; i<=n; ++i)
	{
		int j;
		scanf("%d", &j);
		++a[j];
	}
}

bool check(int k)
{
	int i, j;
	memcpy(b, a, sizeof(a));
	memset(c, 0, sizeof(c));
	for (i=1; i<=10000; ++i)
	while (b[i] > 0)
	{
		++c[i+k];
		if (c[i] == 0)
		{
			for (j=i; j<i+k; ++j)
			if (b[j] > 0) --b[j];
			else return false;
		}
		else
		{
			++c[i+k];
			for (j=i; j<i+k; ++j)
			if (b[j] > 0) -- b[j];
			else
			{
				--c[i+k];
				--c[i];
				break;
			}
		}
	}
	return true;
}

void solve()
{
	if (n == 0)
	{
		printf("0\n");
		return;
	}
	int l = 1;
	int r = n;
	int m;
	while (l <= r)
	{
		m = (l + r) >> 1;
		if (check(m)) l = m + 1;
		else r = m - 1;
	}
	printf("%d\n", r);
}


int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int CASE, TT;
	scanf("%d", &TT);
	for (CASE=1; CASE<=TT; ++CASE)
	{
		printf("Case #%d: ", CASE);
		init();
		solve();
	}
	return 0;
}

