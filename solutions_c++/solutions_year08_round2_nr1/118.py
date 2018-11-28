#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<long long, long long> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))

int tc, n, A, B, C, D, x0, y0, M;
long long ans;
long long tab[3][3];

int main()
{
	int t, i,j,k, i1, j1, k1;
	long long x, y, z;
	scanf("%d", &tc);
	FOR(t, tc)
	{
		ans = 0;
		scanf("%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		for (i = 0; i < 3; i++)for (j = 0; j < 3; j++) tab[i][j] = 0LL;
		x = x0; y = y0; tab[x0 % 3][y0 % 3]++; 
//			printf("%d %d\n", x % 3, y % 3);
		for (i = 0; i < n - 1; i++)
		{
			x = (A * x + B) % ((long long ) M);
			y = (C * y + D) % ((long long) M);
			tab[x%3][y%3]++;
//			printf("%lld %lld\n", x % 3, y % 3);
		}
//		for (i = 0; i < 3; i++) for (j = 0; j < 3; j++)  fprintf(stderr, "tab[%d][%d] = %d\n", i, j, tab[i][j]);
		
		for (i = 0; i < 9; i++)
			for (j = i; j < 9; j++)
				for (k = j; k < 9; k++)
				{
					if (i == j && j == k)
					{
//						fprintf(stderr, "h1 ");
						z = tab[(i/3)][(i%3)] * (tab[(i/3)][(i%3)] - 1) * (tab[(i/3)][(i%3)] - 2) / 6;
						ans += z;
//						fprintf(stderr, "%d %d %d ", i, j, k);
//						fprintf(stderr, "%d,%d %d,%d %d,%d %lld\n", i/3, i%3, j/3,j%3, k/3, k%3, z);
					}
					else if (((i / 3) + (j / 3) + (k / 3)) % 3 == 0 &&
							     ((i % 3) + (j % 3) + (k % 3)) % 3 == 0)
					{
//						fprintf(stderr, "h2 ");
						z = tab[(i/3)][(i%3)] * tab[(j/3)][(j%3)] * tab[(k/3)][(k%3)]; 
						ans += z;
//						fprintf(stderr, "%d %d %d ", i, j, k);
//						fprintf(stderr, "%d,%d %d,%d %d,%d %lld\n", i/3, i%3, j/3,j%3, k/3, k%3, z);
					}
				}
		
		fprintf(stderr, "running %d\n", t + 1);
		printf("Case #%d: %lld\n", t + 1, ans);
	}
	return 0;
}

