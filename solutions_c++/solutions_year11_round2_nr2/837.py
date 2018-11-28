
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];
int  dictval[10001][26];

// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int  C, D;
		int  P[200], V[200];
		int  Vindi[100];
		int  Vindi_tobe[100];
		int  Vindi_cnt = 0;

		double  Ans;

		scanf("%d %d", &C, &D);

		for(int j=0; j<C; j++)
		{
			scanf("%d %d", &P[j], &V[j]);
//			printf("%d %d\n", P[j], V[j]);
			for(int k=0; k<V[j]; k++)
				Vindi[Vindi_cnt++] = P[j] - P[0];
		}

		int  max = 0;
		Vindi_tobe[0] = 0;
		for(int j=1; j<Vindi_cnt; j++)
		{
			if ( Vindi[j] >= Vindi_tobe[j-1] + D )
				Vindi_tobe[j] = Vindi[j];
			else
				Vindi_tobe[j] = Vindi_tobe[j-1] + D;

			if ( max < Vindi_tobe[j] - Vindi[j] )
				max = Vindi_tobe[j] - Vindi[j];
		}

//		for(int j=0; j<Vindi_cnt; j++)
//			printf("%d %d\n", Vindi[j], Vindi_tobe[j]);

		Ans = ((double)max)/2;

		printf("Case #%d: ", i);
		printf("%.1f", Ans);
    	printf("\n");
	}
  
	return  0;  
}

