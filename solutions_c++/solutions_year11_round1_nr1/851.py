
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

typedef  long long  int64;

int64 gcd(int64 a, int64 b)
{
    while (b != 0)
	{
       int64 t = b;
       b = a % b;
       a = t;
	}
    return a;
}

// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int64  N = 0;
		int64  Pd = 0, Pg = 0;

		int  Ans = 0;
		scanf("%I64d %I64d %I64d", &N, &Pd, &Pg);
//		printf("%I64d %I64d %I64d", N, Pd, Pg);

		if ( Pg == 0 || Pg == 100 )
		{
			if ( Pg == Pd )
				Ans = 1;
			else
				Ans = 0;
		}
		else
		{
			int64 t = 100 / gcd(100, Pd);
			if ( t <= N )
				Ans = 1;
			else
				Ans = 0;
		}

		printf("Case #%d: ", i);
		if ( Ans == 1 )
			printf("Possible");
		else
			printf("Broken");
    	printf("\n");
	}
  
	return  0;  
}

