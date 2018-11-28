#include<cstdio>
#include<cstring>

const int RMAX(50);
const int CMAX(50);

char map[RMAX+2][CMAX+2];

int x_move[4]={0,1,0,1};
int y_move[4]={0,0,1,1};
char tile[4] ={'/','\\','\\','/'};

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int nTest;
	scanf("%d",&nTest);
	for(int test=1; test<=nTest;test++)
	{
		int r,c;
		scanf("%d %d",&r,&c);
		for(int i=1;i<=r;i++)
			scanf("%s",map[i]+1);

		bool flag(true);

		for(int i=1;i<=r & flag;i++)
		{
			for(int j=1;j<=c & flag;j++)
			{
				if(map[i][j]=='#')
				{
					for(int k=0;k<4 & flag;k++)
					{
						if(map[i+y_move[k]][j+x_move[k]]=='#')
							map[i+y_move[k]][j+x_move[k]] = tile[k];
						else
							flag = false;
					}
				}
			}
		}

		printf("Case #%d:\n",test);
		if(flag)
		{
			for(int i=1;i<=r;i++)
			{
				for(int j=1;j<=c;j++)
				{
					printf("%c",map[i][j]);
				}
				printf("\n");
			}
		}
		else
			printf("Impossible\n");
	}
	return 0;
}