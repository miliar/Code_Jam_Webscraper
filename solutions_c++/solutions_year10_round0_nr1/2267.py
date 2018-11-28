#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int t, n;
	unsigned long k;
	int i,j,q;
	int *s, *p;
	scanf("%d\n", &t);
	for(i = 0; i < t; i++)
	{
		scanf("%d %ld\n", &n, &k);
		s = (int *) malloc((n + 1) * sizeof(int));
		p = (int *) malloc((n + 1) * sizeof(int));
		for(j = 0; j <= n; j++)
		{
			s[j] = 0;
			p[j] = 0;
		}
		p[0] = 1;
		s[0] = 1;
		p[1] = 1;
		for(j = 0; j < k; j++)
		{
			for(q = 1; q <= n; q++)
			{
				if(p[q] == 1)
				{
					if(s[q] == 0)
					{
						s[q] = 1;
					}
					else
					{
						s[q] = 0;
					}
				}
			}
			for(q = 1; q <= n; q++)
			{
				p[q] = s[q-1] * p[q-1];
			}
		}
		if(p[n] * s[n])
		{
			printf("Case #%d: ON\n", (i+1));
		}
		else
		{
			printf("Case #%d: OFF\n", (i+1));
		}
	}
	return 0;
}
					
