#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "B-large(2)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

int u[256],mas[200];
char s[100];

double f(double t, double a, double b)
{
	return t*a+b;
}

double dst(double x, double y, double z)
{
	return sqrt(x*x +y*y +z*z);
}

int main()
{

	init();

	int c;
	scanf("%d\n",&c);
	int cas=1;

	for (int cas=0;cas<c;cas++)
	{
		int n;
		scanf("%d",&n);
		double ax=0,ay=0,az=0,bx=0,by=0,bz=0,x,y,z,vx,vy,vz;
		for (int i=0;i<n;i++){
			scanf("%lf %lf %lf %lf %lf %lf",&x,&y,&z,&vx,&vy,&vz);
			ax+=vx;
			ay+=vy;
			az+=vz;
			bx+=x;
			by+=y;
			bz+=z;
		}

		ax/=n; ay/=n; az/=n;
		bx/=n; by/=n; bz/=n;

		double l=0, r= 1e8;
		double res=1e20;
		for (int st=1;st<=1000;st++)
		{
			double l1=l+(r-l)/3;
			double r1=l+2*(r-l)/3;
			double xl = f(l1,ax,bx);
			double yl = f(l1,ay,by);
			double zl = f(l1,az,bz);

			double xr = f(r1,ax,bx);
			double yr = f(r1,ay,by);
			double zr = f(r1,az,bz);

			double dl = dst(xl,yl,zl);
			double dr = dst(xr,yr,zr);
			if (dl <= dr) r=r1; else l=l1;		
			res = min(res,dl);
			res = min(res,dr);
		}
		
		
		printf("Case #%d: %.6lf %.6lf\n",cas+1,res,l);	
	}


  

   return 0; 
}
