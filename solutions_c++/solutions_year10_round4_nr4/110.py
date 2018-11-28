#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


const long double pi=3.1415926535897932384626433832795;

long double calc(long double d,long double r,long double R)
{
    if (d>=R+r) return 0;
    if (r>R) swap(r,R);
    if (d<=R-r) return pi*r*r;
    long double A=acos((R*R+d*d-r*r)/(2.0*R*d))*2;
    long double a=acos((r*r+d*d-R*R)/(2.0*r*d))*2;
    long double sA=R*R*(A-sin(A))/2;
    long double sa=r*r*(a-sin(a))/2;
    return sa+sA;
}

typedef pair<double,double> point;

double dist(point a,point b)
{
	double dx=a.first-b.first;
	double dy=a.second-b.second;
	return sqrt(dx*dx+dy*dy);
}

int n,m;
point p,q;
point bucket;

int caseN;
int main()
{
	cin>>caseN;
	cout.setf(ios::fixed);
	cout.precision(10);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		cin>>n>>m;
		cin>>p.first>>p.second;
		cin>>q.first>>q.second;
		cout<<"Case #"<<caseI<<":";
		while (m--)
		{
			cin>>bucket.first>>bucket.second;
			double r1=dist(bucket,p);
			double r2=dist(bucket,q);
			cout<<' '<<calc(dist(p,q),r1,r2);
		}
		cout<<endl;
	}
	return 0;
}



