#include<stdio.h>

char map[4][5];
char findWinner();
int main()
{
	int t,T;

	FILE * ip=fopen("A-small-attempt5.in","r");
	FILE * op=fopen("A-small-attempt5.out","w");

	fscanf(ip,"%d",&T);
	for(t=0;t<T;t++)
	{
		int i,j,xT=-1,yT=-1,p=1;
		char winner='D';
		for(i=0;i<4;i++)
		{
			fscanf(ip,"%s",map[i]);
			for(j=0;j<4;j++)
				if(map[i][j]=='T')
				{
					xT=i;
					yT=j;
				}
		}
		if(xT==-1)//T °¡ ¾ø´Ù.
		{
			winner=findWinner();
		}
		else
		{
			{
				if(winner!='O'&&winner!='X')
				{
				map[xT][yT]='O';
				winner=findWinner();
				}
			}
			{
				if(winner!='O'&&winner!='X')
				{
				map[xT][yT]='X';
				winner=findWinner();
				}
			}

		}
		if(winner=='X'||winner=='O')
			fprintf(op,"Case #%d: %c won\n",t+1,winner);

		else
		{
			for(i=0;i<4;i++)for(j=0;j<4;j++)
				if(map[i][j]=='.')
					p=0;
			if(p)
				fprintf(op,"Case #%d: Draw\n",t+1);
			else
				fprintf(op,"Case #%d: Game has not completed\n",t+1);
		}



	}
	return 0;
}
char findWinner()
{
	char winner='D';
	int i,j;
	for(i=0;i<4;i++)
	{
		if((map[i][0]==map[i][1])&&(map[i][0]==map[i][2])&&(map[i][0]==map[i][3]))
			return winner=map[i][0];
	}
	for(j=0;j<4;j++)
	{
		if((map[0][j]==map[1][j])&&(map[0][j]==map[2][j])&&(map[0][j]==map[3][j]))
			return winner=map[0][j];
	}
	if((map[0][0]==map[1][1])&&(map[0][0]==map[2][2])&&(map[0][0]==map[3][3]))
		return winner=map[0][0];
	if((map[0][3]==map[1][2])&&(map[0][3]==map[2][1])&&(map[0][3]==map[3][0]))
		return winner=map[0][3];
	 
	return winner;
}