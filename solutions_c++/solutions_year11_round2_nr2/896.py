#include <cstdio>
#include <iostream>
using namespace std;

int c,d,p[210],v[210];

bool check(double t)
{
	double lp;
	int i,j;
	lp=p[0]-t;
	for(i=0;i<c;i++)
	{
		if(i==0)
			j=1;
		else
			j=0;
		for(;j<v[i];j++)
		{
			if(lp+d<p[i])
				lp=max(lp+d,p[i]-t);
			else
			{
				if(lp+d-p[i]>t)
					return false;
				lp=lp+d;
			}
		}
	}
	return true;
}

int main()
{
	FILE *fin=freopen ("p.in","r",stdin);
	FILE *fout=freopen ("p.out","w",stdout);

	int T,t;
	int i;

	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>c>>d;

		for(i=0;i<c;i++)
		{
			cin>>p[i]>>v[i];
		}
		double s,e,m;
		bool b;
		s=0.0;
		e=1000000000.0;//3'alat
		while(e-s>0.0000001)
		{
			m=(s+e)/2.0;
			b=check(m);

			if(b)
				e=m;
			else
				s=m;
		}
		//cout<<"Case #"<<t<<": "<<s<<endl;
		fprintf (fout,"Case #%d: %.7f\n",t,s);
	}
	return 0;
}