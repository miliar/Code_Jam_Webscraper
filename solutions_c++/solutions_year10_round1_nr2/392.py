#include <cstdio>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <cassert>
using namespace std;
#define PB push_back
#define LL long long
#define ULL unsigned LL
#define LD long double

const int inf = 1000000000;
#define MR 110
#define MS 300
int D, I, M, N, a[MR], dp[MR][MS];

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for(int c = 0; c < tests; c++)
	{
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for(int i = 0; i < N; i++)
			scanf("%d", &a[i]);
		//wypelnij calosc inf
		for(int i = 0; i < N; i++)
			for(int j = 0; j < 256; j++)
				dp[i][j] = inf;
		//wypelnij pierwsza kolumne
		for(int i = 0; i < 256; i++)
			dp[0][i] = abs(a[0] - i);
		for(int i = 1; i < N; i++)	//po pozycjach
		{
			//usun pixel			
			for(int j = 0; j < 256; j++)
				dp[i][j] = min(dp[i][j], dp[i-1][j] + D);
			//wstaw pixel - jesli M > 0
			if(M)
				for(int j = 0; j < 256; j++)
				{
					int ile = abs(j - a[i]) / M;	//ile symboli trzeba wstawic
					if(!(abs(j - a[i]) % M))
						ile--;
					if(ile < 0)
						ile = 0;				
					dp[i][a[i]] = min(dp[i][a[i]], dp[i-1][j] + ile * I);
				}
			//zmien wartosc
			for(int j = 0; j < 256; j++)
			{				
				int pom = abs(j - a[i]);	//tyle kosztuje nas podmiana
				//if(j == 125)
				//	printf("%d\n", pom);
				for(int l = 0; l < 256; l++)
					if(abs(l - j) <= M)
						dp[i][j] = min(dp[i][j], pom + dp[i-1][l]);
			}
		}		
		int val = dp[N-1][0];
		for(int i = 1; i < 256; i++)
			val = min(val, dp[N-1][i]);
		printf("Case #%d: %d\n", c+1, val);
	}
	return 0;
}