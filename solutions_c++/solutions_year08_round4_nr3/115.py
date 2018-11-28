#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<ctime>

using namespace std;

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

#define EPS 1e-6
#define INF 1000000000
double xx[102],yy[102],zz[102],pp[102];
int N;
double maxX,maxY,maxZ;

double check(double Z,double Y,double X)
{
	double ret=0.0;
	int i;
	for(i=0;i<N;i++)
	{
		double R=fabs(xx[i]-X)+fabs(yy[i]-Y)+fabs(zz[i]-Z);
		R/=pp[i];
		ret=MAX(ret,R);
	}
	return ret;
}

double TernaryZ(double Y,double X)
{
	double lo=0.0,hi=maxZ,minL=INF;

	while(hi-lo>EPS)
	{
		double left = (2.0*lo + hi)/3.0;
		double right= (lo + 2.0*hi)/3.0;

		double l1=check(left,Y,X);
		double l2=check(right,Y,X);

		if(l1<minL) minL=l1;
		if(l2<minL) minL=l2;
		
		if(l1>l2)
			lo=left;
		else 
			hi=right;
	}
	return minL;
}

double TernaryY(double X)
{
	double lo=0.0,hi=maxY,minL=INF;

	while(hi-lo>EPS)
	{
		double left = (2.0*lo + hi)/3.0;
		double right= (lo + 2.0*hi)/3.0;

		double l1=TernaryZ(left,X);
		double l2=TernaryZ(right,X);

		if(l1<minL) minL=l1;
		if(l2<minL) minL=l2;

		if(l1>l2)
			lo=left;
		else 
			hi=right;
	}
	return minL;
}

int main()
{
	int i,j,k,tests,cs=0;

	//freopen("C:\\.in","r",stdin);
	freopen("C:\\Csmall.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		scanf("%d",&N);

		for(i=0;i<N;i++)
			scanf("%lf %lf %lf %lf",&xx[i],&yy[i],&zz[i],&pp[i]);

		maxX=maxY=maxZ=0.;

		for(i=0;i<N;i++)
		{
			maxX=MAX(maxX,xx[i]);
			maxY=MAX(maxY,yy[i]);
			maxZ=MAX(maxZ,zz[i]);

		}

		maxX=maxY=maxZ=1e6;

	
		double lo=0.0,hi=maxX,minL=INF;

		while(hi-lo>EPS)
		{
			double left = (2.0*lo + hi)/3.0;
			double right= (lo + 2.0*hi)/3.0;
			
			double l1=TernaryY(left);
			double l2=TernaryY(right);
			 
			if(l1<minL) minL=l1;
			if(l2<minL) minL=l2;
			
			if(l1>l2)
				lo=left;
			else 
				hi=right;
		}

		printf("Case #%d: %.6lf\n",++cs,minL);
		
	}
	return 0;
}