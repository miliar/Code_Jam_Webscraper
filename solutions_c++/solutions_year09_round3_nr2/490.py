#include <iostream>
#include <math.h>
using namespace std;

int x[3][500];
int v[3][500];
int n;

int xa[3],vxa[3];
int dx,dy;

void Compute()
{
	for (int i=0; i<3; i++)
	{
		xa[i]=vxa[i]=0;
	}
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<3; j++)
		{
			xa[j]+=x[j][i];
			vxa[j]+=v[j][i];
		}
	}
}

double GetMinTime()
{
	double d=0;
	double zz=0;
	for (int i=0; i<3; i++)
	{
		d+=(double)vxa[i]*(double)vxa[i];
		zz+=(double)xa[i]*(double)vxa[i];
	}
	if(zz>=0)
		return 0;
	dx=zz;
	dy=d;
	//cout<<dx<<" "<<dy<<endl;
	return -zz/d;
}

double GetMinDis(double t)
{
	if (t==0)
	{
		double res=0;
		for (int i=0; i<3; i++)
		{
			res+=(double)xa[i]*(double)xa[i];
		}
		return sqrt(res)/n;
	}
	double res=0;
	for (int i=0; i<3; i++)
	{
		res+=(xa[i]+vxa[i]*t)*(xa[i]+vxa[i]*t);
	}
	return sqrt(res)/n;
}

void Resolve(int index)
{
	cin>>n;
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<3; j++)
		{
			cin>>x[j][i];
		}
		for (int j=0; j<3; j++)
		{
			cin>>v[j][i];
		}
	}
	Compute();
	double t=GetMinTime();
	double d=GetMinDis(t);
	printf("Case #%d: %.8f %.8f\n", index, d,t);
}
int main()
{
	FILE* ff=freopen("j:\\B-large.in", "r", stdin);
	FILE* f=freopen("j:\\out1.txt", "w", stdout);
	int testCase;
	cin>>testCase;
	for (int i=1; i<=testCase; i++)
	{
		Resolve(i);
	}
}