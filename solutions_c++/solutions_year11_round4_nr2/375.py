#include <cstdio>
#include <algorithm>
using namespace std;

int R, C, D;
int M[509][509];

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		//input
		scanf("%d %d %d ", &R, &C, &D);
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
			{
				char c;
				scanf("%c ", &c);
				M[i][j] = D + (c - '0');
			}
		
		//brute force
		int maxK = 0;
		for (int i = 1; i <= R; i++)
			for (int j = 1; j <= C; j++)
				for (int a = i; a <= R; a++)
					for (int b = 1; b <= C; b++)
						if (a - i == b - j)
						{
							//printf("[%d;%d] - [%d;%d]\n", i, j, a, b);
							
							int M0 = 0; //mass
							int Mx = 0; //moment of inertia x
							int My = 0; //moment of inertia y
							for (int x = i; x <= a; x++)
								for (int y = j; y <= b; y++)
								{
									//eliminate
									if (((x == i) || (x == a)) && ((y == j) || (y == b)))
										continue;
									
									M0 += M[x][y];
									Mx += x * M[x][y];
									My += y * M[x][y];
								}
								
							//check
							if ((M0 * (i + a) == 2 * Mx) && (M0 * (j + b) == 2 * My))
								maxK = max(maxK, a - i + 1);
						}
		
		//output
		printf("Case #%d: ", Ti);
		if (maxK < 3)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", maxK);
	}
	return 0;
}