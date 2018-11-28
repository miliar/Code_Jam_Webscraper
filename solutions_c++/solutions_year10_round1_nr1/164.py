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
char M[64][64], R[64][64], R4, B4;
char msg[4][16] = {"Neither", "Red", "Blue", "Both"};

inline bool checkWin(int r, int c)
{
	int i;
	char z = R[r][c];
	if(r+K <= N)
	{
		for(i = 1; i < K; ++i)
			if(R[r+i][c] != z) break;
		if(i == K) return true;
	}
	if(c+K <= N)
	{
		for(i = 1; i < K; ++i)
			if(R[r][c+i] != z) break;
		if(i == K) return true;
	}
	if(r+K <= N && c+K <= N)
	{
		for(i = 1; i < K; ++i)
			if(R[r+i][c+i] != z) break;
		if(i == K) return true;
	}
	if(r+K <= N && c >= K-1)
	{
		for(i = 1; i < K; ++i)
			if(R[r+i][c-i] != z) break;
		if(i == K) return true;
	}
	return false;
}

int main()
{
	int i, j, k, m, t;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d", &N, &K);
		for(i = 0; i < N; ++i)
			scanf("%s", M[i]);
		for(i = 0; i < N; ++i)
			for(j = 0; j < N; ++j)
				R[j][N-i-1] = M[i][j];
		for(j = 0; j < N; ++j)
		{
			t = 0;
			for(i = N-1; i >= 0; --i)
				if(R[i][j] == '.') ++t;
				else if(t > 0)
					R[i+t][j] = R[i][j], R[i][j] = '.';
		}
		R4 = B4 = 0;
		for(i = 0; i < N && (R4==0||B4==0); ++i)
		{
			for(j = 0; j < N; ++j)
				if(R[i][j] == '.') continue;
				else if(checkWin(i, j))
				{
					if(R[i][j] == 'R') R4 = 1;
					else B4 = 2;
				}
		}
		printf("Case #%d: %s\n", csK, msg[B4|R4]);
	}
}

