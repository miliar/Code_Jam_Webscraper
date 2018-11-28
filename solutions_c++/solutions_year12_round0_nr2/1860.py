//Jakub "Cubix651" Cisło
//Zadanie: B - Google Code Jam
#include <cstdio>

int t, n, s, p, res, ti;

int main()
{
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
	{
		res = 0;
		scanf("%d%d%d", &n, &s, &p);
		while(n--)
		{
			scanf("%d", &ti);
			if(ti >= 3*p - 2)
				++res;
			else if((ti >= 3*p - 4) && (s > 0) && (ti > 0))
				++res, --s;
		}
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}
