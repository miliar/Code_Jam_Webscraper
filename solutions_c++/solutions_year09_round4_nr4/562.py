#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

#define MAXN 100

int n;
double ans,x[MAXN],y[MAXN],r[MAXN];

inline double sqr(double a)
{
	return a*a;
}

inline double Far(int a,int b)
{
	return sqrt(sqr(x[a]-x[b])+sqr(y[a]-y[b]));
}

inline double max(double a,double  b)
{
	return a>b?a:b;
}

void run()
{
	if (n==1)
	{
		ans=r[1];
		return;
	}
	if (n==2)
	{
		ans=max(r[1],r[2]);
		return;
	}
	//n==3
	/*CASE 1: One Circle cover 3 plants
	int mx,my;
	mx=(x[1]+x[2]+x[3])/3;
	my=(y[1]+y[2]+y[3])/3;
	if (
	*/
	int a,b,c;
	ans=1e20;
	for (a=1;a<=3;a++)
		for (b=a+1;b<=3;b++)
		{
			if (a==1 && b==2) c=3;
			if (a==1 && b==3) c=2;
			if (a==2 && b==3) c=1;
			if (max((Far(a,b)+r[a]+r[b])/2,r[c])<ans)
				ans=max((Far(a,b)+r[a]+r[b])/2,r[c]);
		}
}

void ini()
{
	int i,k,T;
	cin>>T;
	for (k=1;k<=T;k++)
	{
		ans=0;
		cin>>n;
		for (i=1;i<=n;i++)
		{
			cin>>x[i]>>y[i]>>r[i];
		}
		run();
		printf("Case #%d: %.6lf\n",k,ans);
	}
}


int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	ini();
	return 0;
}
