#include<stdio.h>
int main()
{
	int i,j,k,t,countrx[5],countro[5],countcx[5],countco[5],incomplete=0,diaglx,diagrx,diaglo,diagro;
	int win=0;
	char board[5][5];
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		diaglx=diaglo=diagrx=diagro=0;
		win=0;
		incomplete=0;
		for(j=0;j<4;j++)
			scanf("%s",board[j]);
		for(j=0;j<4;j++)
		{
			countco[j]=0;
			countcx[j]=0;
			countrx[j]=0;
			countro[j]=0;
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(board[j][k]=='O')
				{
					countro[j]++;
					countco[k]++;
				}
				else if(board[j][k]=='X')
				{
					countrx[j]++;
					countcx[k]++;
				}
				else if(board[j][k]=='T')
				{
					countrx[j]++;
					countro[j]++;
					countco[k]++;
					countcx[k]++;
				}
				else if(board[j][k]=='.')
				{
					incomplete=1;
				}
			}
		}
		for(j=0;j<4;j++)
		{
			if(countcx[j]==4 || countrx[j]==4)
			{
				printf("Case #%d: X won\n",i+1);
				win=1;
				break;
			}
			else if(countco[j]==4 || countro[j]==4)
			{
				printf("Case #%d: O won\n",i+1);
				win=1;
				break;
			}
		}
		if(win==0)
		{
			for(j=0;j<4;j++)
			{
				if(board[j][j]=='X')
					diaglx++;
				else if(board[j][j]=='O')
					diaglo++;
				else if(board[j][j]=='T')
				{
					diaglo++;
					diaglx++;
				}
				if(board[j][3-j]=='X')
					diagrx++;
				else if(board[j][3-j]=='O')
					diagro++;
				else if(board[j][3-j]=='T')
				{
					diagro++;
					diagrx++;
				}
			}
			if(diaglx==4 || diagrx==4)
			{
				printf("Case #%d: X won\n",i+1);
			}
			else if(diaglo==4 || diagro==4)
			{
				printf("Case #%d: O won\n",i+1);
			}
			else if(incomplete==1)
			{
				printf("Case #%d: Game has not completed\n",i+1);
			}
			else
			{
				printf("Case #%d: Draw\n",i+1);
			}
		}
	}
}
