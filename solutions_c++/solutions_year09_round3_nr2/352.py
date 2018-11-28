#include<iostream>
#include<cmath>
using namespace std;
double sq(double x)
{
	return x*x;
}
main()
{	
	int cas=1,test,x[5001],y[5001],z[5001],vx[5001],vy[5001],vz[5001],i;
	cin>>test;
	while(test--)
	{
		int n;
		int k1=0,k2=0,k3=0,k4=0,k5=0,k6=0;
		cin>>n;
//		cout<<n<<endl;
		for(i=0;i<n;i++)
		{
			cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
//			cout<<x[i]<<y[i]<<z[i]<<vx[i]<<vy[i]<<vz[i];
			k1+=x[i];
			k2+=vx[i];
			k3+=y[i];
			k4+=vy[i];
			k5+=z[i];
			k6+=vz[i];
		}
		double t=(-1.0*(k1*k2+k3*k4+k5*k6));
		if((k2*k2+k4*k4+k6*k6)==0)
		t=0;
		else		
		t=t/(k2*k2+k4*k4+k6*k6);
		if(t<0)
		t=0;
		double ans=0;
		ans=sq(k1+t*k2)+sq(k3+t*k4)+sq(k5+t*k6);
		ans=sqrt(ans);
		ans=ans/n;
		printf("Case #%d: %lf %lf\n",cas,ans,t);
		cas++;
	}
}
		
		
