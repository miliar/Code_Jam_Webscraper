#include "hpmv.h"

double inter(double a, double b, double c, double d, double r){
	//interpolate c - d on a-r-b
	return c+(d-c)*(r-a)/(b-a);
}
int px1[128],px2[128],py1[128],py2[128];
int w,l,u,g;



double pol(double x){
	int ind1 = lower_bound(px1,px1+l, x-0.1)-px1;
	int ind2 = lower_bound(px2,px2+u, x-0.1)-px2;
	if(ind1>=l-1 || x<=px1[ind1]) ind1--;
	if(ind2>=u-1 || x<=px2[ind2]) ind2--;
	//out(ind1,"/",ind2);ent;
	double yy1 = inter(px1[ind1],px1[ind1+1],py1[ind1],py1[ind1+1],x);
	double yy2 = inter(px2[ind2],px2[ind2+1],py2[ind2],py2[ind2+1],x);
	//out(yy1, ":",yy2);ent;
	double a1 = 0;
	FOR(i,ind1){
		a1+=(px1[i+1]-px1[i])*(py1[i]+py1[i+1])/2.0;
	}
	a1+=(x-px1[ind1])*(yy1+py1[ind1])/2;
	double a2 = 0;
	FOR(i,ind2){
		a2+=(px2[i+1]-px2[i])*(py2[i]+py2[i+1])/2.0;
	}
	a2+=(x-px2[ind2])*(yy2+py2[ind2])/2;
	//out("a1 ",a1,"a2 ",a2);ent;
	return a2-a1;
	
}
hello

memset(px1,0,sizeof(px1));
memset(px2,0,sizeof(px2));
memset(py1,0,sizeof(py1));
memset(py2,0,sizeof(py2));

in(w,l,u,g);
inarr(l,px1,py1);
inarr(u,px2,py2);
ent;
double total = pol(w);
//out(total);ent;
FOR(i,g-1){
	double my = total*(i+1)/g;
	//out(my);ent;
	double lb = 0;
	double ub = w;
	while(ub-lb>0.00000001){
		double mb = (ub+lb)/2;
		double area = pol(mb);
		if(area<my) lb=mb;
		else ub=mb;
	}
	out(lb);ent;
}

cya
