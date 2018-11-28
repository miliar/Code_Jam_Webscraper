#include <stdio.h>
#include <math.h>

void input();
void process();
int flen(int x);
int f(int x, int len);
void output(int t);

int a, b,num;

int main()
{
	int i, t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(i=1; i<=t; i++)
	{
		input();
		process();
		output(i);
	}
	fclose(stdin);
	fclose(stdout);
}

void input()
{
	num=0;
	scanf("%d %d",&a,&b);
}

void process()
{
	int i,len;
	for(i=a; i<=b; i++)
	{
		len = flen(i);
		num+=f(i,len);
	}
}

int flen(int x)
{
	int i,n=1;
	for(i=0; ;i++)
	{
		if(x/n==0)break;
		n*=10;
	}
	return i-1;
}

int f(int x, int len)
{
	int i,y=x,ii,iii,po,nn=0;
	po=pow((double)10,len);
	for(i=1; i<=len; i++)
	{
		ii=y/po;
		iii=(y%po)/(po/10);
		y=(y%po)*10+ii;
		if(y>x && y<=b && iii!=0)nn++;
	}
	return nn;
}

void output(int t)
{
	printf("Case #%d: %d\n",t,num);
}
