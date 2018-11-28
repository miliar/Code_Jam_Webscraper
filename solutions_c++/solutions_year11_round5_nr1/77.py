#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;

double ln, un, g;
double s, w;
struct Tp{
	double x,y;

} u[1111], l[1111];

#define eps 1e-11

inline double GetY(double x1,double y1,double x2,double y2,double x){
	if(fabs(x1 - x2) < eps) return y2;
	double dx = x2 - x1;
	double dy = y2 - y1;
	return ((x - x1)/dx) * dy + y1;
}

double GetS(double x){
	double tot = 0;

	for(int i=0;i<ln-1;i++)
		if(x >= l[i+1].x){
			tot -= (l[i].x - l[i+1].x) * (l[i].y + l[i+1].y);
		}else{
			double y = GetY(l[i].x,l[i].y,l[i+1].x,l[i+1].y,x);
			tot -= (l[i].x - x) * (l[i].y + y);
			break;
		}

	for(int i=0;i<un-1;i++)
		if(x >= u[i+1].x){
			tot += (u[i].x - u[i+1].x) * (u[i].y + u[i+1].y);
		}else{
			double y = GetY(u[i].x,u[i].y,u[i+1].x,u[i+1].y,x);
			tot += (u[i].x - x) * (u[i].y + y);
			break;
		}

	return fabs(tot)/2;
}

double FindAns(double s,double l){
	double left = l, right = w, S = GetS(l);
	while( right - left > eps){
		double center = (left + right) / 2;
		if(GetS(center) - S > s) right = center;else left = center;
	}
	return (left+right)/2;
}

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		cin >> w >> ln >> un >> g;

		s = 0;
		for(int i=0;i<ln;i++){
			cin >> l[i].x >> l[i].y;
			if(i)
				s -= (l[i-1].x - l[i].x) * (l[i - 1].y + l[i].y);
		}
		for(int i=0;i<un;i++){
			cin >> u[i].x >> u[i].y;
			if(i)
				s += (u[i-1].x - u[i].x) * (u[i - 1].y + u[i].y);
		}
		s = fabs(s) / 2;

		cout.precision(15);
		cout << fixed;

		printf("Case #%d:\n",_);		
		double ds = s / g, lBound = 0;
		for(int i=1;i<g;i++){
			double x = FindAns(ds, lBound);
			cout << x << endl;
			lBound = x;
		}		
	}
	return 0;
}
