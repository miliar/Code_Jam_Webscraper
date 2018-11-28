#include <cstdio>



char game[4][10];


bool won(char symbole)
{
	for(int l = 0; l < 4; l++)
	{
		for(int c = 0; c < 4; c++)
		{
			if(game[l][c] != symbole && game[l][c] != 'T')
				break;
			if( c==3)
				return true;
		}
	
	}
	for(int c = 0; c < 4; c++)
	{
		for(int l = 0; l < 4; l++)
		{
			if(game[l][c] != symbole && game[l][c] != 'T')
				break;
			if(l==3)
				return true;
		}
	
	}
	for(int i = 0; i < 4; i++)
	{
		if(game[i][i] != symbole && game[i][i] != 'T')
			break;
		if(i==3)
			return true;
	}
	for(int i = 0; i < 4; i++)
	{
		if(game[i][3-i] != symbole && game[i][3-i] != 'T')
			break;
		if(i==3)
			return true;
	}
	return false;
}

bool not_finished()
{
	for(int i =0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(game[i][j] == '.')
				return true;
	return false;
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int g = 0; g < n; g++)
	{
		for(int i = 0; i < 4; i++)
			scanf("%s", game[i]);
		scanf("\n");
		printf("Case #%d: ", g+1);
		if(won('X'))
		{
			printf("X won");
		}
		else if(won('O'))
			printf("O won", g+1);
		else if(not_finished())
			printf("Game has not completed");
		else printf("Draw");
		printf("\n");
	}
	return 0;
}
