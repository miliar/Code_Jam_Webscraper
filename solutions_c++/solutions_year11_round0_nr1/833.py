#include <assert.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>

int solve()
{
	int n, p, t = 0, P[2] = {1, 1}, T[2] = {0, 0};
	char r;
	scanf("%d", &n);
	while (n--)
	{
		scanf(" %c %d", &r, &p);
		assert(r == 'O' || r == 'B');
		r = r == 'O';
		t += 1 + std::max(0, abs(P[r] - p) - (t - T[r]));
		P[r] = p;
		T[r] = t;
	}
	return t;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		printf("Case #%d: %d\n", i, solve());
	return 0;
}