#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdlib>
using namespace std;

const int maxn=10;
char s[5][5];
int n;

void close()
{
exit(0);
}

void owon()
{
	printf("O won\n");
}

void xwon()
{
	printf("X won\n");
}

bool column(int k,char c)
{
	for (int i=1;i<=4;i++)
		if (s[i][k]!=c && s[i][k]!='T')
			return false;
	return true;
}

bool row(int k,char c)
{
	for (int i=1;i<=4;i++) //Ã¿Ò»ÐÐ
		if (s[k][i]!=c && s[k][i]!='T')
			return false;
	return true;
}

void work()
{
	//x:
	for (int i=1;i<=4;i++)
	{
		if (row(i,'X') || column(i,'X'))
		{
			xwon();
			return;
		}
		if (row(i,'O') || column(i,'O'))
		{
			owon();
			return;
		}
	}
	bool flag=false;
	for (int i=1;i<=4;i++)
		if (s[i][i]!='X' && s[i][i]!='T')
			flag=true;
	if (not flag)
	{
		xwon();
		return;
	}
	flag=false;
	for (int i=1;i<=4;i++)
		if (s[i][i]!='O' && s[i][i]!='T')
			flag=true;
	if (not flag)
	{
		owon();
		return;
	}
	flag=false;
	for (int i=1;i<=4;i++)
		if (s[i][4-i+1]!='X' && s[i][4-i+1]!='T')
			flag=true;
	if (not flag)
	{
		xwon();
		return;
	}
	flag=false;
	for (int i=1;i<=4;i++)
		if (s[i][4-i+1]!='O' && s[i][4-i+1]!='T')
			flag=true;
	if (not flag)
	{
		owon();
		return;
	}
	for (int i=1;i<=4;i++)
	{
		for (int j=1;j<=4;j++)
			if (s[i][j]=='.')
			{
				printf("Game has not completed\n");
				return;
			}
	}
	printf("Draw\n");
}


void init()
{
	scanf("%d",&n);
	for (int i=1;i<=n;i++)
	{
		printf("Case #%d: ",i);
		memset(s,'\0',sizeof(s));
		for (int j=1;j<=4;j++)
			scanf("%s",s[j]);
		for (int k=1;k<=4;k++)
			for (int j=4;j>=1;j--)
				s[k][j]=s[k][j-1];
		work();
	}
}

int main ()
{
	init();
	close();
	return 0;
}

