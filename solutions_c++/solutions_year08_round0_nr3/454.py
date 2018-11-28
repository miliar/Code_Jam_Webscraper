#include<stdio.h>
#include<math.h>
#include<vector>
#include<iostream>
using namespace std;
#define LIMIT 1e-11
#define PI 3.141592653589793

struct point{
	double x,y;
};

double sqr(double a){
	return a*a;
}

int inCircle(double x, double y, double r){
	if(x*x+y*y+LIMIT<r*r)
		return 1;
	return 0;
}

int inCircle(double x, double y, double r, vector<point> &vp){
	if(x*x+y*y+LIMIT<r*r){
		point tp={x,y};
		vp.push_back(tp);
		return 1;
	}
	return 0;
}

double dist(point a,point b){
	return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}

double tri(point a,point b,point c){//计算三角形面积
	double l1=dist(a,b);
	double l2=dist(c,b);
	double l3=dist(a,c);
	double m=(l1+l2+l3)/2;
	if(m*(m-l1)*(m-l2)*(m-l3)<LIMIT) return 0;
	return sqrt(m*(m-l1)*(m-l2)*(m-l3));
}

double dian(point a,point b){
	return a.x*b.x+a.y*b.y;
}

double mo(point a){
	return sqrt(a.x*a.x+a.y*a.y);
}

double ang(point a,point b){
	return acos(dian(a,b)/mo(a)/mo(b));
}

int main(){
	int n,nn;
	scanf("%d",&n);
	for(nn=1;nn<=n;nn++){
		double f, R, t, r, g;
		scanf("%lf%lf%lf%lf%lf",&f, &R, &t, &r, &g);
		g-=2*f;
		double rr=R-t-f;
		r+=f;
		double p;
		if(g<=LIMIT || rr<=LIMIT){
			p=1;
		}else{
			double d=g+2*r;
			double escArea=0;
			int num=(int)(ceil(R/d)+LIMIT);
			for(int i=-num;i<num;i++){
				for(int j=-num;j<num;j++){
					double x=i*d+r, y=j*d+r;
					vector<point> vp;
					vector<point> sp;
					int cnt=inCircle(x,y,rr)+inCircle(x+g,y,rr)+inCircle(x,y+g,rr)+inCircle(x+g,y+g,rr);
					if(cnt==4){
						escArea+=g*g;
					}else if(cnt!=0){
						point tp;
						inCircle(x,y,rr,vp);
						if(inCircle(x,y,rr)+inCircle(x+g,y,rr)==1){
							double tmp=sqrt(sqr(rr)-sqr(y));
							if(!(tmp>=x-LIMIT && tmp<=x+g+LIMIT))
								tmp=-tmp;
							tp.x=tmp;
							tp.y=y;
							vp.push_back(tp);
							sp.push_back(tp);
						}
						inCircle(x+g,y,rr,vp);
						if(inCircle(x+g,y+g,rr)+inCircle(x+g,y,rr)==1){
							double tmp=sqrt(sqr(rr)-sqr(x+g));
							if(!(tmp>=y-LIMIT && tmp<=y+g+LIMIT))
								tmp=-tmp;
							tp.x=x+g;
							tp.y=tmp;
							vp.push_back(tp);
							sp.push_back(tp);
						}
						inCircle(x+g,y+g,rr,vp);
						if(inCircle(x+g,y+g,rr)+inCircle(x,y+g,rr)==1){
							double tmp=sqrt(sqr(rr)-sqr(y+g));
							if(!(tmp>=x-LIMIT && tmp<=x+g+LIMIT))
								tmp=-tmp;
							tp.x=tmp;
							tp.y=y+g;
							vp.push_back(tp);
							sp.push_back(tp);
						}
						inCircle(x,y+g,rr,vp);
						if(inCircle(x,y,rr)+inCircle(x,y+g,rr)==1){
							double tmp=sqrt(sqr(rr)-sqr(x));
							if(!(tmp>=y-LIMIT && tmp<=y+g+LIMIT))
								tmp=-tmp;
							tp.x=x;
							tp.y=tmp;
							vp.push_back(tp);
							sp.push_back(tp);
						}
						for(int k=1;k<vp.size()-1;k++){
							escArea+=tri(vp[0],vp[k],vp[k+1]);
						}
						tp.x=0;
						tp.y=0;
						escArea+=rr*rr*ang(sp[0],sp[1])/2-tri(sp[0],sp[1],tp);
					}
				}
			}
			p=1-escArea/PI/R/R;
		}
		printf("Case #%d: %.6lf\n",nn,p);
	}
}
