#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<algorithm>
using namespace std;

#define IN 1
#define OUT 0

int csK, csN, N, K;
int price[128][32];
char valid[128][128];
int adj[256][256], nAdj[256];
char ok[256], used[256];
int match[256], ans;

inline int getIndex(int pos, int d)
{
	return (pos<<1) | d;
}

bool findAugment(int x)
{
	used[x] = 1;
	for(int i = 0; i < nAdj[x]; ++i)
	{
		if(match[adj[x][i]] == -1 ||
				(!used[match[adj[x][i]]] && findAugment(match[adj[x][i]])))
		{
			match[adj[x][i]] = x;
			match[x] = adj[x][i];
			return 1;
		}
	}
	return 0;
}

int main()
{
	int i, j, k, m, t;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d", &N, &K);
		for(i = 0; i < N; ++i)
		{
			for(j = 0; j < K; ++j)
				scanf("%d", &price[i][j]);
			for(j = 0; j < N; ++j)
				valid[i][j] = 0;
			nAdj[getIndex(i, IN)] = nAdj[getIndex(i, OUT)] = 0;
		}
		for(i = 0; i < N; ++i)
			for(j = 0; j < N; ++j)
			{
				for(k = 0; k < K; ++k)
					if(price[i][k] >= price[j][k]) break;
				if(k == K)
					valid[i][j] = 1;
			}
		for(i = 0; i < N; ++i)
		{
			m = getIndex(i, OUT);
			t = getIndex(i, IN);
			match[m] = match[t] = -1;
			for(j = 0; j < N; ++j)
				if(valid[i][j])
					adj[t][nAdj[t]++] = getIndex(j, OUT);
		}
		ans = 0;
		for(i = 0; i < N; ++i)
		{
			t = getIndex(i, IN);
			if(match[t] == -1)
			{
				memset(used, 0, sizeof(used));
				if(findAugment(t)) ++ans;
			}
		}
		printf("Case #%d: %d\n", csK, N-ans);
	}
}

