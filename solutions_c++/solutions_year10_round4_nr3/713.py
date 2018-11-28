#include<cstdio>
#include<cstring>

int main()
{
	int T,R,A,B,C,D;
	scanf("%d\n",&T);
	char X[105][105];
	char Y[105][105];
	
	for(int ii = 1; ii <= T;++ii)
	{
		scanf("%d\n",&R);
		memset(X,0,sizeof(X));
		for(int i = 0;i < R;++i)
		{
			scanf("%d %d %d %d\n",&A,&B,&C,&D);
			for(int j = A;j <= C;++j) for(int k = B;k <= D;++k) X[j][k] = 1;
		}

		int s = 0;
		int c = 1;
		while(c > 0)
		{
			s++;
			c = 0;
			memcpy(Y,X,sizeof(X));

			for(int i = 1; i <= 100;++i) for(int j = 1;j<= 100;++j)
			{
				if(X[i][j] == 1)
				{
					if(X[i-1][j] == 0 && X[i][j-1] == 0) Y[i][j] = 0;
					else
					{
						Y[i][j] = 1;
						c++;
					}
				}
				else
				{
					if(X[i-1][j] == 1 && X[i][j-1] == 1)
					{
						Y[i][j] = 1;
						c++;
					}
				}
			}
			memcpy(X,Y,sizeof(X));
		}

		printf("Case #%d: %d\n",ii,s);
	}

	return 0;
}
