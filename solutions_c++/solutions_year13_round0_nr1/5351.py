#include<stdio.h>
#include<iostream>
using namespace std;
#define MAX(X,Y) ((X) > (Y) ?  (X) : (Y))
char A[10][10];
char check()
{	int x=0;
	int o=0;
	for(int i =0 ;i<4;i++)
	{	int to,tx;
		to=tx=0;
		for(int j = 0;j<4;j++)
		{	
			if(A[i][j]=='X'||A[i][j]=='T')
				tx++;
			if(A[i][j]=='O'||A[i][j]=='T')
				to++;
		}
		x = MAX(x,tx);
		o = MAX(o,to);
	}
	for(int i =0 ;i<4;i++)
	{	int to,tx;
		to=tx=0;
		for(int j = 0;j<4;j++)
		{	
			if(A[j][i]=='X'||A[j][i]=='T')
				tx++;
			if(A[j][i]=='O'||A[j][i]=='T')
				to++;
		}
		x = MAX(x,tx);
		o = MAX(o,to);
	}
	int j = 0;
	int to,tx;
	to=tx=0;		
	for(int i=0;i<4;i++)
	{	if(A[i][j]=='X'||A[i][j]=='T')
		{	tx++;
		}
		if(A[i][j]=='O'||A[i][j]=='T')
		{	to++;
		}
		j++;
		
	}
	x = MAX(x,tx);
	o = MAX(o,to);
	j = 3;
	to=tx=0;
	for(int i=0;i<4;i++)
	{	if(A[i][j]=='X'||A[i][j]=='T')
		{	tx++;
		}
		if(A[i][j]=='O'||A[i][j]=='T')
		{	to++;
		}
		j--;
		
	}
	x = MAX(x,tx);
	o = MAX(o,to);
	int dot=0;
	for(int k =0;k<4;k++)
		for(int l=0;l<4;l++)
		{	if(A[k][l]=='.')
			{
			dot++;
			break;
			}
		}
	if(x==4)
		return 'X';
	if(o==4)
		return 'Y';
	if(x==3&&o==3&&dot==0)
		return 'D';
	return 'N';
}
int main()
{
	int Z,i,j;
	char c;
	scanf("%d",&Z);
	int count=1;
	while(Z--)
	{
		for(i=0;i<4;i++)
		{
			scanf("%s",A[i]);
		}
		printf("Case #%d: ",count);
		switch(check())
		{
		case 'D':
			printf("Draw\n");break;
		case 'X':
			printf("X won\n");break;
		case 'Y':
			printf("O won\n");break;
		case 'N':
			printf("Game has not completed\n");
		}
		count++;
	}
	return 0;
}
 
