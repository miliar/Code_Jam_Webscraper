#include <cstdio>
inline int min (int x, int y)
{
	return (x<y)? x:y;
}
void solve (int test)
{
	int i, x, N, suma = 0, suma_xor = 0, minv = 1<<30;
	scanf ("%d", &N);

	for (i=1; i <= N; ++i)
	{
		scanf ("%d", &x);
		suma += x;
		suma_xor ^= x;
		minv = min (minv, x);
	}

	printf ("Case #%d: ",test);
	if (suma_xor)
		printf ("NO\n");
	else
		printf ("%d\n", suma - minv);

}
int main()
{
	int T, t;

	freopen ("candy.in", "r", stdin);
	freopen ("candy.out", "w", stdout);

	scanf ("%d", &T);

	for (t=1; t <= T; ++t)
		solve (t);

	return 0;

}
