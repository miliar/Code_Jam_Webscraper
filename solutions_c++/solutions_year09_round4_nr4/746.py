#include <iostream>
#include <string>
#include <queue>
#include <iomanip>
#include <map>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
struct circle
{
	int x,y,r;
}p[50];
double dis(int a,int b)
{
	double xx=p[a].x-p[b].x;
	double yy=p[a].y-p[b].y;
	return sqrt(xx*xx+yy*yy)+p[a].r+p[b].r;
}
int main()
{
	int t;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		int n;
		cin>>n;
		for (int j=0;j<n;j++)
			cin>>p[j].x>>p[j].y>>p[j].r;
		cout<<"Case #"<<i<<": ";
		if (n==1)
			cout<<setiosflags (ios::fixed)<<setprecision (6)<<p[0].r<<endl;
		else if (n==2)
		{
			int q;
			if (p[0].r>p[1].r) q=p[0].r;
			else q=p[1].r;
			cout<<setiosflags (ios::fixed)<<setprecision (6)<<q<<endl;
		}
		else
		{
			double a,b,c;
			a=dis(0,1);
			b=dis(0,2);
			c=dis(1,2);
			if (a>b) a=b;
			if (a>c) a=c;
			a/=2;
			for (int o=0;o<3;o++)
				if (a<p[o].r)
					a=p[o].r;
			cout<<setiosflags (ios::fixed)<<setprecision (6)<<a<<endl;
		}

	}

}