#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <list>
using namespace std;
int n;
int x[500];
int y[500];
int z[500];
int vx[500];
int vy[500];
int vz[500];
double calc(double t){
	double xs=0,ys=0,zs=0;
	for(int i=0;i<n;i++){
		xs+=t*vx[i]+x[i];
		ys+=t*vy[i]+y[i];
		zs+=t*vz[i]+z[i];
	}
	xs/=n;
	ys/=n;
	zs/=n;
	return sqrt(xs*xs+ys*ys+zs*zs);
}
int main() {
	freopen("B-small-attempt3.in","rt",stdin);
	freopen("B-small-attempt3.out","wt",stdout);
	int N;
	cin>>N;
	for(int nn=0;nn<N;nn++){
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
		double A=0,B=1e9;
		for(int xx=0;xx<1000;xx++)
		{
			double p1=A+((B-A)/3);
			double p2=A+((2*(B-A))/3);
			double v1=calc(p1);
			double v2=calc(p2);
			if(v1>v2)
				A=p1;
			else
				B=p2;
		}
		if(calc(0)-1e-5<calc(A))
			A=0;
		printf("Case #%d: %.7lf %.7lf\n",nn+1,calc(A),A);
	}
	return 0;
}
