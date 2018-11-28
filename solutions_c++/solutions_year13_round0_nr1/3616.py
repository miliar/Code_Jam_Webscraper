#include <stdio.h>

char chs[10][10];
int cs;

void go()
{
	int i, j;
	bool ck;
	/* XX */
	for(i = 1 ; i <= 4 ; i++)
	{
		ck = true;
		for(j = 1 ; j <= 4 ; j++)
		{
			if(chs[i][j] == 'O' || chs[i][j] == '.')
			{
				ck = false;
				break;
			}
		}
		if(ck == true)
		{
			printf("Case #%d: X won\n", cs);
			return;
		}
	}

	for(i = 1 ; i <= 4 ; i++)
	{
		ck = true;
		for(j = 1 ; j <= 4 ; j++)
		{
			if(chs[j][i] == 'O' || chs[j][i] == '.')
			{
				ck = false;
				break;
			}
		}
		if(ck == true)
		{
			printf("Case #%d: X won\n", cs);
			return;
		}
	}
	ck = true;
	for(i = 1 ; i <= 4 ; i++)
	{
		if(chs[i][i] == 'O' || chs[i][i] == '.')
		{
			ck = false;
			break;
		}
	}
	if(ck == true)
	{
		printf("Case #%d: X won\n", cs);
		return;
	}

	ck = true;
	for(i = 1 ; i <= 4 ; i++)
	{
		if(chs[i][4-i+1] == 'O' || chs[i][4-i+1] == '.')
		{
			ck = false;
			break;
		}
	}
	if(ck == true)
	{
		printf("Case #%d: X won\n", cs);
		return;
	}	
	/* OO */
	for(i = 1 ; i <= 4 ; i++)
	{
		ck = true;
		for(j = 1 ; j <= 4 ; j++)
		{
			if(chs[i][j] == 'X' || chs[i][j] == '.')
			{
				ck = false;
				break;
			}
		}
		if(ck == true)
		{
			printf("Case #%d: O won\n", cs);
			return;
		}
	}

	for(i = 1 ; i <= 4 ; i++)
	{
		ck = true;
		for(j = 1 ; j <= 4 ; j++)
		{
			if(chs[j][i] == 'X' || chs[j][i] == '.')
			{
				ck = false;
				break;
			}
		}
		if(ck == true)
		{
			printf("Case #%d: O won\n", cs);
			return;
		}
	}

	ck = true;
	for(i = 1 ; i <= 4 ; i++)
	{
		if(chs[i][i] == 'X' || chs[i][i] == '.')
		{
			ck = false;
			break;
		}
	}
	if(ck == true)
	{
		printf("Case #%d: O won\n", cs);
		return;
	}

	ck = true;
	for(i = 1 ; i <= 4 ; i++)
	{
		if(chs[i][4-i+1] == 'X' || chs[i][4-i+1] == '.')
		{
			ck = false;
			break;
		}
	}
	if(ck == true)
	{
		printf("Case #%d: O won\n", cs);
		return;
	}	

	ck = true;
	for(i = 1 ; i <= 4 ; i++)
	{
		for(j = 1 ; j <= 4 ; j++)
		{
			if(chs[i][j] == '.')
			{
				ck = false;
				break;
			}
		}
		if(ck == false)
		{
			break;
		}
	}

	if(ck == true)
	{
		printf("Case #%d: Draw\n", cs);
		return;
	}
	else
	{
		printf("Case #%d: Game has not completed\n", cs);
		return;
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out2.txt", "w", stdout);
	int T;
	
	scanf("%d", &T);
	cs = 1;
	while(T--)
	{
		int i;
		for(i = 1 ; i <= 4 ; i++)
		{
			scanf("%s", chs[i]+1);
		}
		/*for(i = 1 ; i <= 4 ; i++)
		{
			for(j = 1 ; j <= 4 ; j++)
			{
				printf("%c", chs[i][j]);
			}
			printf("\n");
		}*/
		go();
		getchar();
		cs++;
	}
	return 0;
}
