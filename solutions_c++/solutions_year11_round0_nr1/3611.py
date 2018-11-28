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
	char c[10];
	fopen_s(&f, "A-large.in", "rb");
	fscanf_s(f, "%d", &n);
	while(n--)
	{
		fscanf_s(f, "%d", &d);
		lastO = lastB = 1;
		timeO = timeB = time = 0;
		while(d--)
		{
			fscanf_s(f, "%s %d", &c, 10, &x);
			if (c[0] == 'O')
			{ // pomaranc
				timeO += abs(lastO-x);
				timeO = time = max(timeO, time);
				++timeO;
				++time;
				lastO = x;
			}
			else
			{ // blue
				timeB += abs(lastB-x);
				timeB = time = max(timeB, time);
				++timeB;
				++time;
				lastB = x;
			}
		}
		printf("Case #%d: %d\n", ++k, time);
	}
	fclose(f);
}