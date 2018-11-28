#include <stdio.h>
int N,M,A;
int x0,y0,x1,y1,x2,y2;
int calc(void)
{
	x0 = y0 = 0;
	for (x1 = 0;x1 <= N;x1++) for (y2 = 0;y2 <= M;y2++) for (x2 = 0;x2 <= N;x2++)
	{
		if (x2 == 0) {y1 == 1;} else {y1 = (A + x1 * y2) / x2;}
		if (y1 <= M && x2 * y1 - x1 * y2 == A) return 0;
	}
	return -1;
}
int main(void)
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int C;
	scanf("%d",&C);
	for (int cases = 1;cases <= C;cases++)
	{
		scanf("%d%d%d",&N,&M,&A);
		int sol = calc();
		printf("Case #%d: ",cases);
		if (sol == -1) {printf("IMPOSSIBLE\n");} else {printf("%d %d %d %d %d %d\n",x0,y0,x1,y1,x2,y2);}
	}
	return 0;
}
