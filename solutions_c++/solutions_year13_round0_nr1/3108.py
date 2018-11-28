#include<stdio.h>
#include<iostream>
char s[10][10];
int X,O,xx,oo;
void check_row(int k)
{
	xx=0;oo=0;
	for(int i=0;i<4;i++)
	{
		if(s[i][k]=='.') return;
		if(s[i][k]=='X') xx=1;
		if(s[i][k]=='O') oo=1;
	}
	if(xx==1&&oo==1) return;
	if(xx==1) X=1;
	else O=1;
	return;
}
void check_col(int k)
{
	xx=0;oo=0;
	for(int i=0;i<4;i++)
	{
		if(s[k][i]=='.') return;
		if(s[k][i]=='X') xx=1;
		if(s[k][i]=='O') oo=1;
	}
	if(xx==1&&oo==1) return;
	if(xx==1) X=1;
	else O=1;
	return;
}
void check_diag1()
{
	xx=0;oo=0;
	for(int i=0;i<4;i++)
	{
		if(s[i][i]=='.') return;
		if(s[i][i]=='X') xx=1;
		if(s[i][i]=='O') oo=1;
	}
	if(xx==1&&oo==1) return;
	if(xx==1) X=1;
	else O=1;
	return;
}
void check_diag2()
{
	xx=0;oo=0;
	for(int i=0;i<4;i++)
	{
		if(s[i][3-i]=='.') return;
		if(s[i][3-i]=='X') xx=1;
		if(s[i][3-i]=='O') oo=1;
	}
	if(xx==1&&oo==1) return;
	if(xx==1) X=1;
	else O=1;
	return;
}
main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int n,check;
	scanf("%d\n",&n);
	for(int ll=0;ll<n;ll++)
	{
		X=0;O=0;
		for(int i=0;i<4;i++) scanf("%s",s[i]);
		for(int i=0;i<4;i++) check_row(i);
		for(int i=0;i<4;i++) check_col(i);
		check_diag1();
		check_diag2();
		printf("Case #%d: ",ll+1);
		if(X==1)
		{
			printf("X won\n");
			continue;
		}
		else if(O==1)
		{
			printf("O won\n");
			continue;
		}
		check=0;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(s[i][j]=='.') check=1;
		if(check==1) printf("Game has not completed\n");
		else printf("Draw\n");
		
		
		
		
		
	}
}
