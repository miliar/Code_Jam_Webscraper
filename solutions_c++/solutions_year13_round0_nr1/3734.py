#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<string.h>
#include<cmath>
using namespace std;
#define N 10
char MAT[N][N];
void input(int n)
{
	char ch;
	for(int s=0;s<n;s++)
	{
		ch=getchar();
		if(ch=='X')MAT[s/4][s%4]=ch;
		else if(ch=='O')MAT[s/4][s%4]=ch;
		else if(ch=='T')MAT[s/4][s%4]=ch;
		else if(ch=='.')MAT[s/4][s%4]=ch;
		else s--;
	}
}
int check_row(int i,int n,char type)
{
	for(int j=0;j<n;j++)
		if(MAT[i][j]==type||MAT[i][j]=='T')continue;
		else return 0;
		return 1;
}
int check_col(int j,int n,char type)
{
	for(int i=0;i<n;i++)
		if(MAT[i][j]==type||MAT[i][j]=='T')continue;
		else return 0;
		return 1;
}
int check_diag(int n,int diag,char type)
{
	if(diag==0){
		for(int i=0;i<n;i++)
			if(MAT[i][i]==type||MAT[i][i]=='T')continue;
			else return 0;
			return 1;
	}
	else
	{
		for(int i=0;i<n;i++)
			if(MAT[i][n-i-1]==type||MAT[i][n-i-1]=='T')continue;
			else return 0;
			return 1;
	}
}
int checkWho(char type)
{
	for(int i=0;i<4;i++)
		if(check_row(i,4,type))return 1;
	for(int j=0;j<4;j++)
		if(check_col(j,4,type))return 1;
	for(int dia=0;dia<2;dia++)
		if(check_diag(4,dia,type))return 1;
	return 0;
}
int check_draw(int n){
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			if(MAT[i][j]=='.')return 0;
	return 1;
}
int check()
{
	if(checkWho('X'))return 'X';
	if(checkWho('O'))return 'O';
	if(check_draw(4))return 'D';
	return '.';
}
int main(void)
{
	int T,cse=0,ret;
	freopen("data.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		input(4*4);
		ret=check();
		printf("Case #%d: ",++cse);
		if(ret=='X')	printf("X won\n");
		else if(ret=='O')	printf("O won\n");
		else if(ret=='D')	printf("Draw\n");
		else printf("Game has not completed\n");
	}

	return 0;
}
/*
6
XXXT
....
OO..
....

*/