#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <math.h>

using namespace std;

struct point{
	double x,y;
};

double w;
int g,n,m;
point low[201];
point upp[201]; 

double find(double dst){
	vector <point> up;
	vector <point> down;
	//up.push_back(upp[0]);
	//down.push_back(low[0]);

	for (int i=1; i<m; i++){
		if (upp[i].x+1e-9>dst&&upp[i-1].x-1e-9<dst){
			double cur1=upp[i-1].y;
			double cur2=upp[i].y;
			double ds=dst-upp[i-1].x;
			double d=upp[i].x-upp[i-1].x;
			double newsd=cur2-cur1;

			double y=(ds*newsd)/d+cur1;
			point nww; nww.x=dst, nww.y=y;
			up.push_back(upp[i-1]);
			up.push_back(nww);
			break;
		} else
			up.push_back(upp[i-1]);
	}

	for (int i=1; i<n; i++){
		if (low[i].x+1e-9>dst&&low[i-1].x-1e-9<dst){
			double cur1=low[i-1].y;
			double cur2=low[i].y;
			double ds=dst-low[i-1].x;
			double d=low[i].x-low[i-1].x;
			double newsd=cur2-cur1;

			double y=(ds*newsd)/d+cur1;
			point nww; nww.x=dst, nww.y=y;
			down.push_back(low[i-1]);
			down.push_back(nww);
			break;
		} else
			down.push_back(low[i-1]);
	}

	vector <point> nw=up;
	reverse(down.begin(),down.end());
	for (int i=0; i<down.size(); i++)
		nw.push_back(down[i]);

	double area=0;
	for (int i=0; i<nw.size(); i++){
		area+=(nw[i].x*nw[(i+1)%((int)(nw.size()))].y-nw[i].y*nw[(i+1)%(int(nw.size()))].x);
	}
	area/=2.0;
	return fabs(area);
}

void solve(int tst){
	printf("Case #%d:\n",tst);
	scanf("%lf%d%d%d",&w,&n,&m,&g);

	for (int i=0; i<n; i++){
		scanf("%lf%lf",&low[i].x,&low[i].y);
	}
	for (int i=0; i<m; i++){
		scanf("%lf%lf",&upp[i].x,&upp[i].y);
	}

	double arr=find(w);

	double plos=arr/(double)g;

	for (int i=1; i<g; i++){
		double cur=i*plos;
		double l=0, r=w;
		for (int j=1; j<=100; j++){
			double key=(l+r)/2;
			double pls2=find(key);
			if (pls2>cur) r=key; else
				l=key;
		}
		printf("%.10lf\n",l);
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);

	for (int tt=1; tt<=tests; tt++){
		solve(tt);
		cerr<<tt<<endl;
	}

	return 0;
}