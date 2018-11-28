#define	_CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <assert.h>

#define SIZE	10

static char M[SIZE][SIZE];
static int GX[SIZE+1][SIZE+1];
static int GY[SIZE+1][SIZE+1];
static int S[SIZE+1][SIZE+1];


int main()	{
	int i=0,T=0;
	for(i=0;i<500;++i)	{
		GX[0][i] = GY[0][i] = GX[i][0] = GY[i][0] = S[0][i] = S[0][i] = 0;
	}
	scanf("%d",&T);
	for(i=0; i<T; ++i)	{
		int R=0,C=0,D=0;
		int x,y;
		scanf("%d%d%d\n",&R,&C,&D);
		for(y=0; y<R; y++)	{
			static char str[510];
			scanf("%s\n",str);
			for(x=0; x<C; ++x)	{
				int cur = M[y][x] = str[x]-'0';
				GX[y+1][x+1] = GX[y+1][x] + GX[y][x+1] - GX[y][x] + cur*(x+1);
				GY[y+1][x+1] = GY[y+1][x] + GY[y][x+1] - GY[y][x] + cur*(y+1);
				S[y+1][x+1] = S[y+1][x] + S[y][x+1] - S[y][x] + cur;
			}
		}
		int K = 0;
		for(y=0; y<R; ++y)	{
			for(x=0; x<R; ++x)	{
				int k = 2;
				for(;;)	{ ++k;
					const int x0 = x - (k>>1), y0 = y - (k>>1);
					const int x1 = x+((k+1)>>1), y1 = y+((k+1)>>1);
					if(x0<0 || y0<0 || x1>C || y1>R) break;
					int s = S[y1][x1] + S[y0][x0] - S[y1][x0] - S[y0][x1];
					s -= M[y0][x0] + M[y0][x1-1] + M[y1-1][x0] + M[y1-1][x1-1];
					const int d = ( (k&1) ? 0:-s );
					// sum of the area
					int gx = GX[y1][x1] + GX[y0][x0] - GX[y0][x1] - GX[y1][x0];
					//0-based gradient of quad
					gx -= x1 * (M[y0][x1-1] + M[y1-1][x1-1]);
					gx -= (x0+1) * (M[y0][x0] + M[y1-1][x0]);
					gx -= s * (x+1);
					//0-based with cut corners
					if(gx+gx!=d) continue;
					int gy = GY[y1][x1] + GY[y0][x0] - GY[y0][x1] - GY[y1][x0];
					gy -= y1 * (M[y1-1][x0] + M[y1-1][x1-1]);
					gy -= (y0+1) * (M[y0][x0] + M[y0][x1-1]);
					gy -= s * (y+1);
					//0-based with cut corners
					if(gy+gy!=d) continue;
					if(k>K) K=k;
				}
			}
		}
		printf("Case #%d: ", i+1);
		if(K>=3)	printf("%d\n",K);
		else		printf("IMPOSSIBLE\n");
	}
	return 0;
}