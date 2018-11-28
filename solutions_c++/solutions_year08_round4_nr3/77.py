#include <cstdio>
#include <algorithm>
#include <iostream>
#include <iomanip>
using namespace std;
int i,j,k,s,t,n,m,I;
long double l,r,mid;
struct node{
	long double pos;
	int nu;
}a[2000];
int T;
long double x[2000],y[2000],z[2000],p[2000];
long double Abs(double x){ if (x<0) return -x; else return x;}
bool cmp(node x,node y)
{
	return x.pos<y.pos-1e-8 || Abs(x.pos-y.pos)<1e-8 && x.nu==0;
}

main()
{
	I=0;
	cin>>T;
	while (T--)
	{
		cin>>n;
		for (i=1;i<=n;++i)
		{
			cin>>x[i]>>y[i]>>z[i]>>p[i];
			//scanf("%Lf%Lf%Lf%Lf",&x[i],&y[i],&z[i],&p[i]);
		}
		double ans=0;
		for (i=1;i<=n;++i)
		for (j=1;j<=n;++j)
		{
			double tmp=(Abs(x[i]-x[j])+Abs(y[i]-y[j])+Abs(z[i]-z[j]))/(p[i]+p[j]);
			if (tmp>ans) ans=tmp;
		}
		cout<<"Case #"<<++I<<": ";
		cout<<setprecision(8);
 		cout<<fixed<<ans<<endl;
		//printf("Case #%d: %.8Lf\n",++I,calc(x)+calc(y)+calc(z));
	}
	return 0;
}
