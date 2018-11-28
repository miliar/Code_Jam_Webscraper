#include <cstdio>
int t;
char c[6][6];
bool dotexists=false;
int check()
{
	bool tt = false;
	int wynik=0;
	char co=0;
	// diagonals
	for (int i = 0; i < 4; i++)
	{
		if (c[i][i]=='T')
			tt=true;
		else if (c[i][i]=='.')
			break;
		else if (co!='X' && c[i][i]=='O')
			co='O', wynik++;
		else if (co!='O' && c[i][i]=='X')
			co='X', wynik++;
		else
		{co=0, wynik=0, tt=false; break;}
	}
	if ((wynik==3&&tt)||wynik==4)
		return (co=='O')?2:1;
	co=0, wynik=0, tt=false;
	for (int i = 0; i < 4; i++)
	{
		if (c[i][3-i]=='T')
			tt=true;
		else if (c[i][3-i]=='.')
			break;
		else if (co!='X' && c[i][3-i]=='O')
			co='O', wynik++;
		else if (co!='O' && c[i][3-i]=='X')
			co='X', wynik++;
		else
		{co=0, wynik=0, tt=false; break;}
	}
	if ((wynik==3&&tt)||wynik==4)
		return (co=='O')?2:1;
	co=0, wynik=0, tt=false;
	// rows
	for (int j = 0; j < 4; j++)
	{
	for (int i = 0; i < 4; i++)
	{
		if (c[j][i]=='T')
			tt=true;
		else if (c[j][i]=='.')
			break;
		else if (co!='X' && c[j][i]=='O')
			co='O', wynik++;
		else if (co!='O' && c[j][i]=='X')
			co='X', wynik++;
		else
		{co=0, wynik=0, tt=false; break;}
	}
	if ((wynik==3&&tt)||wynik==4)
		return (co=='O')?2:1;
	co=0, wynik=0, tt=false;
	}
	//columns
	for (int j = 0; j < 4; j++)
	{
	for (int i = 0; i < 4; i++)
	{
		if (c[i][j]=='T')
			tt=true;
		else if (c[i][j]=='.')
			break;
		else if (co!='X' && c[i][j]=='O')
			co='O', wynik++;
		else if (co!='O' && c[i][j]=='X')
			co='X', wynik++;
		else
		{co=0, wynik=0, tt=false; break;}
	}
	if ((wynik==3&&tt)||wynik==4)
		return (co=='O')?2:1;
	co=0, wynik=0, tt=false;
	}
	//exit
	if (dotexists)
		return 4;
	else
		return 3;
}
int main()
{
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		dotexists=false;
		for (int y = 0; y < 4; y++)
		{
			scanf("%s", c[y]);
			if (c[y][0]=='.'||c[y][1]=='.'||c[y][2]=='.'||c[y][3]=='.')
				dotexists=true;
		}
		switch (check())
		{
		case 1:
			printf("Case #%d: X won\n", i+1);
			break;
		case 2:
			printf("Case #%d: O won\n", i+1);
			break;
		case 3:
			printf("Case #%d: Draw\n", i+1);
			break;
		case 4:
			printf("Case #%d: Game has not completed\n", i+1);
			break;
		}

	}
	return 0;
}
