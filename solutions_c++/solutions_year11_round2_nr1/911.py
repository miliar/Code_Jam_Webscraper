#include<iostream>
#include<stdio.h>
using namespace std;
char map[105][105];
double wp[105];
double owp[105];
double oowp[105];
double ans[105];
void workwp(int n)
{
	int i,j;
	int sum,win;
	for(i=0;i<n;i++)
	{
		sum=0;
		win=0;
		for(j=0;j<n;j++)
		{
			if(map[i][j]=='1')
			{	win++;sum++;}
			if(map[i][j]=='0')
				sum++;
		}
		wp[i]=1.0*win/sum;
	}
}
void workowp(int n)
{
	int i,j;
	int nn,win,k,sum;
	double wwp;
	for(i=0;i<n;i++)
	{
		nn=0;
		wwp=0;
		for(j=0;j<n;j++)
		{
			if(j==i)continue;
			if(map[j][i]=='.')continue;
			nn++;
			win=sum=0;
			for(k=0;k<n;k++)
			{
				if(k==i)continue;
				if(k==j)continue;
				if(map[j][k]=='1')
				{	win++;sum++;}
				if(map[j][k]=='0')
					sum++;
			}
			wwp+=1.0*win/sum;
		}
		owp[i]=wwp/nn;
	}
}
void workoowp(int n)
{
	int i,j;
	int nn;
	double sum;
	for(i=0;i<n;i++)
	{
		nn=0;
		sum=0;
		for(j=0;j<n;j++)
		{
			if(map[i][j]=='.')continue;
			sum+=owp[j];
			nn++;
		}
		oowp[i]=sum/nn;
	}
}
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-L.out","w",stdout);
	int ct,n;
	int tt=0;
	int i,j;
	scanf("%d",&ct);
	while(ct--)
	{
		scanf("%d",&n);
		getchar();
		for(i=0;i<n;i++)
			gets(map[i]);
		workwp(n);
		workowp(n);
		workoowp(n);
		for(i=0;i<n;i++)
		{
			ans[i]=0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		}
		printf("Case #%d:\n",++tt);
		for(i=0;i<n;i++)
			printf("%.7lf\n",ans[i]);
	}
	return 0;
}