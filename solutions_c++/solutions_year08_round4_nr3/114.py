#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;

#define MAX 1005
#define EPS 1e-7

int n;
double p[MAX];

struct pt{
	double x,y,z;
	pt(double _x=0,double _y=0,double _z=0){
		x=_x;y=_y;z=_z;
	}
	void scan(){
		scanf("%lf%lf%lf",&x,&y,&z);
	}
	pt operator+(pt a){
		return pt(x+a.x , y+a.y , z+a.z );
	}
}s[MAX];

struct Bor{
	pt A,B,C,D,E,F;
	pt G;
	double d;

	void create(pt cen,double g){
		A = cen + pt(g,0,0);
		B = cen + pt(0,g,0);
		C = cen + pt(-g,0,0);
		D = cen + pt(0,-g,0);
		E = cen + pt(0,0,g);
		F = cen + pt(0,0,-g);
		G = cen;
		d = g;
	}
}b[MAX];

bool isect(Bor &p,Bor &q){

	double dd;

	dd = fabs(p.G.x - q.G.x)  +fabs(p.G.y - q.G.y) + fabs(p.G.z - q.G.z) ;

	if(dd < p.d + q.d || fabs(dd-p.d-q.d) < EPS)
		return 1;
	return 0;
}

bool solve(double m){
	int i,j;

	for(i=0;i<n;i++)
		b[i].create(s[i],m*p[i]);

	for(i=0;i<n;i++)
		for(j=i+1;j<n;j++)
			if( !isect(b[i],b[j]) )
				return 0;
	return 1;
}

int main(){
	double lo,hi,m;

	int T,N,i;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%d",&n);

		for(i=0;i<n;i++){
			s[i].scan();
			scanf("%lf",&p[i]);
		}
			

		lo = 0;
		hi = 10000000;

		while(hi-lo > EPS){
			m = (hi+lo)/2;

			if(solve(m))
				hi=m;
			else
				lo=m;
		}

		printf("Case #%d: %.6lf\n",N,m);
	}
	return 0;
}