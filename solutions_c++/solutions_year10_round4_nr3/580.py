// Bacteria small

#include <stdio.h>
#include <memory.h>

int a[2][101][101];

int go()
{
	int x = 1;
	for(int t=1; ; ++ t)
	{
		int b = 0 ;
		memset(a[x], 0, sizeof(int) * 101 * 101);
		for(int i=1; i<=100; ++i) {
			for(int j=1; j<=100; ++j) {
				if(!a[!x][i-1][j] && !a[!x][i][j-1])
					a[x][i][j] = 0;
				else if(a[!x][i-1][j] && a[!x][i][j-1])
					a[x][i][j] = b = 1;
				else {
					b |= (a[x][i][j] = a[!x][i][j]);
				}
			}
		}/*
		for(int i=1; i<=8; ++i) {
			for(int j=1; j<=8; ++j)
				printf("%d", a[x][i][j]);
			printf("\n");
		}
		printf("\n");*/
		x = !x;
		if(b == 0) return t;
	}
}

int main()
{
	int T, tt;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	scanf("%d", &T);
	for(tt=1; tt<=T; ++tt)
	{
		fprintf(stderr, "%d\n", tt);
		int R;
		scanf("%d", &R);
		memset(a, 0, sizeof(a));
		int x1,y1,x2,y2;

		for(int i=0; i<R; ++i) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int x=x1; x<=x2; ++x) {
				for(int y=y1; y<=y2; ++y)
					a[0][y][x] = 1;
			}
		}

		
		printf("Case #%d: %d\n", tt,go());
	}
	return 0;
}