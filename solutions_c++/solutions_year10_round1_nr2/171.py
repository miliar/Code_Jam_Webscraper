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
int D, I, M, N, A[128], iCost[256];
int dp[128][256];
char noI;

inline int myAbs(int x)
{
	return x<0 ? -x : x;
}

int main()
{
	int i, j, k, m, t;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d %d %d", &D, &I, &M, &N);
		for(i = 0; i < N; ++i)
			scanf("%d", &A[i]);
		
		iCost[0] = 0;
		noI = 0;
		for(i = 1; i < 256; ++i)
			if(M > 0) iCost[i] = I * ((i+M-1)/M);
			else iCost[i] = -1, noI = 1;

		for(i = 0; i < 256; ++i)
			dp[0][i] = myAbs(A[0]-i);
		for(i = A[0]+1; i < 256; ++i)
			if(i-A[0] <= M && dp[0][i] > I) dp[0][i] = I;
			else if(i-A[0] > M && dp[0][i] > dp[0][i-M]+I)
				dp[0][i] = dp[0][i-M]+I;
		for(i = A[0]-1; i >= 0; --i)
			if(A[0]-i <= M && dp[0][i] > I) dp[0][i] = I;
			else if(A[0]-i > M && dp[0][i] > dp[0][i+M]+I)
				dp[0][i] = dp[0][i+M]+I;
		for(i = 0; i < 256; ++i)
			if(dp[0][i] > D) dp[0][i] = D;
		
		for(i = 1; i < N; ++i)
		{
			for(j = 0; j < 256; ++j)
			{
				dp[i][j] = dp[i-1][j] + D;
				m = -1;
				for(k = max(0, j-M); k <= min(255, j+M); ++k)
					if(m == -1 || dp[i-1][k] < m)
						m = dp[i-1][k];
				if(m+myAbs(j-A[i]) < dp[i][j])
					dp[i][j] = m + myAbs(j-A[i]);
			}
			if(noI == 0)
			{
				for(j = 0; j < 256; ++j)
					for(k = j+1; k < 256; ++k)
					{
						if(dp[i][k] > dp[i][j]+iCost[k-j])
							dp[i][k] = dp[i][j]+iCost[k-j];
						if(dp[i][j] > dp[i][k]+iCost[k-j])
							dp[i][j] = dp[i][k]+iCost[k-j];
					}
			}
		}
/*		for(i = 0; i < 256; ++i)
		{
			for(j = 0; j < N; ++j)
				fprintf(stderr, "%8d", dp[j][i]);
			fprintf(stderr, "\n");
		}
		for(i = 0; i < N; ++i)
		{
			for(j = 0; j < 10; ++j)
				fprintf(stderr, "%8d", dp[i][j]);
			fprintf(stderr, "\n");
		}*/
		m = dp[N-1][0];
		for(i = 1; i < 256; ++i)
			if(dp[N-1][i] < m) m = dp[N-1][i];
		printf("Case #%d: %d\n", csK, m);
	}
}

