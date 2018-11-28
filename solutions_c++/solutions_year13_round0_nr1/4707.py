#include<iostream>
#include<stdio.h>
using namespace std;
char a[10][10];
bool check1(char p)
{
	int i,j,t1;
	bool d;
	for(i=1;i<=4;i++)
	{
		t1=0;
		d=false;
		for(j=1;j<=4;j++)
		{
			if (a[i][j]==p) t1++;
			if (a[i][j]=='T') d=true;
		}
		if (t1==4||(t1==3&&d))  return true;
	}
	for(i=1;i<=4;i++)
	{
		t1=0;
		d=false;
		for(j=1;j<=4;j++)
		{
			if (a[j][i]==p) t1++;
			if (a[j][i]=='T') d=true;
		}
		if (t1==4||(t1==3&&d))  return true;
	}
	t1=0;
	d=false;
	for(i=1;i<=4;i++)
	{
		if (a[i][i]==p)  t1++;
		if (a[i][i]=='T')  d=true;
	}
	if (t1==4||(t1==3&&d))  return true;
	t1=0;
	d=false;
	for(i=1;i<=4;i++)
	{
		if (a[i][5-i]==p)  t1++;
		if (a[i][5-i]=='T')  d=true;
	}
	if (t1==4||(t1==3&&d))  return true;
	return false;
}
bool check2()
{
	int i,j;
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			if (a[i][j]=='.')  return false;
	return true;

}
int main()
{
	int i,j,n,k;
	char p[100];
//	freopen("1.txt","r",stdin);freopen("2.txt","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.txt","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.txt","w",stdout);
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=4;j++)
		{
			scanf("%s",p);
			for(k=0;k<4;k++)
				a[j][k+1]=p[k];
		}
		if  (check1('X'))  {printf("Case #%d: X won\n",i);continue;}
		if  (check1('O'))  {printf("Case #%d: O won\n",i);continue;}
		if  (check2())     {printf("Case #%d: Draw\n",i);continue;}
		printf("Case #%d: Game has not completed\n",i);
	}
	return 0;
}