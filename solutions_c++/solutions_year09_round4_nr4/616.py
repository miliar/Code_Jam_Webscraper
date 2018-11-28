#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
#include<complex>
using namespace std;

int main()
{
	int c;
	cin>>c;

	for(int i=1;i<=c;i++)
	{
		int n;
		cin>>n;
		vector<complex<double> > v(n);
		vector<double> rad(n);
		for(int j=0;j<n;j++)
		{
			double a,b;
			cin>>a>>b;
			v[j]=complex<double> (a,b);
			cin>>rad[j];
		}
		double ans;
		if(n==1)
		{
			ans=rad[0];
		}
		if(n==2)
		{
			ans=max(rad[1],rad[0]);

		}
		if(n==3)
		{
			vector<double> r1(3);
			complex <double>diff=v[0]-v[1];
			r1[0]=max((abs(diff)+rad[0]+rad[1])/2.0,rad[2]);
			diff=v[0]-v[2];
			r1[1]=max((abs(diff)+rad[0]+rad[2])/2.0,rad[1]);
			diff=v[1]-v[2];
			r1[2]=max((abs(diff)+rad[1]+rad[2])/2.0,rad[0]);
			ans=*(min_element(r1.begin(),r1.end()));
		}
		printf("Case #%d: %lf\n",i,ans);

	}
	return 0;
}
