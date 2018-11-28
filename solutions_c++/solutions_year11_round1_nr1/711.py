#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <iostream>
#include <string.h>
using namespace std;
int d, g, n;
char ch[17];
int gcd(int x, int y)//求x和y的最大公约数
{
	int m, n, t;
	if (x>y) { m=x; n=y; }
	else { m=y; n=x; }
	while (m%n)
	{
		t=n;
		n=m%n;
		m=t;
	}
	return n;
}
void getD(int pd)
{
	int m_gcd=gcd(pd, 100);
	d=100/m_gcd;
}
void getN()
{
	if (strlen(ch)==1) n=ch[0]-'0';
	else n=ch[1]-'0'+(ch[0]-'0')*10;
}
void main()
{
	int i, e, t, pd, pg;
	FILE *rFile=fopen("D:\\A-large.in", "r"); e=ferror(rFile); assert(e==0);
	FILE *wFile=fopen("D:\\R1A-out.txt", "w"); e=ferror(wFile); assert(e==0);
	fscanf(rFile, "%d", &t);
	for (i=0; i<t; i++)
	{
		fscanf(rFile, "%s", ch);
		fscanf(rFile, "%d", &pd);
		fscanf(rFile, "%d", &pg);
		if (pd==0&&pg==0)
		{
			fprintf(wFile, "Case #%d: Possible\n", i+1);
			continue;
		}
		if (pd==0&&pg<100)
		{
			fprintf(wFile, "Case #%d: Possible\n", i+1);
			continue;
		}
		if (pd!=0&&pg==0)
		{
			fprintf(wFile, "Case #%d: Broken\n", i+1);
			continue;
		}
		if (pd==100&&pg==100)
		{
			fprintf(wFile, "Case #%d: Possible\n", i+1);
			continue;
		}
		if (pd!=100&&pg==100)
		{
			fprintf(wFile, "Case #%d: Broken\n", i+1);
			continue;
		}
		if (strlen(ch)>=3) fprintf(wFile, "Case #%d: Possible\n", i+1);
		else
		{
			getN();
			getD(pd);
			if (d<=n) fprintf(wFile, "Case #%d: Possible\n", i+1);
			else fprintf(wFile, "Case #%d: Broken\n", i+1);
		}
	}//for i=0
	fclose(rFile); e=ferror(rFile); assert(e==0);
	fclose(wFile); e=ferror(wFile); assert(e==0);
	system("pause");
}
