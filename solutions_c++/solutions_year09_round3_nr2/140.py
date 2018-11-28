#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;

double k1,k2,k3,k4,k5,k6,t,d;

ifstream ci("b2.in");
ofstream co("b2.out");

int main()
{
	int T,N;
	ci>>T;
	for (int t1=0;t1<T;++t1)
	{
		ci>>N;
		double a,b,c,d,e,f;
		k1=0;
		k2=0;
		k3=0;
		k4=0;
		k5=0;
		k6=0;
		for (int i=0;i<N;++i)
		{
			ci>>a>>b>>c>>d>>e>>f;
			k1+=a;
			k2+=b;
			k3+=c;
			k4+=d;
			k5+=e;
			k6+=f;
		}
		if ((k4*k4+k5*k5+k6*k6)!=0)
		t=-(k4*k1+k5*k2+k6*k3)/(k4*k4+k5*k5+k6*k6);
		else
			t=0;
		if (t<0)
			t=0;
		d=(k1+k4*t)*(k1+k4*t)+(k2+k5*t)*(k2+k5*t)+(k3+k6*t)*(k3+k6*t);
		d=sqrt(d)/N;
		co<<"Case #"<<t1+1<<": "<<setiosflags(ios::fixed)<<setprecision(8)<<d<<" "<<setprecision(8)<<t<<endl;
	}
	return 0;
}