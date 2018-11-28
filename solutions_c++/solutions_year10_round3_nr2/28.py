#include <cstdio>
#include <cmath>
#include <cstring>


int nt;

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		int a, b, c;

		scanf("%d %d %d", &a, &b, &c);

		__int64 aa = a, bb = b, cc = c;

		int res = 0;

		aa *= cc;

		while(aa < bb)
		{
			for(int i = (1 << res); i > 0 && aa < bb; i--) aa *= cc;
			res++;
		}

		printf("%d\n", res);
	}

	return 0;	
}