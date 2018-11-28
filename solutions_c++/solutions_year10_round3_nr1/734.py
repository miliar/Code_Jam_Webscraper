#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;

int a[10010];

struct NODE
{
	int A;
	int B;
};

NODE wi[1010];

bool operator < (const NODE & a, const NODE & b)
{
	return a.B > b.B;
}

int sum(int i)
{
	int s = 0;
	while(i > 0)
	{
		s += a[i];
		i -= (i & (-i));
	}
	return s;
}

void update(int i, int n, int d)
{
	while(i <= n)
	{
		a[i] += d;
		i += (i & (-i));
	}
}

int main()
{
	int n, T, i, cas;
	freopen("A_in.txt", "r", stdin);
	freopen("A_out.txt", "w", stdout);
	for(scanf("%d", &T), cas = 1; cas <= T; cas++)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		{
			scanf("%d%d", &wi[i].A, &wi[i].B);
		}
		sort(wi, wi + n);
		memset(a, 0, sizeof(a));
		int ans = 0;
		for(i = 0; i < n; i++)
		{
			ans += sum(wi[i].A);
			update(wi[i].A, 10000, 1);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}


