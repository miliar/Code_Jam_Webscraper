#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXN 215
#define EPS 1e-12

struct Point {
	double x,y;
	Point() {}
	Point(double a, double b):x(a),y(b) {}
};

Point pl[MAXN],pu[MAXN], p[MAXN], pt[MAXN];
int W,L,U,G;

double find_area(double x) {
	int n = 0;
	int i,j;
	double y;
	rep(i,L) {
		if(pl[i].x < x) {
			pt[n++] = pl[i];
		}
		else if(pl[i].x >= x) {
			y = (double) pl[i-1].y + (double)(pl[i-1].y - pl[i].y) * (double)(x - pl[i-1].x) / (double)(pl[i-1].x - pl[i].x);
			pt[n++] = Point(x, y);
			break;
		}
	}

	for(i=U-1;i>=0;i--) {
		if(pu[i].x > x) continue;
		else if(pu[i].x <= x) {
			y = pu[i].y + (pu[i].y - pu[i+1].y) * (x - pu[i].x) / (pu[i].x - pu[i+1].x);
			pt[n++] = Point(x,y);
			for(j=i;j>=0;j--) pt[n++] = pu[j];
			break;
		}
	}
	pt[n] = pt[0];

	double A;
	A = 0;
	rep(i,n) {
		A += (pt[i].x * pt[i+1].y - pt[i].y * pt[i+1].x);
	}
	A /= 2.0;
	A = fabs(A);
	return A;

}

int main() {
	int T,kase=1;
	int i;
	double A,Ag,Acur,prev;
	double lo,hi,mid;
	int n,ct;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d:\n",kase++);
		scanf(" %d %d %d %d",&W,&L,&U,&G);
		rep(i,L) {
			scanf(" %lf %lf",&pl[i].x,&pl[i].y);
		}
		rep(i,U) scanf(" %lf %lf",&pu[i].x,&pu[i].y);

		n = 0;
		rep(i,L) p[n++] = pl[i];
		for(i=U-1;i>=0;i--) p[n++] = pu[i];
		p[n] = p[0];

		A = 0;
		rep(i,n) {
			A += (p[i].x * p[i+1].y - p[i].y * p[i+1].x);
		}
		A /= 2.0;
		A = fabs(A);
		Ag = A / (double)G;

		prev = 0;

		rep(i,G-1) {
			lo = prev;
			hi = W;
			ct=0;
			while(hi-lo>EPS) {
				mid = (lo + hi) / 2;

				Acur = find_area(mid);
				/*if(fabs(Acur - Ag * (double)(i+1) ) < EPS) {
					printf("%.10lf\n",mid);
					prev = mid;
					break;
				}*/
				if(Acur < Ag*(i+1)) lo = mid;
				else hi = mid;
				ct++;
				if(ct > 1000) break;
			}
			printf("%.10lf\n",mid);
			prev = mid;
		}
	}
	return 0;
}