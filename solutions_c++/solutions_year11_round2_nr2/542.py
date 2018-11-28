#include<iostream>
#include<cmath>
#include<string>
using namespace std;

const double eps = 1e-6;

double p[205],v[205];
int n;
double d;

bool test(double t)
{
	double left = p[0]-t;
	double right;
	for(int i=0;i<n;i++)
	{
		left = max(left,p[i]-t);
		right = left+(v[i]-1)*d;
		if(fabs(right-p[i])>t) return false;
		left = right+d;
	}
	return true;

}

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
//	freopen("1.txt","r",stdin);
	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		cin>>n>>d;
		for(int i=0;i<n;i++)
		{
			cin>>p[i]>>v[i];
		}

		double l=0,r=1e8;
		while(r-l>eps)
		{
			double mid = (l+r)/2;
			if(test(mid)) r = mid;
			else l=mid;
		}

		cout<<"Case #"<<cas<<": "<<l<<'\n';
	}
	return 0;
}