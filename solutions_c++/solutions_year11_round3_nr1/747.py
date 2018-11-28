#include<stdio.h>

using namespace std;

int floor[50][50];
int R,C;

bool checkReplace(int x,int y)
{
	if(x == R-1 || y == C-1)
		return false;
	if(floor[x+1][y+1] == 1 && floor[x+1][y] == 1 && floor[x][y+1] == 1)
		return true;
	return false;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d %d",&R,&C);
		for(int i=0;i<R;i++)
		{
			char temp[100];
			scanf("%s",temp);
			for(int j=0;j<C;j++)
			{
				if(temp[j] == '.')
					floor[i][j] = 0;
				else if(temp[j] == '#')
					floor[i][j] = 1;
			}
		}
		bool out = false;
		for(int i=0;!out && i<R;i++)
			for(int j=0;!out && j<C;j++)
			{
				if(floor[i][j] == 1)
				{
					if(checkReplace(i,j))
					{
						floor[i][j] = floor[i+1][j+1] = 2;
						floor[i+1][j] = floor[i][j+1] = 3;
					}
					else
						out = true;
				}
			}
		printf("Case #%d:\n",t);
		if(out)
			printf("Impossible\n");
		else
		{
			for(int i=0;i<R;printf("\n"),i++)
				for(int j=0;j<C;j++)
				{
					if(floor[i][j] == 0)
						printf(".");
					else if(floor[i][j] == 2)
						printf("/");
					else if(floor[i][j] == 3)
						printf("\\");
				}
		}
		
	}
	return 0;
}
