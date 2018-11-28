#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;


double eps = 1e-11;


double A1,A2,A3;
double B1,B2,B3;
bool Read()
{
	int x,y,z,vx,vy,vz;
	int n,i;
	
	A1 = A2 = A3 = 0;
	B1 = B2 = B3 = 0;
	scanf("%d",&n);
	for(i=0;i<n;++i)
	{
		scanf("%d%d%d%d%d%d",&x,&y,&z,&vx,&vy,&vz);
		A1+=x;
		A2+=y;
		A3+=z;
		B1+=vx;
		B2+=vy;
		B3+=vz;
	}
	A1/=n;
	A2/=n;
	A3/=n;
	B1/=n;
	B2/=n;
	B3/=n;
	return true;
}

void Work()
{
	double res;
	double A = B1*B1 + B2*B2 + B3*B3;
	double B = 2*(A1*B1 + A2*B2 + A3*B3);
	double C = A1*A1 + A2*A2 + A3*A3;
	double Vert = 0;
	if( fabs(A)<eps )
	{
		res = C;
	}
	else
	{
		double min = C;
		Vert = -B;
		Vert/=2;
		Vert/=A;
		double calc = A*Vert*Vert + B*Vert + C;
		
		if( Vert<0 )
		{
			Vert = 0;
			res = min;
		}
		else
		{
			res = calc;
		}
		 
		
	}
	if( res<0 ) res = 0;
	if( Vert<0 ) Vert = 0;
	res = sqrt(res);
	printf("%.8lf %.8lf\n",res,fabs(Vert));
}

void Write()
{
}

int main()
{
	int i=1,n;
scanf("%d",&n);
for(i=0;i<n;++i)
{
	Read();
	printf("Case #%d: ",i+1);
	Work();
	Write();
}
return 0;
}

