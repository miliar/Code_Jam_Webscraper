#include <stdio.h>
#include <string.h>
#include <math.h>
#define MAXSIZE 20
//#define C 40
//#define D 40
void main (void)
{
	int T, I;
	FILE* out;
	scanf("%d", &T);
	if(!( out=fopen("123.out", "w") ))
	{
		printf("open error\n");
	}
	for(I=1; I<=T; I++)
	{
		int i, n, sum, min, num[MAXSIZE], digit[21], impossible=0;
		memset(digit, 0, sizeof(digit) );
		scanf("%d", &n);
		for(i=0; i<n; i++)
		{
			scanf("%d", &num[i]);
			impossible ^= num[i];
		}

		if (impossible)
		{
			fprintf(out, "Case #%d: NO\n", I);
			printf("Case #%d: NO\n", I);
		}
		else
		{
			sum = min = num[0];
			for(i=1; i<n; i++)
			{
				sum += num[i];
				if(min>num[i])
				{
					min = num[i];
				}
			}
			sum -= min;
			fprintf(out, "Case #%d: %d\n", I, sum);
			printf("Case #%d: %d\n", I, sum);
		}
	}
}