#include<stdio.h>

int compute(char board[][5])
{
int i,j,dot=0,count1,count2;
	for(i=0;i<4;i++)
	{
		count1=0;
		count2=0;
		for(j=0;j<4;j++)
		{
			if(board[i][j]=='.')
				dot++;
			if(board[i][j]=='X')
				count1++;
			if(board[i][j]=='O')
				count2++;	
			if(board[i][j]=='T')
			{
				count1++;
				count2++;
			}
		}
		if(count1==4)
			return 1;
		if(count2==4)
			return 2;
	}
	
	for(i=0;i<4;i++)
	{
		count1=0;
		count2=0;
		for(j=0;j<4;j++)
		{
			if(board[j][i]=='.')
				dot++;
			if(board[j][i]=='X')
				count1++;
			if(board[j][i]=='O')
				count2++;	
			if(board[j][i]=='T')
			{
				count1++;
				count2++;
			}
		}
		if(count1==4)
			return 1;
		if(count2==4)
			return 2;
	}
		count1=0;
		count2=0;	
	for(i=0,j=0;i<4 && j<4;i++,j++)
	{

			if(board[i][j]=='X')
				count1++;
			if(board[i][j]=='O')
				count2++;	
			if(board[i][j]=='T')
			{
				count1++;
				count2++;
			}
		if(count1==4)
			return 1;
		if(count2==4)
			return 2;
	}
		count1=0;
		count2=0;
	for(i=3,j=0; i>=0 && j<4; i--,j++)
	{

			if(board[i][j]=='X')
				count1++;
			if(board[i][j]=='O')
				count2++;	
			if(board[i][j]=='T')
			{
				count1++;
				count2++;
			}
	
		if(count1==4)
			return 1;
		if(count2==4)
			return 2;
	}
	if(!dot)
		return 3;
	return 4;
}
	


int main()
{
char board[5][5];
int i,t,j,k,status;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
	for(j=0;j<4;j++)
		scanf("%s",board[j]);
	status=compute(board);
	switch(status)
	{
		case 1:printf("Case #%d: X won\n",i);
				break;
		case 2:printf("Case #%d: O won\n",i);
				break;
		case 3:printf("Case #%d: Draw\n",i);
				break;
		case 4:printf("Case #%d: Game has not completed\n",i);
				break;
	}
}
return 0;
}
