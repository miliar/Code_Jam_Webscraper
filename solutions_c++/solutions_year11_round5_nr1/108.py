#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <queue>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <set>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


int num[20005],tmp[20005],keyi[20005];

int W,L,U,G;

struct Point{
	double x,y;
	Point(double _x=0,double _y=0):x(_x),y(_y){};
}lp[1005],up[1005];

double eps=1e-8;
inline int sgn(double a){
	return a>eps ? 1 :( a<-eps ? -1 :0 );
}

Point getP(Point a,Point b,double x){
	if( sgn(a.x-b.x) == 0 ) return Point(x,a.y);
	double r=(b.x-x)/(b.x-a.x);
	double y=b.y+(a.y-b.y)*r;
	return Point(x,y);
}
double ans[1005];




int main(){
	freopen("A-large(2).in","r",stdin);
	freopen("A-large(2).out","w",stdout);

	int cas,Te=1;
	cin>>cas;
	while( cas-- ){
		cin>>W>>L>>U>>G;
		for(int i=1;i<=L;i++) cin>>lp[i].x>>lp[i].y;
		for(int i=1;i<=U;i++) cin>>up[i].x>>up[i].y;
		double area=0,curX=0;
		for(int i=2,j=2;i<=L || j<=U;){
			double nxtX=min(lp[i].x,up[j].x);
			Point leftU=getP(up[j-1],up[j],curX);
			Point leftL=getP(lp[i-1],lp[i],curX);
			Point rightU=getP(up[j-1],up[j],nxtX);
			Point rightL=getP(lp[i-1],lp[i],nxtX);
			area+=(leftU.y-leftL.y + rightU.y-rightL.y)*(nxtX-curX)/2;
			curX=nxtX;
			if( sgn(lp[i].x-curX) ==0 ) i++;
			if( sgn(up[j].x-curX) ==0 ) j++;
		}
		double ave=area/G;
		curX=0,area=0;
		int ind=1;
		for(int i=2,j=2;i<=L || j<=U;){
			double nxtX=min(lp[i].x,up[j].x);
			Point leftU=getP(up[j-1],up[j],curX);
			Point leftL=getP(lp[i-1],lp[i],curX);
			Point rightU=getP(up[j-1],up[j],nxtX);
			Point rightL=getP(lp[i-1],lp[i],nxtX);
			int ss=sgn(area+(leftU.y-leftL.y + rightU.y-rightL.y)*(nxtX-curX)/2 - ave);
			if(  ss==0 ){
				area=0;
				ans[ind++]=nxtX;
				curX=nxtX;
				if( sgn(lp[i].x-curX) ==0 ) i++;
				if( sgn(up[j].x-curX) ==0 ) j++;
			}else if( ss<0 ){
				area+=(leftU.y-leftL.y + rightU.y-rightL.y)*(nxtX-curX)/2;
				curX=nxtX;
				if( sgn(lp[i].x-curX) ==0 ) i++;
				if( sgn(up[j].x-curX) ==0 ) j++;
			}else{
				double left=curX,right=nxtX;
				while( right-left > eps ){
					double mid=(left+right)/2;
					Point leftU=getP(up[j-1],up[j],curX);
					Point leftL=getP(lp[i-1],lp[i],curX);
					Point rightU=getP(up[j-1],up[j],mid);
					Point rightL=getP(lp[i-1],lp[i],mid);
					if( area+(leftU.y-leftL.y + rightU.y-rightL.y)*(mid-curX)/2 > ave ) 
						right=mid;
					else left=mid;
				}
				nxtX=left;
				area=0;
				ans[ind++]=nxtX;
				curX=nxtX;
				if( sgn(lp[i].x-curX) ==0 ) i++;
				if( sgn(up[j].x-curX) ==0 ) j++;
			}
		}

		printf("Case #%d:\n",Te++);
		for(int i=1;i<G;i++) printf("%.8lf\n",ans[i]);
	}
}