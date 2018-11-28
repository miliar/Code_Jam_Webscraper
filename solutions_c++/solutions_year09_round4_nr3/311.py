#include <iostream>
#include <cstring>
#include <climits>

#define INF (INT_MAX/2)
#define MAXN 16
#define MAXK 32

using namespace std;

int bang[MAXN][MAXN];
int input[MAXN][MAXK];
int setok[1<<MAXN];
int pd[1<<MAXN];

int problem(int a, int b, int c, int d)
{
	int up = c-a;
	int down = b-a-d+c;

	if (down < 0) {
		up *= -1;
		down *= -1;
	}

	if (a == c || b == d)
		return 1;

	if (down == 0)
		return 0;
	
	if (up > down)
		return 0;

	if (up < 0)
		return 0;

	return 1;
}

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n, nk;

		scanf("%d %d", &n, &nk);

		for (int i = 0; i < n; i++)
			for (int k = 0; k < nk; k++)
				scanf(" %d", &input[i][k]);
		
		memset(bang, 0, sizeof(bang));
		for (int a = 0; a < n; a++)
			for (int b = a+1; b < n; b++) {
				int ok = 1;

				for (int k = 0; k+1 < nk; k++)
					if (problem(input[a][k], input[a][k+1], input[b][k], input[b][k+1])) {
						ok = 0;
						break;
					}

				bang[a][b] = bang[b][a] = !ok;
			}

		for (int s = 0; s < (1<<n); s++) {
			int ok = 1;

			for (int i = 0; i < n; i++)
				for (int j = i+1; j < n; j++)
					if ((s & (1<<i)) && (s & (1<<j)) && bang[i][j])
						ok = 0;

			setok[s] = ok;
		}
		
		pd[0] = 0;
		for (int s = 1; s < (1<<n); s++) {
			pd[s] = INF;

			for (int s2 = s; s2; s2 = (s2-1)&s)
				if (setok[s2])
					pd[s] = min(pd[s], 1+pd[s-s2]);
		}

		printf("Case #%d: %d\n", t+1, pd[(1<<n)-1]);
	}

	return 0;
}

