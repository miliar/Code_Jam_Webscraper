#include <stdio.h>
#include <set>

int main()
{
	int T;
	scanf("%d", &T);
	for(int ca = 1; ca <= T; ca++)
	{
		int n, s = 0, x = 0, m = 100000000;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
		{
			int c;
			scanf("%d", &c);
			s += c;
			if(c < m) m = c;
			x ^= c;
		}
		printf("Case #%d: ", ca);
		if(!x) printf("%d\n", s - m);
		else printf("NO\n");
	}
	return 0;
}

