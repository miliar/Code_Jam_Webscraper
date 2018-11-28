
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int  N;
		int  C;

		scanf("%d", &N);

		int  Ans = 0;
		for(int j=1; j<=N; j++)
		{
			scanf("%d", &C);
			//printf("<%d>", C);
			if ( C != j )
				Ans++;
		}

		printf("Case #%d: ", i);
		printf("%.6f", (float)Ans);
    	printf("\n");
	}
  
	return  0;  
}

