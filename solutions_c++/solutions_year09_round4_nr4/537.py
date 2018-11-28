#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<cmath>

using namespace std;

int main()
{
	freopen("output.txt","w",stdout);
	int i,j,l,n,t;
	double a[10][3];
	double d1,d2,mn;
	cin>>t;
	for(l=0;l<t;++l)
	{
		cout<<"Case #"<<l+1<<": ";
		cin>>n;
		for(i=0;i<n;++i)
			cin>>a[i][0]>>a[i][1]>>a[i][2];
		if(n==1)
		{
			printf("%.7lf\n",a[0][2]);
			continue;
		}
		if(n==2)
		{
			d1=a[0][2];
			d2=a[1][2];
			if(d1<d2)
				d1=d2;
			printf("%.7lf\n",d1);
			continue;
		}
		if(n==3)
		{
			d1=sqrt( (a[0][0]-a[1][0])*(a[0][0]-a[1][0])+(a[0][1]-a[1][1])*(a[0][1]-a[1][1]));
			d1+=a[0][2]+a[1][2];
			d1/=2;
			d2=a[2][2];
			if(d1<d2)
				d1=d2;
			mn=d1;
			d1=sqrt( (a[2][0]-a[1][0])*(a[2][0]-a[1][0])+(a[2][1]-a[1][1])*(a[2][1]-a[1][1]));
			d1+=a[2][2]+a[1][2];
			d2=a[0][2];
			d1/=2;
			if(d1<d2)
				d1=d2;
			if(d1<mn)
				mn=d1;
			d1=sqrt( (a[0][0]-a[2][0])*(a[0][0]-a[2][0])+(a[0][1]-a[2][1])*(a[0][1]-a[2][1]));
			d1+=a[0][2]+a[2][2];
			d2=a[1][2];
			d1/=2;
			if(d1<d2)
				d1=d2;
			if(d1<d2)
				d1=d2;
			if(d1<mn)
				mn=d1;
			printf("%.7lf\n",mn);
			continue;
		}
		cout<<"WFT\n";
	}
	return 0;
}