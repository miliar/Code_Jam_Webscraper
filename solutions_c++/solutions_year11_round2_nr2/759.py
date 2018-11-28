#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

#define INP_FILE "B-small-attempt0.in"
#define OUT_FILE "output_B-small-attempt0.in.txt"

int n,d;
double v[200],p[200];

bool check(double time)
{
	double border=p[0]-time;
	double cborder;
	for(int i=0;i<n;i++)
	{
		cborder = ((p[i]-time>border)?(p[i]-time):border);
		border=cborder+d*v[i];
		if (border>p[i]+time+d)
			return false;		
	}
	return true;
}

double l,r,m;

int main()
{
	freopen( INP_FILE , "r" , stdin );
	freopen( OUT_FILE , "w" , stdout );
	int tstCnt;
	cin>>tstCnt;

	for(int tst=1;tst<=tstCnt;tst++)
	{
		cin>>n>>d;
		for(int i=0;i<n;i++)
		{
			cin>>p[i]>>v[i];
		}

		if (check(0))
		{
			printf("Case #%d: 0\n",tst);
			continue;
		}

		l=0;
		r=1;
		while ( !check(r))
			r=2*r;
		while(abs(l-r)>0.00000001)
		{
			m=(l+r)/2;
			if (check(m))
				r=m;
			else
				l=m;
		}
		printf("Case #%d: %lf\n",tst,l);
	}
	return 0;
}