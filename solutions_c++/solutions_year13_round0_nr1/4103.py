#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>
#pragma comment(linker, "/STACK:10000000") 
#define md 1000000007

using namespace std;

int i,t,test,j,all;
char s[5][5];

FILE* f,*g;

bool check(char c)
{
	int i,j,p;
	bool ok=false;
	
	for (i=1;i<=4;i++)
	{
		p=0;
		for (j=1;j<=4;j++) if (s[i][j]=='T' || s[i][j]==c) p++;
		ok = (ok || p==4);
		
		p=0;
		for (j=1;j<=4;j++) if (s[j][i]=='T' || s[j][i]==c) p++;
		ok = (ok || p==4);
	}
	p=0;
	for (i=1;i<=4;i++) if (s[i][i]=='T' || s[i][i]==c) p++;
	ok = (ok || p==4);
	
	p=0;
	for (i=1;i<=4;i++) if (s[i][5-i]=='T' || s[i][5-i]==c) p++;
	ok = (ok || p==4);
	return ok;
}

int main()
{
	f = fopen("input.txt","r");
	g = fopen("output.txt","w");
	fscanf(f,"%d\n",&t);
	
	for (test=1;test<=t;test++)
	{
		all=0;
		for (i=1;i<=4;i++)
		{
			for (j=1;j<=4;j++)
			{
				 fscanf(f,"%c",&s[i][j]);
				 if (s[i][j]=='.') all++;
			}
			fscanf(f,"\n");	
			fscanf(f,"\n");	
		}	
		fprintf(g,"Case #%d: ",test);
		
		if (check('X')) fprintf(g,"X won\n");
		else if (check('O')) fprintf(g,"O won\n");
		else if (all==0) fprintf(g,"Draw\n");
		else fprintf(g,"Game has not completed\n");
	}	
}
