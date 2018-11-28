#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <cmath>
#include <cstdio>
#include <string.h>
#include <vector>
using namespace std;


int main ()
{
#ifndef ONLINE_JUDGE
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
#endif
		
	int T,N,K;
	scanf("%d",&T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d%d",&N,&K);
		vector<bool> state;
		state.resize(N);
		for (int j = 0; j < N; j++)
			state[j] = false;
		int power = 0;
		for (int j = 0; j < K; j++)
		{
			for (int k = 0; k <= power && k < N; k++)
				state[k] = !state[k];
			power = 0;
			for (int k = 0; k < N; k++)
				if (state[k]) power++; else break;
		}
		printf("Case #%d: %s\n", i + 1, (power == N)?("ON"):("OFF"));
	}

	return 0;
}