#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

#define MS(a,b) memset(a,b,sizeof(a));

struct vec
{
	int x,y,z;
};

vec pos[600],vel[600];

#define eps 1e-9

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1;t<=T;t++)
	{
		MS(pos,0);
		MS(vel,0);
		int N;
		double a,b,c,m,n,p;
		a=b=c=m=n=p=0;
		cin>>N;
		for (int i=0;i<N;i++)
		{
			cin>>pos[i].x>>pos[i].y>>pos[i].z>>vel[i].x>>vel[i].y>>vel[i].z;
			a+=pos[i].x;
			b+=pos[i].y;
			c+=pos[i].z;
			m+=vel[i].x;
			n+=vel[i].y;
			p+=vel[i].z;
		}
		a/=N;
		b/=N;
		c/=N;
		m/=N;
		n/=N;
		p/=N;
		double A=m*m+n*n+p*p,B=2*(a*m+b*n+c*p),C=a*a+b*b+c*c;
		double px=-B/(2*A);
		double py=A*px*px+B*px+C;
		if (py<0)
			py=0;
		cout<<"Case #"<<t<<": ";
		if (px>=0)
			cout<<fixed<<setprecision(9)<<sqrt(py)<<' '<<px<<endl;
		else
			cout<<fixed<<setprecision(9)<<sqrt(C)<<" 0.0"<<endl;
	}
	return 0;
}