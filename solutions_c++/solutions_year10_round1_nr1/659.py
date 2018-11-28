#include <cstdio>

char board[50][51], rotated[50][51];
int ntest, bsize, ninarow;

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		scanf("%d %d", &bsize, &ninarow);
		for(int i = 0;i < bsize;++i)
			scanf("%s", board[i]);
		for(int i = 0;i < bsize;++i)
		{
			for(int j = 0;j < bsize;++j)
				rotated[i][j] = board[bsize - j - 1][i];
			rotated[i][bsize] = 0;
		}
		for(int j = 0;j < bsize;++j)
			for(int i = bsize - 1;i >= 0;--i)
				if(rotated[i][j] == '.')
				{
					int k = i - 1;
					for(;k >= 0 && rotated[k][j] == '.';--k);
					if(k >= 0)
					{
						char temp = rotated[i][j];
						rotated[i][j] = rotated[k][j];
						rotated[k][j] = temp;
					}
				}
		//for(int i = 0;i < bsize;++i)
		//	printf("%s\n", rotated[i]);
		int res = 0;
		for(int i = 0;i < bsize;++i)
			for(int j = 0;j < bsize;++j)
				if(rotated[i][j] == 'B')
				{
					int nblue = 0;
					for(int k = i;k < bsize && nblue < ninarow && rotated[k][j] == 'B';++k)
						++nblue;
					res |= (nblue == ninarow);
					//printf("b B %d %d %d\n", i, j, nblue);
					nblue = 0;
					for(int l = j;l < bsize && nblue < ninarow && rotated[i][l] == 'B';++l)
						++nblue;
					res |= (nblue == ninarow);
					//printf("ka B %d %d %d\n", i, j, nblue);
					nblue = 0;
					for(int k = i, l = j;k < bsize && l < bsize && nblue < ninarow && rotated[k][l] == 'B';++k, ++l)
						++nblue;
					res |= (nblue == ninarow);
					//printf("kab B %d %d %d\n", i, j, nblue);
					nblue = 0;
					for(int k = i, l = j;k < bsize && l >= 0 && nblue < ninarow && rotated[k][l] == 'B';++k, --l)
						++nblue;
					res |= (nblue == ninarow);
					//printf("kib B %d %d %d\n", i, j, nblue);
				}
				else if(rotated[i][j] == 'R')
				{
					int nblue = 0;
					for(int k = i;k < bsize && nblue < ninarow && rotated[k][j] == 'R';++k)
						++nblue;
					res |= 2*(nblue == ninarow);
					//printf("b B %d %d %d\n", i, j, nblue);
					nblue = 0;
					for(int l = j;l < bsize && nblue < ninarow && rotated[i][l] == 'R';++l)
						++nblue;
					res |= 2*(nblue == ninarow);
					//printf("ka B %d %d %d\n", i, j, nblue);
					nblue = 0;
					for(int k = i, l = j;k < bsize && l < bsize && nblue < ninarow && rotated[k][l] == 'R';++k, ++l)
						++nblue;
					res |= 2*(nblue == ninarow);
					//printf("kab B %d %d %d\n", i, j, nblue);
					nblue = 0;
					for(int k = i, l = j;k < bsize && l >= 0 && nblue < ninarow && rotated[k][l] == 'R';++k, --l)
						++nblue;
					res |= 2*(nblue == ninarow);
				}
		printf("Case #%d: ", test);
		switch(res)
		{
			case 0 : printf("Neither\n");break;
			case 1 : printf("Blue\n");break;
			case 2 : printf("Red\n");break;
			case 3 : printf("Both\n");
		}
	}
}
