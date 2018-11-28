#include<cstdio>

int main()
{
	int C,N,K,B,T;
	int X[105],V[105];
	scanf("%d\n",&C);
	for(int ii = 1;ii <= C;++ii)
	{
		scanf("%d %d %d %d\n",&N,&K,&B,&T);
		for(int i =0; i < N;++i) scanf("%d ",X+i);
		for(int i =0; i < N;++i) scanf("%d ",V+i);

		bool M[55];
		for(int i = 0;i < N;++i) M[i] = false;

		int s = 0, cc =0;
		for(int i = N-1;i >= 0 && cc < K;--i)
		{
			if(B-X[i] <= V[i]*T)
			{
				for(int j = i+1;j < N;++j) if(!M[j]) s++;
				M[i] = true;
				cc++;
			}
		}

		if(cc == K) printf("Case #%d: %d\n",ii,s);
		else        printf("Case #%d: IMPOSSIBLE\n",ii);
	}
	return 0;
}
