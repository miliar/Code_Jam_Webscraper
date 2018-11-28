#include <iostream>
#include <cmath>

using namespace std;

/*bool tri(long long x1, long long x2, long long x3, long long y1, long long y2, long long y3)
{
	return true;
	if((x1==x2 && x2==x3) || (y1==y2 && y2==y3))
		return true;
	double d1=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
	double d2=sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3));
	double d3=sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1));
	if(d1+d2>d3 && d2+d3>d1 && d3+d1>d2)
		return true;
	return false;
}*/

int main()
{
	int t, num;
	long long n, a, b, c, d, x[100000], y[1000000], m;
	cin>>t;
	for(int j=1; j<=t; j++)
	{
		num=0;
		cin>>n>>a>>b>>c>>d>>x[0]>>y[0]>>m;
		for(int i=0; i<n-1; i++)
		{
			x[i+1]=(x[i]*a+b)%m;
			y[i+1]=(y[i]*c+d)%m;
		}
		for(int i=0; i<n; i++)
			for(int j=i+1; j<n; j++)
				for(int k=j+1; k<n; k++)
					if((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0)
						num++;
		cout<<"Case #"<<j<<": "<<num<<endl;
	}
	return 0;
}
