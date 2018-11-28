#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <cstring>
#include <cmath>

using namespace std;

double dist(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

double solve(double x1,double y1,double r1,double x2,double y2,double r2)
{
	double rr=dist(x1,y1,x2,y2);
	double a1=2*acos((r1*r1+rr*rr-r2*r2)/(2*r1*rr));
	double a2=2*acos((r2*r2+rr*rr-r1*r1)/(2*r2*rr));
	return 0.5*( a1*r1*r1- r1*r1*sin(a1) + a2*r2*r2 - r2*r2*sin(a2));
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,t,i,j,k,n,m;
	cin>>T;
	double x1,y1,x2,y2;
	for(t=1;t<=T;t++)
	{
		cin>>n>>m;
		double px,py;
		cin>>x1>>y1>>x2>>y2;
		//px=x1;
		//py=y1;
		//x1-=px; y1-=py;
		//x2-=px; y2-=py;

		printf("Case #%d:",t);
		for(i=0;i<m;i++) 
		{
			double xx,yy;
			cin>>xx>>yy;
			//xx-=px; yy-=py;
			printf(" %.8lf",solve(x1,y1,dist(x1,y1,xx,yy),x2,y2,dist(x2,y2,xx,yy)));
		}
		puts("");
	}

	return 0;
}