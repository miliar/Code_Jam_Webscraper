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
int N, K;
char M[128][128];

inline bool isGood(int r, int c, int nr, int nc)
{
	return nr < 1 || nr >= (K<<1) || nc < 1 || nc >= (K<<1) ||
		M[r][c] == M[nr][nc] || M[nr][nc] < '0' || M[nr][nc] > '9';
}

inline bool good(int r, int c, int cr, int cc)
{
	int nr, nc;
	nr = cr + (cr-r);
	nc = cc + (cc-c);
	return isGood(r, c, nr, c) && isGood(r, c, r, nc);
}

inline bool OK(int cr, int cc)
{
	int i, j;
	for(i = 1; i <= K; ++i)
		for(j = K-i+1; j <= K+i-1; j += 2)
			if(!good(i, j, cr, cc)) return false;
	for(i = K+1; i < (K<<1); ++i)
		for(j = i-K+1; j <= 3*K-i-1; j += 2)
			if(!good(i, j, cr, cc)) return false;
	return true;
}

int main()
{
	int i, j, k, m, t, nr, nc;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d", &K);
		gets(M[0]);
		memset(M, ' ', sizeof(M));
		for(i = 1; i < (K<<1); ++i) gets(M[i]+1);
		if(OK(K, K)) nr = nc = K, m = 0;
		else
		{
			for(m = 1; m <= (K<<1); ++m)
			{
				for(i = 0; i < m; ++i)
				{
					if(OK(K-i, K-(m-i)))
					{
						nr = K-i, nc = K-(m-i);
						break;
					}
					if(OK(K-i, K+(m-i)))
					{
						nr = K-i, nc = K+(m-i);
						break;
					}
					if(OK(K+i, K-(m-i)))
					{
						nr = K+i, nc = K-(m-i);
						break;
					}
					if(OK(K+i, K+(m-i)))
					{
						nr = K+i, nc = K+(m-i);
						break;
					}
					if(OK(K-(m-i), K-i))
					{
						nc = K-i, nr = K-(m-i);
						break;
					}
					if(OK(K-(m-i), K+i))
					{
						nc = K+i, nr = K-(m-i);
						break;
					}
					if(OK(K+(m-i), K-i))
					{
						nc = K-i, nr = K+(m-i);
						break;
					}
					if(OK(K+(m-i), K+i))
					{
						nc = K+i, nr = K+(m-i);
						break;
					}
				}
				if(i < m) break;
			}
		}
	//	fprintf(stderr, "%d: m = %d  @ (%d, %d)\n", csK, m, nr, nc);
		printf("Case #%d: %d\n", csK, ((K<<1)+m)*m);
	}
}

