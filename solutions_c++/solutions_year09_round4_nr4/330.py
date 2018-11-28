#include <cstdio>
#include <cmath>

double maxi(double a, double b)
{
	if(a>b)return a;
	return b;
}

double mini(double a, double b)
{
	if(a<b)return a;
	return b;
}

void N1()
{
	double x,y,r;
	scanf("%lf %lf %lf",&x,&y,&r);
	printf("%.6lf\n",r);
}

void N2()
{
	double x1,y1,r1;
	scanf("%lf %lf %lf",&x1,&y1,&r1);

	double x2,y2,r2;
	scanf("%lf %lf %lf",&x2,&y2,&r2);

	double r=maxi(r1,r2);

	printf("%.6lf\n",r);
}

double dist(double x1, double y1, double x2, double y2)
{
	double delx=x1-x2;
	double dely=y1-y2;

	return sqrt(delx*delx + dely*dely);
}
double solve(double x1, double y1, double r1, double x2, double y2, double r2)
{
	return (dist(x1,y1,x2,y2) + r1 + r2)/2.0;
}

void N3()
{
	double x[3];
	double y[3];
	double r[3];
	for(int i=0;i<3;i++)
		scanf("%lf %lf %lf",&x[i],&y[i],&r[i]);

	double rx=1000000000;
	//12
	double r12 = maxi(r[0], solve(x[1],y[1],r[1],x[2],y[2],r[2]));
	rx = mini(rx, r12);

	//02
	double r02 = maxi(r[1], solve(x[0],y[0],r[0],x[2],y[2],r[2]));
	rx = mini(rx, r02);

	//01
	double r01 = maxi(r[2], solve(x[0],y[0],r[0],x[1],y[1],r[1]));
	rx = mini(rx, r01);

	printf("%.6lf\n",rx);
}

int main()
{
	freopen("d1in.txt","r",stdin);
	freopen("d1out.txt","w",stdout);


	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int N;
		scanf("%d",&N);
		printf("Case #%d: ",t);
		if(N==1)N1();
		else if(N==2)N2();
		else N3();
	}
}