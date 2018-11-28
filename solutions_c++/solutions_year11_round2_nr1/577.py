#include<stdio.h>
char data[500][500];
int in;
long double wp[1000],owp[1000],oowp[1000];
long double wpwithout(int x,int wo)
{
	int sum=0,win=0,n;
	for(n=0;n<in;n++)
	{
		if(n==wo)
			continue;
		if(data[x][n]=='1')
		{
			sum++;win++;
		}
		if(data[x][n]=='0')
			sum++;
	}
	return (long double)win/sum;
}
void work()
{
	int n,m;
	scanf("%d",&in);
	for(n=0;n<in;n++)
		scanf("%s",data[n]);
	for(n=0;n<in;n++)
		wp[n]=wpwithout(n,-1);
	for(n=0;n<in;n++)
	{
		int c=0;
		owp[n]=0;
		for(m=0;m<in;m++)
		{
			if(data[n][m]!='.')
			{
				owp[n]+=wpwithout(m,n);
				c++;
			}
		}
		if(c!=0)
		owp[n]/=c;
	}
	for(n=0;n<in;n++)
	{
		int c=0;
		oowp[n]=0;
		for(m=0;m<in;m++)
		{
			if(data[n][m]!='.')
			{
				oowp[n]+=owp[m];
				c++;
			}
		}
		if(c!=0)
		oowp[n]/=c;
	}
	for(n=0;n<in;n++)
	{
		printf("%.15lf\n",(double)(0.25*wp[n]+0.50*owp[n]+0.25*oowp[n]));
	}
}
int main()
{
	int n,ix;
	scanf("%d",&ix);
	for(n=0;n<ix;n++)
	{
		printf("Case #%d:\n",n+1);
		work();
	}
}
