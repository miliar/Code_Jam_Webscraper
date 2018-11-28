#include <stdio.h>

bool didWon(char a, char b, char c, char d, char &won)
{
	if(a=='.'||b=='.'||c=='.'||d=='.') return false;
	if(a=='T')
	{
		won=b;
		return b==c&&c==d;
	}
	if(b=='T')
	{
		won=b;
		return a==c&&c==d;
	}
	if(c=='T')
	{
		won=b;
		return b==a&&a==d;
	}
	if(d=='T')
	{
		won=b;
		return b==c&&c==a;
	}

	{
		won=b;
		return b==c&&c==a&&a==d;
	}
}
int main(int argc, char const *argv[])
{
	int t;
	char array[5][5];
	int isOver;
	int isWon;
	char whoWon;
	scanf("%d",&t);
	for(int k=1; k<=t;k++)
	{
		isOver=true;
		isWon = false;
		for (int i = 0; i < 4; ++i)
		{
			
				scanf("%s",array[i]);
			for (int j = 0; j < 4; ++j)
			{
				if(array[i][j]=='.') isOver=false;
			}
		}
		
		for (int i = 0; i < 4; ++i)
		{
			if(didWon(array[i][0],array[i][1],array[i][2],array[i][3],whoWon))
			{
				isWon=true;
				break;
			}
				
		}
		for (int i = 0; i < 4 && !isWon; ++i)
		{
			if(didWon(array[0][i],array[1][i],array[2][i],array[3][i],whoWon))
			{
				isWon=true;
				break;
			}
		}
		if(!isWon && didWon(array[0][0],array[1][1],array[2][2],array[3][3],whoWon))
			isWon=true;
		if(!isWon && didWon(array[0][3],array[1][2],array[2][1],array[3][0],whoWon))
			isWon=true;
		printf("Case #%d: ",k);
		if(isWon)
		{
			printf("%c won\n", whoWon);
		}
		else if(isOver)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}	
	}
	return 0;
}
