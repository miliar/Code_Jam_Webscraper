#include <stdio.h>
#include <math.h>

#define SQR(x) ((x)*(x))
#define MIN(a, b) (((a)<(b))?(a):(b))
#define MAX(a, b) (((a)>=(b))?(a):(b))

#define y1 Y1

int cases, n, x1, x2, x3, y1, y2, y3, r1, r2, r3;

int main()
{
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		scanf(" %d", &n);
		if (n==1)
		{
			scanf(" %d %d %d", &x1, &y1, &r1);
			printf("Case #%d: %d\n", cs, r1);
		}
		if (n==2)
		{
			scanf(" %d %d %d", &x1, &y1, &r1);
			scanf(" %d %d %d", &x2, &y2, &r2);
			printf("Case #%d: %d\n", cs, MAX(r1, r2));
		}
		if (n==3)
		{
			scanf(" %d %d %d", &x1, &y1, &r1);
			scanf(" %d %d %d", &x2, &y2, &r2);
			scanf(" %d %d %d", &x3, &y3, &r3);
			printf("Case #%d: %.6f\n", cs, 
						 MIN(MIN(MAX(sqrt(SQR(x2-x1)+SQR(y2-y1))/2+r1/2.0+r2/2.0, r3),
										 MAX(sqrt(SQR(x3-x1)+SQR(y3-y1))/2+r1/2.0+r3/2.0, r2)),
								 MAX(sqrt(SQR(x3-x2)+SQR(y3-y2))/2+r2/2.0+r3/2.0, r1)));
		}		
	}
	return 0;
}
