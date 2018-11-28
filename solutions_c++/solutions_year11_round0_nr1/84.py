#include <stdio.h>
#include <math.h>

int main()
{
int n , cas;

	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	scanf("%d" , &cas);
	for (int ca = 1; ca <= cas; ca ++)
	{
		scanf("%d", &n);
		char s[3];
		int bu;

		int oset = 1;
		int bset = 1;
		int lasto = 0; 
		int lastb = 0;
		int res = 0;
		for (int i = 0; i < n; i ++)
		{
			scanf("%s %d" , s , &bu);
			if (s[0] == 'O')
			{
				int ti = abs(bu - oset) - (res - lasto);
				if (ti < 0) ti = 0;
				res += ti + 1;
				lasto = res;
				oset = bu;
			}
			else
			{
				int ti = abs(bu - bset) - (res - lastb);
				if (ti < 0) ti = 0;
				res += ti + 1;
				lastb = res;
				bset = bu;
			}
		}
		printf("Case #%d: %d\n" , ca , res);
	}
	return 0;
}