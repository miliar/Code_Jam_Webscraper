#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

#define BASE 10009

int csK, csN, N, K, cntM[128][32], cnt[32], ans[16];
char S[128], M[128][64];

inline int eval()
{
	int sum = 0, i, t = 1;
	for(i = 0; S[i] != '\0'; ++i)
	{
		if(S[i] == '+')
		{
			sum += t;
			t = 1;
		}
		else t = (t*cnt[S[i]-'a']) % BASE;
	}
	sum += t;
	return sum;
}

inline void DFS(int x)
{
	ans[x] = (ans[x]+eval()) % BASE;
	if(x == K) return;
	int i, j;
	for(i = 0; i < N; ++i)
	{
		for(j = 0; j < 26; ++j)
			cnt[j] += cntM[i][j];
		DFS(x+1);
		for(j = 0; j < 26; ++j)
			cnt[j] -= cntM[i][j];
	}
}

int main()
{
	int i, j, k, m, t;
	char perm[128];
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%s %d %d", S, &K, &N);
		memset(cntM, 0, sizeof(cntM));
		for(i = 0; i < N; ++i)
		{
			scanf("%s", M[i]);
			for(j = 0; M[i][j] != '\0'; ++j)
				cntM[i][M[i][j]-'a']++;
		}
		for(i = 0; i <= K; ++i) ans[i] = 0;
		DFS(0);
		printf("Case #%d:", csK);
		for(i = 1; i <= K; ++i)
			printf(" %d", ans[i]);
		printf("\n");
	}
}
