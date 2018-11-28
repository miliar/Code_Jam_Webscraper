
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

typedef  long long  int64;

int comparisonFunction(const void *a, const void *b);

// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int64  L, T, N, C;
		int64  Ans = 0;
		int64  ai[1001][2];

		scanf("%I64d %I64d %I64d %I64d", &L, &T, &N, &C);

		for(int j=0; j<C; j++)
		{
			scanf("%I64d", &ai[j][0]);
		}
/*
		printf("%I64d %I64d %I64d %I64d\n", L, T, N, C);
		for(int j=0; j<C; j++)
			printf("%I64d", ai[j][0]);
		printf("\n");
*/
		int64 ai_len = C;

		int64 sumai = 0;
		for(int j=0; j<C; j++)
			sumai += ai[j][0];

		// fill ai[j][1]
		int64 multi = N/C;
		int64 resi = N%C;
		for (int j=0; j<C; j++)
			ai[j][1] = multi;
		for (int j=0; j<resi; j++)
			ai[j][1]++;

		// calc  maxtime
		int64 sum = 0;
		for (int j=0; j<C; j++)
			sum += ai[j][0]*ai[j][1];
		int64 maxtime = sum * 2;
//		printf("maxtime = %d\n", maxtime);

		int64 savetime = 0;
		// calc savetime
		if  ( T < maxtime )
		{
			// point out boostable 
			int64 t_multi = (T/2)/sumai;
			int64 t_resi = (T/2)%sumai;
			for(int j=0; j<C; j++)
				ai[j][1] -= t_multi;
			for(int j=0; j<C; j++)
			{
				if ( t_resi == 0 )
					break;
				if ( t_resi >= ai[j][0] )
				{
					t_resi -= ai[j][0];
					ai[j][1]--;
				}
				else
				{
					ai[C][0] = ai[j][0] - t_resi;
					ai[C][1] = 1;
					t_resi = 0;
					ai[j][1]--;
					ai_len++;
					break;
				}
			}

			qsort((void *)&ai[0], (size_t) ai_len, sizeof(ai[0]), comparisonFunction);

			int64 cntdown = L;
			for(int j=0; j<C; j++)
			{
				if ( ai[j][1] == 0 )
					continue;
				if ( cntdown == 0 )
					break;
				if ( cntdown >= ai[j][1] )
				{
					savetime += ai[j][0]*ai[j][1];
					cntdown -= ai[j][1];
				}
				else 
				{
					savetime += ai[j][0]*cntdown;
					cntdown = 0;
				}
			}

//			for(int j=0; j<ai_len; j++)
//				printf("%d: %I64d %I64d\n", j, ai[j][0], ai[j][1]);
		}
//		printf("savetime=%I64d\n", savetime);
		Ans = maxtime - savetime;

		printf("Case #%d: ", i);
		printf("%I64d", Ans );
		printf("\n");
	}
  
	return  0;  
}

int comparisonFunction(const void *a, const void *b) {
  return  (int)( ((int64*)b)[0] - ((int64*)a)[0] );
}
