//In the name of Allah
//
//
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long llong;
#define int llong
int map[1000][1000];
double d1[1000][1000],d2[1000][1000],d3[1000][1000];
int r,c,d,t;
int b=0;
double calc(int a,int b,int c,int d,double  p[1000][1000],int type)
{
	double res=p[c][d];
	if (a!=0)
		res-=p[a-1][d];
	if (b!=0)
		res-=p[c][b-1];
	if (a!=0 && b!=0)
		res+=p[a-1][b-1];
	if (type==1)
	{
		res-=map[a][b];
		res-=map[a][d];
		res-=map[c][b];
		res-=map[c][d];
	}
		if (type==2)
	{
		res-=a*map[a][b];
		res-=a*map[a][d];
		res-=c*map[c][b];
		res-=c*map[c][d];
	}
	if (type==3)
	{
		res-=b*map[a][b];
		res-=d*map[a][d];
		res-=b*map[c][b];
		res-=d*map[c][d];
	}

	return res;
}
bool av(int a,int b,int k)
{
	double m1=a+double(k)/2;
	double m2=b+double(k)/2;
	double tot1=0,tot2=0;
	/*for (int i=a;i<a+k;i++)
		for (int j=b;j<b+k;j++)
			if (!((i==a && j==b) || (i==a && j==b+k-1) || (i==a+k-1 && j==b) || (i==a+k-1 && j==b+k-1)))
			{
				tot1+=(i-m1+0.5)*map[i][j];
				tot2+=(j-m2+0.5)*map[i][j];
			}*/
	tot1=calc(a,b,a+k-1,b+k-1,d1,1)*(0.5-m1)+calc(a,b,a+k-1,b+k-1,d2,2);
	tot2=calc(a,b,a+k-1,b+k-1,d1,1)*(0.5-m2)+calc(a,b,a+k-1,b+k-1,d3,3);
	if (abs(tot1)<=1e-8 && abs(tot2)<=1e-8)
		return 1;
	return 0;
}
 main()
{
	ios::sync_with_stdio(false);
	cin>>t;
	for (int cas=1;cas<=t;cas++)
	{
		cerr<<cas<<endl;
		b=0;
		cin>>r>>c>>d;
		for (int i=0;i<r;i++)
			for (int j=0;j<c;j++)
			{
				char c;
				cin>>c;
				map[i][j]=d+c-'0';
			}
		d1[0][0]=map[0][0];
		for (int i=1;i<c;i++)
			d1[0][i]=d1[0][i-1]+map[0][i];
		for (int i=1;i<r;i++)
		{
			double now=0;
			for (int j=0;j<c;j++)
			{
				now+=map[i][j];
				d1[i][j]=now+d1[i-1][j];
			}
		}
		d2[0][0]=0;
		for (int i=1;i<c;i++)
			d2[0][i]=0;
		for (int i=1;i<r;i++)
		{
			double now=0;
			for (int j=0;j<c;j++)
			{
				now+=i*map[i][j];
				d2[i][j]=now+d2[i-1][j];
			}
		}
		d3[0][0]=0;
		for (int i=1;i<r;i++)
			d3[i][0]=0;
		for (int i=1;i<c;i++)
		{
			double now=0;
			for (int j=0;j<r;j++)
			{
				now+=i*map[j][i];
				d3[j][i]=now+d3[j][i-1];
			}
		}

		for (int k=3;k<=min(r,c);k++)
		{
			for (int c1=0;c1<=r-k;c1++)
				for (int c2=0;c2<=c-k;c2++)
					if (av(c1,c2,k))
					{
						b=k;
						goto end;
					}
end:;
		}
		cout<<"Case #"<<cas<<": ";
		if (b==0)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<b<<endl;
	}
	return 0;
}
