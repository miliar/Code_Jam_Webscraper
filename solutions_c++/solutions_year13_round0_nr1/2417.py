#include <stdio.h>
#include <string.h>

char str[5][5];

int main()
{
	int T;
	FILE* fp;
	fp = fopen("A-small-attempt1.in","r");

	FILE* fp1;
	fp1 = fopen("output.out","w");
	fscanf(fp,"%d",&T);
	for(int c = 1;c <= T;c++)
	{
		char a;
		int flag = -1;
		int i,j;
		for(i = 0;i < 4;i++)	fscanf(fp,"%s",str[i]);

		for(i = 0;i < 4;i++)
		{
			a = str[i][0];
			for(j = 0;j < 4;j++)
				if(str[i][j] != a && str[i][j] != 'T')
					break;
			if(j >= 4)
			{
				if(a == 'X')
					flag = 0;
				else
				{
					if(a == 'O')
						flag = 1;
				}
				break;
			}
		}

		for(i = 0;i < 4;i++)
		{
			a = str[0][i];
			for(j = 0;j < 4;j++)
				if(str[j][i] != a && str[j][i] != 'T')
					break;
			if(j >= 4)
			{
				if(a == 'X')
					flag = 0;
				else
				{
					if(a == 'O')
						flag = 1;
				}
				break;
			}
		}

		a = str[0][0];
		for(i = 0;i < 4;i++)
			if(str[i][i] != a && str[i][i] != 'T')
				break;
		if(i >= 4)
		{
			if(a == 'X')
				flag = 0;
			else
			{
				if(a == 'O')
					flag = 1;
			}
		}

		a = str[0][3];
		for(i = 0;i < 4;i++)
			if(str[i][3-i] != a && str[i][3-i] != 'T')
				break;
		if(i >= 4)
		{
			if(a == 'X')
				flag = 0;
			else
			{
				if(a == 'O')
					flag = 1;
			}
		}

		if(flag == -1)
		{
			int cnt = 0;
			for(i = 0;i < 4;i++)
				for(j = 0;j < 4;j++)
					if(str[i][j] == '.')
						cnt++;
			if(cnt > 0)
				fprintf(fp1,"Case #%d: Game has not completed\n",c);
			else
				fprintf(fp1,"Case #%d: Draw\n",c);
		}
		else
		{
			if(flag == 0)
			{
				fprintf(fp1,"Case #%d: X won\n",c);
			}
			else
			{
				fprintf(fp1,"Case #%d: O won\n",c);
			}
		}
	}

	fclose(fp);
	fclose(fp1);
	return 0;
}