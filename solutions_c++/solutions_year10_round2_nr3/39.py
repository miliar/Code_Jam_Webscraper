#include <stdio.h>
int C[505][505];
int D[505][505];
int S[505];
const int MOD = 100003;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	for (int q=0;q<=500;++q) for (int w=0;w<=q;++w)
	{
		if (w==0 || w==q) C[q][w] = 1;
		else C[q][w] = (C[q-1][w-1]+C[q-1][w]) % MOD;
	}
	for (int l=1;l<=500;++l) for (int x=2;x<=500;++x)
	{
		//assumption:
		//(1) l + 1 <= x
		//(2) D[1,x] = 1
		if (l + 1 > x) continue;
		if (l == 1) D[l][x] = 1; 
		else
		{
			for (int s=1;;++s)
			{
				if (s + 1 > l) break;
				//D[l][x] += D[s][l] * C[x-l-1][l-s-1]
				D[l][x] += long long(D[s][l]) * C[x-l-1][l-s-1] % MOD;
				D[l][x] %= MOD;
			}
		}
		S[x] += D[l][x];
		S[x] %= MOD;
	}
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int N;
		scanf("%d",&N);
		printf("Case #%d: %d\n",kase,S[N]);
	}
	
	return 0;
}