#include<stdio.h>
#include<string.h>

char win, board[4][4];

int checkOwin();
int checkXwin();
int checkDraw();

int main()
{
	char c;
	int i,j,T,t=1,a,b;
	scanf("%d",&T);
	while(t<=T)
	{
		scanf("%c",&c);
		a=b=-1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%c",&board[i][j]);
				if(board[i][j]=='T')
				{
					a=i;
					b=j;
				}
			}
			scanf("%c",&c);
		}

		if(a!=-1 && b!=-1)
			board[a][b]='O';

		if(checkOwin()<0)
		{
			if(a!=-1 && b!=-1)
				board[a][b]='X';
			if(checkXwin()<0)
				if(checkDraw()<0)
					win='I';
		}



		char msg[120];
		switch(win)
		{
			case 'O': strcpy(msg,"O won\n");
				  break;
			case 'X': strcpy(msg,"X won\n");
				  break;
			case 'D': strcpy(msg,"Draw\n");
				  break;
			case 'I': strcpy(msg,"Game has not completed\n");
				  break;
		}
		printf("Case #%d: %s",t,msg);

		t++;
	}
	return 0;
}

int checkOwin()
{
	int i,j;
	for(i=0;i<4;i++)
		if(board[i][0]==board[i][1] && board[i][1]==board[i][2] && board[i][2]==board[i][3] && board[i][3]=='O')
		{
			win='O';
			return 1;
		}
	for(i=0;i<4;i++)
		if(board[0][i]==board[1][i] && board[1][i]==board[2][i] && board[2][i]==board[3][i] && board[3][i]=='O')
		{
			win='O';
			return 1;
		}
	if(board[0][0]==board[1][1] && board[1][1]==board[2][2] && board[2][2]==board[3][3] && board[3][3]=='O')
	{
		win='O';
		return 1;
	}
	if(board[3][0]==board[2][1] && board[2][1]==board[1][2] && board[1][2]==board[0][3] && board[0][3]=='O')
	{
		win='O';
		return 1;
	}
		return -1;
}

int checkXwin()
{
	int i,j;
	for(i=0;i<4;i++)
		if(board[i][0]==board[i][1] && board[i][1]==board[i][2] && board[i][2]==board[i][3] && board[i][3]=='X')
		{
			win='X';
			return 1;
		}
	for(i=0;i<4;i++)
		if(board[0][i]==board[1][i] && board[1][i]==board[2][i] && board[2][i]==board[3][i] && board[3][i]=='X')
		{
			win='X';
			return 1;
		}

	if((board[0][0]==board[1][1] && board[1][1]==board[2][2] && board[2][2]==board[3][3] && board[3][3]=='X') ||(board[3][0]==board[2][1] && board[2][1]==board[1][2] && board[1][2]==board[0][3] && board[0][3]=='X'))
	{
		win='X';
		return 1;
	}
	return -1;
}

int checkDraw()
{
	int i,j;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(board[i][j]=='.')
				return -1;
		}
	win='D';
	return 1;
}