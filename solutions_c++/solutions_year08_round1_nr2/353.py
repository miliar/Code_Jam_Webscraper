#include <iostream>
#include <cstdio>
using namespace std;

int pref[100][100];

int main()
{
	int	T,cs;
	int	N,M;
	int	i,j;

	scanf("%d",&T);

	for(cs = 1; cs <= T; cs++)
	{
		scanf("%d",&N);
		scanf("%d",&M);

		for(i = 0; i < M; i++) for(j = 0; j < N; j++) pref[i][j] = 0;

		for(i = 0; i < M; i++)
		{
			int	t;
			int	s,m;

			scanf("%d",&t);

			while(t--)
			{
				scanf("%d %d",&s,&m);
				
				s--;
				pref[i][s] |= (1 <<m);
			}
		}

//		for(i = 0; i < M; i++) printf("%x\n",pref[i]);

		bool	flag[100];

		int	flg,sol = -1,sc = -1;

		for(flg = 0; flg < (1 << N); flg++)
		{
			for(i = 0; i < M; i++) flag[i] = false;

			for(i = 0; i < M; i++)
			{
				for(j = 0; j < N; j++)
				{
					if(pref[i][j] != 0)
					{
						if((pref[i][j] & 1) && !(flg & (1 << j)))
							break;
						if((pref[i][j] & 2) && (flg & (1 << j)))
							break;
					}
				}

				if(j < N) flag[i] = true;
			}

			for(i = 0; i < M; i++)
				if(!flag[i]) break;
			if(i >= M)
			{
				int	c = 0,x = flg;

//				printf("sol: %d\n",flg);

				while(x)
				{
					x >>= 1;
					c++;
				}

				if(sc == -1 || c < sc)
				{
					sol = flg;
					sc = c;
				}
			}
		}

		printf("Case #%d:",cs);

		if(sc == -1)
			printf(" IMPOSSIBLE");
		else
			for(i = 0; i < N; i++) printf(" %d",(sol & (1 << i)) ? 1 : 0);
		printf("\n");
	}

	return 0;
}
