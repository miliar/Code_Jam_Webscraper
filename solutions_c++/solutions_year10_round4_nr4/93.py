#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

const double pi = acos(-1.0);
struct point{
	double x,y;
};

int n,m;
point pole[5000+10],bkt[1000+10];

double sqdist(const point& p1,const point &p2){
	return (p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y);
}

double getinter(point bkt,point p1,point p2){
	double a,b,c;
	a = sqdist(bkt,p1);
	b = sqdist(bkt,p2);
	c = sqdist(p1,p2);
	double g1 = 2.0 * acos(0.5*(a+c-b)/sqrt(a * c));
	double g2 = 2.0 * acos(0.5*(b+c-a)/sqrt(b*c));
	double area = 0.0;
	/*if(g1>=pi){

	}*/
			
	area += 0.5 * g1 * a  - 0.5 * a * sin(g1);
	area += 0.5 * g2 * b  - 0.5 * b * sin(g2);
	return area;
}

int main(){
	int tt,tc;
	cin>>tc;
	for(tt=1;tt<=tc;tt++){
		printf("Case #%d:",tt);
		cin>>n>>m;
		int i;
		for(i=0;i<n;i++)
			cin>>pole[i].x>>pole[i].y;
		for(i=0;i<m;i++)
			cin>>bkt[i].x>>bkt[i].y;
		for(i=0;i<m;i++)
			printf(" %.7lf",getinter(bkt[i],pole[0],pole[1]));
		printf("%\n");
	}
	return 0;
}
