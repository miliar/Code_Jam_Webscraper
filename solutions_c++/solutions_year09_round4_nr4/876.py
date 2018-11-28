#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main()
{
	int c;
	cin>>c;
	for (int q=1;q<=c;q++)
	{
		int f=3;
		cin>>f;
		
		cout<<"Case #"<<q<<": ";
		
		if (f==3){
		double a[10];
		for (int i=0;i<9;i++)
			cin>>a[i];
		double x,y,z;
		x=sqrt((a[3]-a[0])*(a[3]-a[0])+(a[4]-a[1])*(a[4]-a[1]))+a[5]+a[2];
		y=sqrt((a[3]-a[6])*(a[3]-a[6])+(a[4]-a[7])*(a[4]-a[7]))+a[5]+a[8];
		z=sqrt((a[6]-a[0])*(a[6]-a[0])+(a[7]-a[1])*(a[7]-a[1]))+a[8]+a[2];
		//cout<<x<<y<<z<<endl;
		double u=99999;
		u=min(u,x);
		u=min(u,y);
		u=min(u,z);
		u=max(u,a[2]);
		u=max(u,a[5]);
		u=max(u,a[8]);
			cout<<setprecision(8)<<setiosflags(ios::fixed)<<u/2<<endl;}
		else
		{
			double a[10];
			for (int i=0;i<3*f;i++)
				cin>>a[i];
			if (f==1)
				cout<<a[2]<<endl;
			else
				cout<<max(a[2],a[5])<<endl;
		}
	}
	return 0;
}
