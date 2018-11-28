
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

typedef  long long  int64;

// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int  R, C;
		char canvas[50][51];
		char newcanvas[50][51];
		int  Ans = 0;
		
		scanf("%d %d", &R, &C);

		for(int j=0; j<R; j++)
			scanf("%s", canvas[j]);

		// initialize newcanvas
		for(int j=0; j<R; j++)
		{
			for(int k=0; k<C; k++)
				newcanvas[j][k] = '.';
			newcanvas[j][C] = '\0';
		}

		Ans = 1;
		for(int j=0; j<R; j++)
		{
			for(int k=0; k<C; k++)
			{
				if ( canvas[j][k] == '.' )
					continue;

				if ( j==R-1 || k==C-1 )
				{
					Ans = 0;
					break;
				}

				if ( canvas[j][k+1] == '.' || canvas[j+1][k] == '.' || canvas[j+1][k+1] == '.' )
				{
					Ans = 0;
					break;
				}

				canvas[j][k] = '.';
				canvas[j][k+1] = '.';
				canvas[j+1][k] = '.';
				canvas[j+1][k+1] = '.';
				newcanvas[j][k] = '/';
				newcanvas[j][k+1] = '\\';
				newcanvas[j+1][k] = '\\';
				newcanvas[j+1][k+1] = '/';
			}
			if ( Ans == 0 )
				break;
		}


		printf("Case #%d:\n", i);
		if ( Ans == 0 )
		{
			printf("Impossible\n");
		}
		else
		{
			for(int j=0; j<R; j++)
				printf("%s\n", newcanvas[j]);
		}
	}
  
	return  0;  
}
