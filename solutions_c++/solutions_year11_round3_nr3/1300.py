#include <cstdio>
int test, qt;
unsigned long long l, h, tab[10001];
int main()
{
	scanf("%d", &test);
	for(int t=0; t<test; t++)
	{
		scanf("%d%llu%llu", &qt, &l, &h);
		for(int i=0; i<qt; i++)
			scanf("%llu", &tab[i]);
		unsigned long long i=0;
		int j=0;
		for(i=l; i<=h; i++)
		{
			for(j=0; j<qt; j++)
				if(tab[j]%i && i%tab[j])break;
			if(j==qt) break;
		}
		if(j==qt)
			printf("Case #%d: %llu\n", t+1, i);
		else 
			printf("Case #%d: NO\n", t+1);
	}
	
	return 0;
}
