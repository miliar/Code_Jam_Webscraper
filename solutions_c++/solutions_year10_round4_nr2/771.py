#include<cstdio>

int min(int a,int b)
{
	if(a < b) return a;
	return b;
}

int max(int a,int b)
{
	if(a > b) return a;
	return b;
}

int main()
{
	int T;
	scanf("%d\n",&T);
	
	int P, M[2000], C[12][1000];
	for(int ii = 1; ii <= T;++ii)
	{
		scanf("%d\n",&P);
		for(int i = 0; i < (1 << P);++i) scanf("%d ", M + i);
		for(int i = P-1;i >= 0;--i)
			for(int j = 0;j < (1 << i);++j) scanf("%d ", C[i] + j);

		int s = 0;
		for(int i = P;i > 0;--i)
		{
			for(int j = 0;j < (1 << i);j+= 2)
			{
				if(M[j] == 0 || M[j+1] == 0) s++;
				M[j/2] = max(0,min(M[j]-1,M[j+1]-1));
			}
		}

		printf("Case #%d: %d\n",ii,s * C[0][0]);
	}

	return 0;
}
