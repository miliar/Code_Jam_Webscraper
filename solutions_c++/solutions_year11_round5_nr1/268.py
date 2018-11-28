#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <vector>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std;

const double eps=1e-8;

struct CPoint {
	double x,y;
};

CPoint pl[205],pu[205];
int w,l,u,g,n;

int dcmp(double x) {
	if (x<-eps) return -1;
	else return (x>eps);
}

double cross(CPoint p0, CPoint p1, CPoint p2) {
	return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y);
}

double dot(CPoint p0, CPoint p1, CPoint p2) {
	return (p1.x-p0.x)*(p2.x-p0.x)+(p1.y-p0.y)*(p2.y-p0.y);
}

int PointOnSeg(CPoint p0, CPoint p1, CPoint p2) {
	return dcmp(cross(p0,p1,p2))==0&&dcmp(dot(p0,p1,p2))<=0;
}

int LineIntersection(CPoint p1, CPoint p2, CPoint p3, CPoint p4, CPoint &cp) {
	double u=cross(p1,p2,p3);
	double v=cross(p2,p1,p4);
	if (dcmp(u+v)) {
		cp.x=(p3.x*v+p4.x*u)/(v+u);
		cp.y=(p3.y*v+p4.y*u)/(v+u);
		return 1;
	}
	if (dcmp(u)) return 0;
	if (dcmp(cross(p3,p4,p1))) return 0;
	return -1;
}

int SegIntersection(CPoint p1, CPoint p2, CPoint p3, CPoint p4, CPoint &cp) {
	int ret=LineIntersection(p1,p2,p3,p4,cp);
	if (ret==1) return PointOnSeg(cp,p1,p2)&&PointOnSeg(cp,p3,p4);
	return 0;
}

CPoint pp[205];

double getArea(int nn) {
	double area=0;
	for (int i=1;i<=nn;i++)
		area+=pp[i-1].x*pp[i%nn].y-pp[i%nn].x*pp[i-1].y;
	return fabs(area);
}

void solve() {
	double area;
	n=l+u;
	for (int i=0;i<l;i++) pp[i]=pl[i];
	for (int i=0;i<u;i++) pp[i+l]=pu[u-i-1];
	area=getArea(n);
	area/=g;

//	cout<<"area="<<area<<endl;

	double left,right,mid,subarea;
	int j,k,lastj=0,lastk=0,nn;
	CPoint lastl=pl[0],lastu=pu[0];
	CPoint ppl,ppu,cpl,cpu;
	left=0;right=w;
	for (int i=1;i<g;i++) {
		for (int t=0;t<100;t++) {
			mid=(left+right)/2;
			ppl.x=mid;ppl.y=-1000;
			ppu.x=mid;ppu.y=1000;
			for (j=lastj;j<l-1;j++)
				if (SegIntersection(pl[j],pl[j+1],ppl,ppu,cpl))
					break;
			for (k=lastk;k<u-1;k++)
				if (SegIntersection(pu[k],pu[k+1],ppl,ppu,cpu))
					break;

//			cout<<left<<" "<<right<<" "<<mid<<endl;
//			cout<<lastj<<" "<<lastk<<"   "<<j<<" "<<k<<endl;

			pp[0]=lastl;
			nn=1;
			for (int ii=lastj+1;ii<=j;ii++)
				pp[nn++]=pl[ii];
			pp[nn++]=cpl;
			pp[nn++]=cpu;
			for (int ii=k;ii>lastk;ii--)
				pp[nn++]=pu[ii];
			pp[nn++]=lastu;


			subarea=getArea(nn);
			if (subarea<area) 
				left=mid;
			else
				right=mid;

/*			cout<<nn<<"   ";
			for (int ii=0;ii<nn;ii++) cout<<pp[ii].x<<","<<pp[ii].y<<" ";
			cout<<endl;
			cout<<"area="<<subarea<<" "<<area<<endl;
*/
		}
		printf("%.10lf\n",mid);
		lastl=cpl;
		lastu=cpu;
		lastj=j;
		lastk=k;

		left=mid;
		right=w;
	}
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		cin>>w>>l>>u>>g;
		for (int i=0;i<l;i++)
			scanf("%lf%lf",&pl[i].x,&pl[i].y);
		for (int i=0;i<u;i++)
			scanf("%lf%lf",&pu[i].x,&pu[i].y);
		printf("Case #%d:\n",++kase);
		solve();
	}
	return 0;
}

