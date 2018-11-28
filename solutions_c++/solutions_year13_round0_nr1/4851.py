#include<cstdio>
using namespace std;
#define MAXN 4

int T;
int G[MAXN][MAXN];
int N=4;

bool check_t(int x0,int y0,int dx,int dy,int f)
{
	for (int k=0;k<N;k++)
	{
		if ((G[x0+dx*k][y0+dy*k] & f) == 0)
			return 0;
	}
	return 1;
}

bool check(int f)
{
	int i;
	for (i=0;i<4;i++)
		if (check_t(i,0,0,1,f) || check_t(0,i,1,0,f))
			return 1;
	return check_t(0,0,1,1,f) || check_t(N-1,0,-1,1,f);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j;
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		for (i=0;i<N;i++)
		{
			char str[5];
			scanf("%s",str);
			for (j=0;j<N;j++)
			{
				if (str[j] == 'X')
					G[i][j] = 1;
				if (str[j] == 'O')
					G[i][j] = 2;
				if (str[j] == '.')
					G[i][j] = 0;
				if (str[j] == 'T')
					G[i][j] = 3;
			}
		}
		printf("Case #%d: ",cases);
		if (check(1))
			printf("X won");
		else if (check(2))
			printf("O won");
		else 
		{
			for (i=0;i<N;i++)
				for (j=0;j<N;j++)
					if (G[i][j] == 0)
					{
						printf("Game has not completed");
						goto HERE;
					}
		HERE:
			if (i == N)
				printf("Draw");
		}
	
	
		printf("\n");
	}
	return 0;
}
