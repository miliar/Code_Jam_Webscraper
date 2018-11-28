#include<iostream>
#include<cmath>
#include<vector>
#include<cstring>
#include<algorithm>
#include<stdio.h>
using namespace std;
struct A{int p;double s;}a[22222];

int pt(A a, A b)
{
	return a.p<b.p;
}
int n;
double d;
int ok(double z)
{
	//cout<<n<<endl;
	double p=a[0].p-z,p2;
	for(int i=0;i<n;i++)
	{
		p=max(p,a[i].p-z);
		p2=p+d*(a[i].s-1);
	//	cout<<i<<"    "<<p<<"  "<<p2<<"   "<<endl;
		if(p2>a[i].p+z)
		{
			return 0;
		}
		p=p2+d;
	}
	return 1;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		cin>>n>>d;
		for(int i=0;i<n;i++)
			cin>>a[i].p>>a[i].s;
		
		sort(a,a+n,pt);
		//ok(2.84217);while(1);
		double mid,l=0,r=1e14;
		for(int z=0;z<19999;z++)
		{

			mid=(l+r)/2;
			//cout<<mid<<endl;
			if(ok(mid))r=mid;
			else l=mid;
		}
		printf("Case #%d: %.8lf\n",cas++,l);
	
	}
}