#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

int csK, csN;
int N, K, ans, R, C;
char M[128][128], M2[128][128];

inline bool has1()
{
	int i, j;
	for(i = 0; i <= R; ++i)
		for(j = 0; j <= C; ++j)
			if(M[i][j]) return true;
	return false;
}

int main()
{
	int i, j, k, m, t;
	int x1, x2, y1, y2;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d", &N);
		memset(M, 0, sizeof(M));
		R = C = 0;
		for(i = 0; i < N; ++i)
		{
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			if(y2 > R) R = y2;
			if(x2 > C) C = x2;
			for(j = y1; j <= y2; ++j)
				for(k = x1; k <= x2; ++k)
					M[j][k] = 1;
		}
		for(ans = 0; has1(); ++ans)
		{
			memset(M2, 0, sizeof(M2));
			for(i = 1; i <= R; ++i)
				for(j = 1; j <= C; ++j)
					M2[i][j] = (M[i][j] && (M[i-1][j] || M[i][j-1])) ||
						(M[i-1][j] && M[i][j-1]);
			memcpy(M, M2, sizeof(M2));
		}
		printf("Case #%d: %d\n", csK, ans);
	}
}

