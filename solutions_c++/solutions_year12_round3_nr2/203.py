#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
int main ()
{
	int t;
	scanf ("%d", &t);
	for (int tt=1; tt<=t; tt++)
	{
		printf ("Case #%d:\n", tt);
		double d;
		int n,a;
		scanf ("%lf %d %d", &d, &n, &a);
		double ss=0.0,czass=0.0;
		double pocz=0.0;
		for (int k=0; k<n; k++)
		{
			double e,r;
			scanf ("%lf %lf", &r,&e);
			ss=e-ss;
			czass=r-czass;
			if (k==0) pocz=e;
		}
		double vv=ss/czass;
		double t2=(d-pocz)/vv;
		while (a--)
		{
			double aa;
			scanf ("%lf", &aa);
			double t1=sqrt((2*d)/aa);
			printf ("%.6lf\n", max(t1,t2));
		}
	}

//system ("pause");
return 0;
}
