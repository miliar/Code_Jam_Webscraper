
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

		int  PatrickSum = 0;
		int  Sum = 0;
		int  MinCandy = 9999999;
		for(int j=0; j<N; j++)
		{
			scanf("%d", &C);
			//printf("<%d>", C);
			PatrickSum ^= C;
			Sum += C;
			if ( MinCandy > C )
				MinCandy = C;
		}

		printf("Case #%d: ", i);
		if ( PatrickSum != 0 )
			printf("NO");
		else
			printf("%d", Sum - MinCandy);
    	printf("\n");
	}
  
	return  0;  
}

