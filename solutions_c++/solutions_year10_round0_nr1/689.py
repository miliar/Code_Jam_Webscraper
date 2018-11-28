#include <cstdio>

using namespace std;

int main()
{
	freopen ("A-large.in", "r", stdin );
	freopen ("ans.out", "w", stdout );

	int T;
	scanf ("%d", &T);

	for(int cas = 1; cas <= T; cas++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		if( (k+1)%(1<<n) )
			printf ("Case #%d: OFF\n", cas);
		else
			printf ("Case #%d: ON\n", cas );
	}

	return 0;
}
