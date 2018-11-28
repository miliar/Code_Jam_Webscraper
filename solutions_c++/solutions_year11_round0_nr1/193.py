#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int c[200], b[200], t[200], last[2], n;

int solve()
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		scanf("%s %d", &c[i], &b[i]);
		c[i] = c[i] == 'B';
//		printf("%d : %d %d\n", i, c[i], b[i]);
	}
	last[0] = last[1] = 0;
	b[0] = 1;
	for (int i = 1; i <= n; i++)
	{
		if (i == 1 || c[i] == c[i - 1])
		{
			t[i] = t[i - 1] + abs(b[i] - b[last[c[i]]]) + 1;
		} else
		{
			t[i] = max(t[last[c[i]]] + abs(b[i] - b[last[c[i]]]), t[i - 1]) + 1;
		}
//		printf("%d -- %d\n", i, t[i]);
		last[c[i]] = i;
	}
	return t[n];	
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
