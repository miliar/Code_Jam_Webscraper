#include <cstdio>
#include <cstdlib>
int cmp(int* a, int* b)
{
	return *b - *a;
}
int best(int n, int s, int p, int* t)
{
	int b = 0;
	qsort(t, n, sizeof(t[0]), (int(*)(const void*, const void*))cmp);
	for (int i = 0, j = 0; i < n; i++)
		if (t[i] / 3 >= p || t[i] / 3 == p - 1 && t[i] % 3)
			b++;
		else if (j < s && t[i] > 1 && (t[i] / 3 == p - 1 && t[i] % 3 == 0 || t[i] / 3 == p - 2 && t[i] % 3 > 1))
		{
			j++;
			b++;
		}
	return b;
}
int main()
{
	int t, n, s, p;
	int tr[100];
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%d%d", &n, &s, &p);
		for (int j = 0; j < n; j++)
			scanf("%d", &tr[j]);
		printf("Case #%d: %d\n", i, best(n, s, p, tr));
	}
	return 0;
}