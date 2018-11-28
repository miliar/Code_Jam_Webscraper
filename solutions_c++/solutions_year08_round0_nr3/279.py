#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <limits>
#include <iomanip>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
#define MP make_pair
#define REP(x,n) for(int x=0; x<(int)(n); ++x)
#define REB(b,x,n) for(int x=b; x<(int)(n); ++x)
#define REPD(x,n) for(int x=(n)-1; x>=0; --x)
#define PB push_back
#define ST first
#define ND second
const int INF = 1000000001;
const double EPS = 10e-9;

typedef long double lod;

//distance between two points
inline lod dist(lod x1,lod y1, lod x2,lod y2) {
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

//area of circular segment given chord length and radius
inline lod segmentArea(lod c, lod r) {
	//central angle
	lod theta = 2*asin(c/r/2);
	return r*r*(theta-sin(theta))/2;
}

//intersect square (x,y,x+w,y+w) with circle((0,0),inr), inr,x,y>0
lod intersectArea(lod x, lod y, lod w, lod inr) {
	lod inr2 = inr*inr;
	//whether the 4 vertexes are in or outside the circle
	bool vmin = dist(x,y,0,0) < inr;
	bool vx = dist(x+w,y,0,0) < inr;
	bool vy = dist(x,y+w,0,0) < inr;
	bool vmax = dist(x+w,y+w,0,0) < inr;

	//if(!vmax) cout<<vmin<<vx<<vy<<vmax<<endl;

	//all outside
	if(!vmin) return 0;
	//all inside
	if(vmax) return w*w;
	//majority outside
	if(!vx && !vy) {
		//count the other coordinate of intersection points
		lod doty = sqrt(inr2-x*x);
		lod dotx = sqrt(inr2-y*y);
		//right triangle + circle segment
		return (dotx-x)*(doty-y)/2 + segmentArea(dist(dotx,y,x,doty),inr);
	}
	//bottom half outside
	if(vx && !vy) {
		lod dot1y = sqrt(inr2-x*x);
		lod dot2y = sqrt(inr2-(x+w)*(x+w));
		//trapezoid + circle segment
		return (dot1y-y + dot2y-y)*w/2 + segmentArea(dist(x,dot1y, x+w,dot2y),inr);
	}
	//right half outside
	if(!vx && vy) {
		lod dot1x = sqrt(inr2-y*y);
		lod dot2x = sqrt(inr2-(y+w)*(y+w));
		//trapezoid + circle segment
		return (dot1x-x + dot2x-x)*w/2 + segmentArea(dist(dot1x,y, dot2x,y+w),inr);
	}
	//majority inside
	else {
		lod dotx = sqrt(inr2-(y+w)*(y+w));
		lod doty = sqrt(inr2-(x+w)*(x+w));
		//all the square except for a triangle except for the circle segment
		return w*w - (x+w-dotx)*(y+w-doty)/2 + segmentArea(dist(x+w,doty, dotx,y+w),inr);
	}
}

//count area of previously "thickened" raquet
lod doit(lod outr, lod inr, lod gap, lod ginit, lod gstep) {
	if(gap<0) gap=0; //return 1;
	if(inr<0) inr=0; //return 1;

	//cout<<outr<<" "<<inr<<" "<<gap<<" "<<ginit<<" "<<gstep<<endl;

	lod gapArea = 0;
	//count all gaps in positive quarter
	for(lod x=ginit; x<inr; x+=gstep)
	for(lod y=ginit; y<inr; y+=gstep) {
		gapArea += intersectArea(x,y,gap,inr);
		//cout<<"added "<<intersectArea(x,y,gap,inr)<<endl;
	}

	return 1 - gapArea/M_PI_4/outr/outr;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int N;
	cin>>N;
	cout<<fixed<<setprecision(7);
	REP(ncase,N) {
		lod f,R,t,r,g;
		cin>>f>>R>>t>>r>>g;
		lod result = doit(R, R-f-t, g-f-f, r+f, g+r+r);
		cout<<"Case #"<<ncase+1<<": "<< result <<endl;
	}

	return 0;
}
