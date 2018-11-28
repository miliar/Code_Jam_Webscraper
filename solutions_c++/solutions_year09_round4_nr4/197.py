#include<iostream>
#include<cmath>
using namespace std;
int d[101][101];
double sqr(double a)
{
	return a*a;
}
double Max(double a,double b)
{
	return a>b?a:b;
}
double x[4],y[4],r[4];
int main()
{
	freopen("d-small-attempt1.in","r",stdin);
	freopen("d-small-attempt1.out","w",stdout);
	int css,cs,a,ct,tp,k,i,j,n,m;
	double s12,s13,s23,out;
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
		if(n==1)
		{
			printf("Case #%d: %f\n",css,r[0]);
		}
		else if(n==2)
		{
			printf("Case #%d: %f\n",css,Max(r[0],r[1]));
		}
		else
		{
			s23=Max((sqrt(sqr(x[2]-x[1])+sqr(y[2]-y[1]))+r[2]+r[1])/2,r[0]);
			out=s23;
			s12=Max((sqrt(sqr(x[1]-x[0])+sqr(y[1]-y[0]))+r[0]+r[1])/2,r[2]);
			out<?=s12;
			s13=Max((sqrt(sqr(x[2]-x[0])+sqr(y[2]-y[0]))+r[2]+r[0])/2,r[1]);
			out<?=s13;
			printf("Case #%d: %f\n",css,out);
		}
	}
	return 0;
}
