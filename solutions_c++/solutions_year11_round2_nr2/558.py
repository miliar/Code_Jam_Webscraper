#include<iostream>
#include<vector>
#include<cmath>
using namespace std;

#define MAXN 100001

int t,c,d,n;
double l,r,m;
int p[MAXN],v[MAXN];

bool Check(double m)
{
	double pos=0;
	for(int i=0;i<c;++i)
	{
		for(int j=0;j<v[i];++j)
		{
			if(i==0&&j==0)
			{
				pos=p[0]-m+d;
			}
			else
			{
				double a,b;
				a=p[i]-m;
				b=p[i]+m;
				if(pos<=a)
				{
					pos=a+d;
				}
				else if(a<=pos&&pos<=b)
				{
					pos=pos+d;
				}
				else
				{
					return false; 
				}
			}
		}
	}
	return true;
}

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);
	//freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int ca=1;ca<=t;++ca)
	{
		cin>>c>>d;
		for(int i=0;i<c;++i)
		{
			cin>>p[i]>>v[i];
		}

		Check(2.5);

		l=0;
		r=1e7;
		while(fabs(r-l)>1e-7)
		{
			m=(l+r)/2;
			if(Check(m))
			{
				r=m;
			}
			else
			{
				l=m;
			}
		}

		printf("Case #%d: %.7lf\n",ca,r);
	}
	return 0;
}
