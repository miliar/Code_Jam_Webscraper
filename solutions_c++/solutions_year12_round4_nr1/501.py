#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 10000 + 10;

int D[MAXN], L[MAXN], dist[MAXN];
int T, N, Len;

int Solve (int c)
{
	scanf ("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%d%d", D + i, L + i);
		//if (c == 7) printf ("%d %d\n", D[i], L[i]);
	}
	scanf ("%d", &Len);

	dist[0] = 2 * D[0];
	if (dist[0] >= Len) return 1;

	for (int i = 1; i < N; ++i)
	{
		dist[i] = 0;
		for (int j = 0; j < i; ++j)
			if (dist[j] >= D[i])
				dist[i] = max (dist[i], D[i] + min (D[i] - D[j], L[i]));
		if (dist[i] >= Len)
			return 1;
	}

	return 0;
}

int main(int argc, char *argv[])
{
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.txt", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		if (Solve (i))
			printf ("YES\n");
		else
			printf ("NO\n");
	}
	
	return 0;
}
