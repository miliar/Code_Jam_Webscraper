#include<stdio.h>
#include<conio.h>
int check(char board[4][5])
{
	char temp;
	int flag=1, winning,i,j;

	/*for(i=0;i<4;++i)
		printf("%s\n",board[i]);
	*/
	//horizontals
	for(i=0;i<4;++i)
	{
		flag=1;
		if (board[i][0]=='.')
			flag=0;
		if (board[i][0]!='T')
			temp=board[i][0];
		else
			temp=board[i][1];
		for(j=1;j<4;++j)
		{
			if(temp!=board[i][j] && board[i][j]!='T')
			{
				flag=0;
				break;
			}
		}
		if(flag)
		{
			//printf("%c\n",temp);
			switch(temp)
			{
				case 'X': return 1;
				case 'O': return 2;
			}
		}
	}

	//verticals
	flag=1;
	for(i=0;i<4;++i)
	{
		flag=1;
		if (board[0][i]=='.')
			flag=0;
		if (board[0][i]!='T')
			temp=board[0][i];
		else
			temp=board[1][i];
		for(j=1;j<4;++j)
		{
			if(temp!=board[j][i] && board[j][i]!='T')
			{
				flag=0;
				break;
			}
		}
		if(flag)
		{
			//printf("%c\n",temp);
			switch(temp)
			{
				case 'X': return 1;
				case 'O': return 2;
			}
		}
	}

	//diagonal i==j
	flag=1;
	if (board[i][0]=='.')
			flag=0;
	if (board[0][0]!='T')
		temp=board[0][0];
	else
		temp=board[1][1];
	for(j=1;j<4;++j)
	{
		if(temp!=board[j][j] && board[j][j]!='T')
		{
			flag=0;
			break;
		}
	}
	if(flag)
	{
		//printf("%c\n",temp);
		switch(temp)
		{
			case 'X': return 1;
			case 'O': return 2;
		}
	}

	//diagonal i==3-j
	flag=1;
	if (board[i][0]=='.')
			flag=0;
	if (board[0][3]!='T')
		temp=board[0][3];
	else
		temp=board[1][2];
	for(j=1;j<4;++j)
	{
		if(temp!=board[j][3-j] && board[j][3-j]!='T')
		{
			flag=0;
			break;
		}
	}
	if(flag)
	{
		//printf("%c\n",temp);
		switch(temp)
		{
			case 'X': return 1;
			case 'O': return 2;
		}
	}

	//Draw
	flag=1;
	for(i=0;i<4;++i)
		for(j=0;j<4;++j)
			if(board[i][j]=='.')
				flag=0;
	if(flag)
		return 3;
	return 4;
}
int main()
{
	char board[4][5]={"","","",""};
	int T,i;
	clrscr();
	FILE *fp=fopen("input.txt","r");
	FILE *out=fopen("output.txt","w");
	fscanf(fp,"%d",&T);
	for(int set=1;set<=T;++set)
	{
		for(i=0;i<4;++i)
			fscanf(fp,"%4s",board[i]);

		switch(check(board))
		{
			case 1:
				fprintf(out,"Case #%d: X won\n",set);
				printf("Case #%d: X won\n",set);
				break;
			case 2:
				fprintf(out,"Case #%d: O won\n",set);
				printf("Case #%d: O won\n",set);
				break;
			case 3:
				fprintf(out,"Case #%d: Draw\n",set);
				printf("Case #%d: Draw\n",set);
				break;
			case 4:
				fprintf(out,"Case #%d: Game has not completed\n",set);
				printf("Case #%d: Game has not completed\n",set);
				break;
		}
	}
	getch();
	fclose(fp);
	fclose(out);
	return 0;
}