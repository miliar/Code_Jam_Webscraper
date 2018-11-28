#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
char ch[4][4];
int check()
{
	int cntx,cnto,cnt=0;
	for(int i=0;i<4;i++)
	{
		cntx=cnto=0;
		for(int j=0;j<4;j++)
		{
			if(ch[i][j]=='X' || ch[i][j]=='T')
			cntx++;
			if(ch[i][j]=='O' || ch[i][j]=='T')
			cnto++;
		}
		if(cnto==4)
		return 0;
		else if(cntx==4)
		return 1;
	}
	for(int j=0;j<4;j++)
	{
		cntx=cnto=0;
		for(int i=0;i<4;i++)
		{
			if(ch[i][j]=='X' || ch[i][j]=='T')
			cntx++;
			if(ch[i][j]=='O' || ch[i][j]=='T')
			cnto++;
		}
		if(cnto==4)
		return 0;
		else if(cntx==4)
		return 1;
	}
	cntx=cnto=0;
	{
		for(int i=0;i<4;i++)
		{
			if(ch[i][i]=='X' || ch[i][i]=='T')
			cntx++;
			if(ch[i][i]=='O' || ch[i][i]=='T')
			cnto++;
		}
		if(cnto==4)
		return 0;
		else if(cntx==4)
		return 1;
	}
	cntx=cnto=0;
	{
		for(int i=0;i<4;i++)
		{
			if(ch[i][3-i]=='X' || ch[i][3-i]=='T')
			cntx++;
			if(ch[i][3-i]=='O' || ch[i][3-i]=='T')
			cnto++;
		}
		if(cnto==4)
		return 0;
		else if(cntx==4)
		return 1;
	}
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	if(ch[i][j]!='.')
	cnt++;
	if(cnt==16)
	return 5;
	else 
	return 9;
}
int main()
{
	int t,test;
	FILE *fp;
	FILE *rf;
	char c[6];
	fp=fopen("A-large.in","r");
	fscanf(fp,"%d",&test);
	int ans[test];
	for(t=0;t<test;t++)
	{
		for(int i=0;i<4;i++)
		fscanf(fp,"%s",ch[i]);
		ans[t]=check();
	}
	rf=fopen("ANS1.in","w+");
	for(t=0;t<test;t++)
	{
		fprintf(rf,"Case #%d: ",t+1);
		if(ans[t]==0)
		fprintf(rf,"O won\n");
		if(ans[t]==1)
		fprintf(rf,"X won\n");
		if(ans[t]==5)
		fprintf(rf,"Draw\n");
		if(ans[t]==9)
		fprintf(rf,"Game has not completed\n");
	}
}
