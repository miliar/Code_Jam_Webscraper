#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
typedef long long LL;
using namespace std;

struct pt{
	double x,y,z;
	pt(double _x=0,double _y=0, double _z=0){
		x=_x; y=_y; z=_z;
	}
	pt operator + (const pt &a){
		return pt(x+a.x,y+a.y,z+a.z);
	}
	pt operator * (const double &a){
		return pt(x*a,y*a,z*a);
	}
	double dot(const pt &a){
		return x*a.x+y*a.y+z*a.z;
	}
	void output(){
		printf("(%lf,%lf,%lf)\n",x,y,z);
	}
};

const int N=1000;
int n;
pt A[N],V[N];

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int cas,ic;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++) scanf("%lf%lf%lf%lf%lf%lf",&A[i].x,&A[i].y,&A[i].z,&V[i].x,&V[i].y,&V[i].z);
		pt aa(0,0,0);
		pt vv(0,0,0);
		for(i=0;i<n;i++){
			aa=aa+A[i];
			vv=vv+V[i];
		}
		aa=aa*(1./n);
		vv=vv*(1./n);
		//aa.output(); vv.output();
		double a=vv.dot(vv);
		double b=aa.dot(vv);
		double c=aa.dot(aa);
		//printf("%lf %lf %lf\n",a,b,c);
		double dm,tm;
		if(fabs(a)<1e-11){
			tm=0;
			dm=c;
		}
		else{
			if(b<-1e-11){
				//printf("here\n");
				tm=-b/a;
				dm=a*tm*tm+2*b*tm+c;
				//printf("%lf\n",dm);
			}
			else{
				tm=0;
				dm=c;
			}
		}
		if(dm<1e-11) dm=0;
		printf("Case #%d: %.10lf %.10lf\n",ic,sqrt(dm),tm);
	}
	return 0;
}
