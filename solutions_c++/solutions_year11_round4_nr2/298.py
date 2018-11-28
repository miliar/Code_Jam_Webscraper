#include <iostream>
#include <cstdio>
#include <complex>

#define MAXS 513

using namespace std;

typedef complex<int> vec;

int weight[MAXS][MAXS];
int wsum[MAXS][MAXS];
vec dsum[MAXS][MAXS];
vec delta[MAXS][MAXS];

int main()
{
	int T;
	
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		int R, C, D;

		scanf("%d %d %d", &R, &C, &D);
		
		for (int y = 0; y < R; y++)
			for (int x = 0; x < C; x++) {
				char c;
				scanf(" %c", &c);
				weight[y][x] = c-'0';
				wsum[y][x] = weight[y][x];
				if (y-1 >= 0)
					wsum[y][x] += wsum[y-1][x];
				if (x-1 >= 0)
					wsum[y][x] += wsum[y][x-1];
				if (y-1 >= 0 && x-1 >= 0)
					wsum[y][x] -= wsum[y-1][x-1];

				delta[y][x] = vec(y, x) * weight[y][x];
				dsum[y][x] = delta[y][x];
				if (y-1 >= 0)
					dsum[y][x] += dsum[y-1][x];
				if (x-1 >= 0)
					dsum[y][x] += dsum[y][x-1];
				if (y-1 >= 0 && x-1 >= 0)
					dsum[y][x] -= dsum[y-1][x-1];
			}
		
		int ret = -1;
		for (int k = min(R,C); k >= 3; k--) {
			int ok = 0;
			for (int y = 0; y+k-1 < R && !ok; y++)
				for (int x = 0; x+k-1 < C && !ok; x++) {
					int y2 = y+k-1, x2 = x+k-1;

					int ws = wsum[y2][x2];
					if (y-1 >= 0)
						ws -= wsum[y-1][x2];
					if (x-1 >= 0)
						ws -= wsum[y2][x-1];
					if (y-1 >= 0 && x-1 >= 0)
						ws += wsum[y-1][x-1];

					ws -= weight[y][x] + weight[y2][x] + weight[y][x2] + weight[y2][x2];

					vec ve = dsum[y2][x2];
					if (y-1 >= 0)
						ve -= dsum[y-1][x2];
					if (x-1 >= 0)
						ve -= dsum[y2][x-1];
					if (y-1 >= 0 && x-1 >= 0)
						ve += dsum[y-1][x-1];

					ve -= delta[y][x] + delta[y2][x] + delta[y][x2] + delta[y2][x2];

					if (2*ve == ws*vec(y+y2, x+x2))
						ok = 1;
				}
			if (ok) {
				ret = k;
				break;
			}
		}

		printf("Case #%d: ", t+1);
		if (ret != -1)
			printf("%d", ret);
		else
			printf("IMPOSSIBLE");
		printf("\n");
	}

	return 0;
}
