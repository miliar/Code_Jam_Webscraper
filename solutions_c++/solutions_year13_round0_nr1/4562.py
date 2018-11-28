#include<cstdio>


char test(char str[][5])
{
	int i,j,X,O;
	char flag='D';
	for(i=0;i<=3;i++)
	{
		for(j=0,X=0,O=0;j<=3;j++)
		{
			if(str[i][j]=='.')
			{
				flag='I';
				break;
			}
			else if(str[i][j]=='X')
			{
				X++;
			}
			else if(str[i][j]=='O')
			{
				O++;
			}
			else if(str[i][j]=='T')
			{
				X++;
				O++;
			}
		}
		if(X==4)
		{
			return 'X';
		}
		else if(O==4)
		{
			return 'O';
		}
	}
	for(j=0;j<=3;j++)
	{
		for(i=0,X=0,O=0;i<=3;i++)
		{
			if(str[i][j]=='X')
			{
				X++;
			}
			else if(str[i][j]=='O')
			{
				O++;
			}
			else if(str[i][j]=='T')
			{
				X++;
				O++;
			}
		}
		if(X==4)
		{
			return 'X';
		}
		else if(O==4)
		{
			return 'O';
		}
	}
	for(i=0,X=0,O=0;i<=3;i++)
	{
		if(str[i][i]=='X')
		{
			X++;
		}
		else if(str[i][i]=='O')
		{
			O++;
		}
		else if(str[i][i]=='T')
		{
			X++;
			O++;
		}
		if(X==4)
		{
			return 'X';
		}
		else if(O==4)
		{
			return 'O';
		}
	}
	for(i=3,j=0,X=0,O=0;i>=0;i--,j++)
	{
		if(str[i][j]=='X')
		{
			X++;
		}
		else if(str[i][j]=='O')
		{
			O++;
		}
		else if(str[i][j]=='T')
		{
			X++;
			O++;
		}
		
		if(X==4)
		{
			return 'X';
		}
		else if(O==4)
		{
			return 'O';
		}
	}

	return flag;
}

int main()
{
	int i,j,T;
	char str[5][5];
	char flag,temp[5];
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		gets(temp);
		for(j=0;j<4;j++)
		{
			gets(str[j]);
		}
		flag=test(str);
		if(flag=='X')
		{
			printf("Case #%d: X won\n",i);
		}
		else if(flag=='O')
		{
			printf("Case #%d: O won\n",i);
		}
		else if(flag=='I')
		{
			printf("Case #%d: Game has not completed\n",i);
		}
		else if(flag=='D')
		{
			printf("Case #%d: Draw\n",i);
		}
	}
//	fclose(stdin);
//	fclose(stdout);
	return 0;
}