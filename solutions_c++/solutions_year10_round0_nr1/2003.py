#include <cstdio>


int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	int T;

	int n, K;

	scanf ("%d\n", &T);

	for (int caz = 1; caz <= T; ++caz)
	{
		scanf ("%d %d\n", &n, &K);

		printf ("Case #%d: ", caz);
		if ( (K - ((1<<n) - 1)) % (1<<n) == 0)
			printf ("ON\n");
		else 
			printf ("OFF\n");


	}

	return 0;
}


	
