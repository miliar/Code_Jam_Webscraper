#include <stdio.h>

int main()
{
	int T,i,j,k,win; //win 1draw  2not completed    3 O   4 X
	char game[4][5],cam;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		win=1;
		for(j=0;j<4;j++)
		{
			scanf("%s",game[j]);
		}
		for(j=0;j<4;j++) //直 
		{
			cam='T';
			for(k=0;k<4;k++)
			{
				if(game[j][k]=='.')
				{
					if(win==1)
						win=2;
					break;
				}
				if(cam=='T' && game[j][k]!='T')
					cam=game[j][k];
				if(cam!=game[j][k] && game[j][k]!='T')
					break;
			}
			if(k==4)
			{
				if(cam=='O')
					win=3;
				else
					win=4;
			}
		}
		
		for(k=0;k<4;k++)  //橫 
		{
			cam='T';
			for(j=0;j<4;j++)
			{
				if(game[j][k]=='.')
				{
					if(win==1)
						win=2;
					break;
				}
				if(cam=='T' && game[j][k]!='T')
					cam=game[j][k];
				if(cam!=game[j][k] && game[j][k]!='T')
					break;
			}
			if(j==4)
			{
				if(cam=='O')
					win=3;
				else
					win=4;
			}
		}
		
		cam='T'; 
		for(j=0;j<4;j++)	//左上to右下
		{
			if(game[j][j]=='.')
			{
				if(win==1)
					win=2;
				break;
			}
			if(cam=='T' && game[j][j]!='T')
				cam=game[j][j];
			if(cam!=game[j][j] && game[j][j]!='T')
				break;
		}
		if(j==4)
		{
			if(cam=='O')
				win=3;
			else
				win=4;
		}
		
		cam='T'; 
		for(j=0;j<4;j++)	//右上to左下
		{
			if(game[j][3-j]=='.')
			{
				if(win==1)
					win=2;
				break;
			}
			if(cam=='T' && game[j][3-j]!='T')
				cam=game[j][3-j];
			if(cam!=game[j][3-j] && game[j][3-j]!='T')
				break;
		}
		if(j==4)
		{
			if(cam=='O')
				win=3;
			else
				win=4;
		}
		
		printf("Case #%d: ",i);
		switch(win)
		{
			case 1: printf("Draw\n") ;break;
			case 2: printf("Game has not completed\n") ;break;
			case 3: printf("O won\n") ;break;
			case 4: printf("X won\n") ;break;
		}
	}
	return 0;
}
