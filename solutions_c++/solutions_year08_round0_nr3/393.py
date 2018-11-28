#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;

pair<double,double> Inter(pair<double,double> a, pair<double,double> b, double r)
{
	double x0=a.first;
	double y0=a.second;

	double k=b.first-x0;
	double l=b.second-y0;

	double A=k*k+l*l;
	double B=2*(x0*k+y0*l);
	double C=-(r*r-x0*x0-y0*y0);

	double t1=(-B+sqrt(B*B-4.0*A*C))/(2.0*A);
	double t2=(-B-sqrt(B*B-4.0*A*C))/(2.0*A);

	double t=t1;
	if (t1<0.0 || t1>1.0)
		t=t2;

	double X=x0+t*k;
	double Y=y0+t*l;
	return make_pair(X,Y);
}

double A(double x1, double y1, double x2, double y2, double r)
{
	if (x2*x2+y2*y2<=r*r)
		return (x2-x1)*(y2-y1);
	
	vector<pair<double,double> > X;
	X.push_back(make_pair(x1,y1));
	X.push_back(make_pair(x2,y1));
	X.push_back(make_pair(x2,y2));
	X.push_back(make_pair(x1,y2));

	vector<pair<double,double> > Y,I;

	for(int i=0;i<X.size();++i)
	{
		int j=(i+1)%X.size();
		bool b1=X[i].first*X[i].first+X[i].second*X[i].second <= r*r;
		bool b2=X[j].first*X[j].first+X[j].second*X[j].second <= r*r;

		if (b1 && b2)
		{
			Y.push_back(X[j]);
		}
		else
			if (b1 && !b2)
			{
				pair<double,double> inter = Inter(X[i],X[j],r);
				Y.push_back(inter);
				I.push_back(inter);
			}
			else
				if (!b1 && b2)
				{
				pair<double,double> inter = Inter(X[i],X[j],r);
				Y.push_back(inter);
				Y.push_back(X[j]);
				I.push_back(inter);
				}
				else
				{
				}
	}

	double area=0.0;

	for(int i=0;i<Y.size();++i)
	{
		int j=(i+1)%Y.size();
		double x1=Y[i].first;
		double y1=Y[i].second;
		double x2=Y[j].first;
		double y2=Y[j].second;

		double tmp=(x2-x1)*(y1+y2)/2.0;

		area+=tmp;
	}

	area=fabs(area);

	if (I.size()==2)
	{
		double x1=I[0].first;
		double y1=I[0].second;
		double x2=I[1].first;
		double y2=I[1].second;

		double cs=x1*x2+y1*y2;
		cs/=sqrt(x1*x1+y1*y1);
		cs/=sqrt(x2*x2+y2*y2);

		double a = acos(cs);
		double tmp=r*r*a/2.0;
		tmp-=fabs(x1*y2-x2*y1)/2.0;

		area+=tmp;
	}

	if (area>(x2-x1)*(y2-y1))
		area=area;

	return area;
}

int main()
{
	int n;
	cin >> n;
	for(int qq=0;qq<n;++qq)
	{
		double f,R,t,r,g;
		cin >> f >> R >> t >> r >> g;

		double rad = R-t-f;

		g-=2.0*f;
		r+=f;

		if (g<=0.0)
		{
			cout << "Case #"<<qq+1<<": " << "1.000000"<< endl;
			continue;
		}

		double area=0.0;
		for(int i=0;i<100+rad/(g+2.0*r);++i)
			for(int j=0;j<100+rad/(g+2.0*r);++j)
			{
				double x1=r+i*(g+2.0*r);
				double y1=r+j*(g+2.0*r);

				double x2=x1+g;
				double y2=y1+g;

				if (x1*x1+y1*y1>=rad*rad)
					continue;

				area+=A(x1,y1,x2,y2,rad);
			}

		area*=4.0;

		double p = area/(3.1415926*R*R);
		p=1.0-p;

		cout << "Case #"<<qq+1<<": ";
		cout << int(p);
		cout << ".";
		p-=int(p);
		for(int i=0;i<6;++i)
		{
			p=p*10.0;
			cout << int(p);
			p-=int(p);
		}
		cout << endl;
	}

	return 0;
}
