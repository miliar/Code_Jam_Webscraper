#include "stdio.h"
#include "stdlib.h"

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(x) ((x)>(0)?(x):-(x))

void main()
{
	FILE *f;
	int n,d,x,k=0;
	int lastO, lastB;
	int time, timeO, timeB;
	int lollypop[1000];
	int minlol;
	char c[10];
	int sum,rs;
	fopen_s(&f, "C-large.in", "rb");
	fscanf_s(f, "%d", &n);
	while(n--)
	{
		printf("Case #%d: ",++k);
		fscanf_s(f, "%d", &d);
		sum = 0;
		minlol = 1000001;
		rs = 0;
		while(d--)
		{
			fscanf_s(f, "%d", &lollypop[d]);
			sum ^= lollypop[d];
			minlol = min(minlol, lollypop[d]);
			rs += lollypop[d];
		}
		rs -= minlol;
		if (sum)
		{
			printf("NO");
		}
		else
		{
			printf("%d", rs);
		}
		printf("\n");
	}
	fclose(f);
}