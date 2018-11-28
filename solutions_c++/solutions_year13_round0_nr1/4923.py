#include <stdio.h>

FILE *in=fopen("A-large.in","rt");
FILE *out=fopen("A-large.out","wt");

char map[10][10];

void input()
{
	int i;
	for(i=1;i<=4;i++) fscanf(in," %s",&map[i][1]);
}

bool win_check1(int i, char t)
{
	int j;
	for(j=1;j<=4;j++) 
	{
		if(map[i][j]=='T' || map[i][j]==t) continue;
		return false;
	}
	return true;
}

bool win_check2(int i, char t)
{
	int j;
	for(j=1;j<=4;j++)
	{
		if(map[j][i]=='T' || map[j][i]==t) continue;
		return false;
	}
	return true;
}

bool win_check3(char t)
{
	int i;
	for(i=1;i<=4;i++) 
	{
		if(map[i][i]=='T' || map[i][i]==t) continue;
		return false;
	}
	return true;
}

bool win_check4(char t)
{
	int i;
	for(i=1;i<=4;i++) 
	{
		if(map[i][5-i]=='T' || map[i][5-i]==t) continue;
		return false;
	}
	return true;
}

void process()
{
	int i,j;
	for(i=1;i<=4;i++)
	{
		if(win_check1(i,'O') || win_check2(i,'O'))
		{
			fprintf(out,"O won");
			return;
		}
		
		if(win_check1(i,'X') || win_check2(i,'X'))
		{
			fprintf(out,"X won");
			return;
		}
	}

	if(win_check3('O') || win_check4('O'))
	{
		fprintf(out,"O won");
		return;
	}
	if(win_check3('X') || win_check4('X'))
	{
		fprintf(out,"X won");
		return;
	}

	for(i=1;i<=4;i++)
	{
		for(j=1;j<=4;j++) 
		{
			if(map[i][j]=='.')
			{
				fprintf(out,"Game has not completed");
				return;
			}
		}
	}
	fprintf(out,"Draw");
		
}

int main()
{
	int t,i;
	fscanf(in,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fprintf(out,"Case #%d: ",i);
		input();
		process();
		fprintf(out,"\n");
	}
	fclose(in);
	fclose(out);
	return 0;
}