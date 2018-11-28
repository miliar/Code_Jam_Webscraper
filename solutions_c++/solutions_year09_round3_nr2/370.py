#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	double ai[550][7];
	int n;
	cin>>n;
	int t = 1 ;
	while(t<=n)
	{
		if(t==17)
			t=t;
		int n1;
		cin>>n1;
		int i,j;
		for(i = 0 ; i< n1; i++)
			for(j = 0 ; j < 6; j++)
				cin>>ai[i][j];
		double kx=0,ky=0,kz=0;
		double mx=0,my=0,mz=0;
	    for(i=0 ; i < n1; i++)
		{
			kx+=ai[i][0];
			ky+=ai[i][1];
			kz+=ai[i][2];
			
			mx+=ai[i][3];
			my+=ai[i][4];
			mz+=ai[i][5];
		}
		kx/=n1;
		ky/=n1;
		kz/=n1;
		mx/=n1;
		my/=n1;
		mz/=n1;
		double a=0,b=0,c=0;
		c=kx*kx+ky*ky+kz*kz;
		a=mx*mx+my*my+mz*mz;
		b=2*(kx*mx+ky*my+kz*mz);
		double an1=0,an2=0;
		if(a==0)
			printf("Case #%d: %lf %lf\n",t,c==0?0:sqrt(c),an2);
		else
		{
			double ti = -b/(2*a);
		    if(ti<=0)ti=0;
			//ti*=n1;
			an1=a*ti*ti+b*ti+c;
			if(an1<=0)an1=0;
			else an1=sqrt(an1);
			printf("Case #%d: %lf %lf\n",t,an1,ti);
		}
		t++;
	}



}