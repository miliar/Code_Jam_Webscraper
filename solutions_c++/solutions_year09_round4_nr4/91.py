#include<iostream>
#include<iomanip>
#include<math.h>
#include<fstream>
using namespace std;

double x[101],y[101],r[101];

double dis(int a,int b)
{
	return sqrt((x[a]-x[b])*(x[a]-x[b]) + (y[a]-y[b])*(y[a]-y[b]));
}

int main()
{
	ifstream cin("D.in");
	ofstream cout("D.out");
	cout<<fixed<<setprecision(10);
	int T;
	cin>>T;
	for(int c=1;c<=T;c++)
	{
	int n;
	cin>>n;
		//cout<<n<<endl;
	for(int i=1;i<=n;i++)
	{
		cin>>x[i]>>y[i]>>r[i];
		//cout<<x[i]<<" , "<<y[i] <<" , "<<r[i]<<endl;
	}
	double res=10000;
		if(n == 3)
		{
	res = min(res ,max( dis(1,2) + r[1] + r[2] , r[3]*2));
	res = min(res ,max( dis(3,2) + r[3] + r[2] , r[1]*2));
	res = min(res , max (dis(1,3) + r[1] + r[3] , r[2]*2) );
		}
	if(n < 3)
	{
		res = 0;
		for(int i=1;i<=n;i++)
			res = max(res, r[i]);
		res *= 2;
	}
	cout<<"Case #"<<c<<": "<<res/2<<endl;
	}
	return 0;
}
