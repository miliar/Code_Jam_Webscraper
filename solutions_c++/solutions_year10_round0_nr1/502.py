#include <cstdio>
#include <cstring>

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T; scanf("%d",&T);
	for(int t = 0; t < T; t ++ )
	{
		int n, k;
		scanf("%d%d", &n, &k);
		k %= (1<<n);
		printf("Case #%d: ", t+1);
		if( k == (1<<(n))-1 )
			printf("ON\n"); else printf("OFF\n");
	
	}
	return 0;
}
