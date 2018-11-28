#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char a[9][9],map[9][9];
int test;

bool deal(char c)
{
	memcpy(a,map,sizeof a);
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			if (a[i][j]=='T') a[i][j]=c;
	for (int i=0;i<4;i++)
	{
		if (a[i][0]==c && a[i][1]==c && a[i][2]==c && a[i][3]==c) return 1;
		if (a[0][i]==c && a[1][i]==c && a[2][i]==c && a[3][i]==c) return 1;
	}
	if (a[0][0]==c && a[1][1]==c && a[2][2]==c && a[3][3]==c) return 1;
	if (a[0][3]==c && a[1][2]==c && a[2][1]==c && a[3][0]==c) return 1;
	return 0;
}

bool check()
{
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			if (map[i][j]=='.') 
				return 0;
	return 1;
}

int main()
{
	scanf("%d",&test);
	for (int t=0;t<test;t++)
	{
		for (int i=0;i<4;i++) scanf("%s",map[i]);
		printf("Case #%d: ",t+1);
		if (deal('X')) puts("X won");
		else if (deal('O')) puts("O won");
		else if (check()) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}