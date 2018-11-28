#include <cstdlib>
#include <cstdio>

int main()
{
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		int n, k;
		scanf("%d%d", &n, &k);

		int pn = 1 << n;
		if ((k+1) % pn == 0) printf("Case #%d: ON\n", t);
		else printf("Case #%d: OFF\n", t);
	}
	return 0;
}