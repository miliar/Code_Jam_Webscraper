#include <iostream>
#include <cstdio>
#include <cmath>
#include <complex>
using namespace std;

#define X real()
#define Y imag()

typedef complex<double> point;

int W;
int L,U;
const double eps = 1e-8;
const int maxn = 100 + 10;
point lower[maxn],upper[maxn];
point all[maxn + maxn];
int s = 0;
int G;
double tot;

double getArea() {
	double ans = 0.0;
	for(int i = 0;i<s - 1;i++)
		ans += all[i].X * all[i + 1].Y - all[i + 1].X * all[i].Y;
	ans += all[s - 1].X * all[0].Y - all[s - 1].Y * all[0].X;
	return fabs(ans);
}

bool getInter(point p1,point p2,double x,point& ret) {
	if(fabs(p1.X - x)<eps){
		ret = p1;
		return true;
	}
	if(fabs(p2.X - x)<eps) {
		ret = p2;
		return true;
	}
	if(x - p1.X < -eps || x - p2.X > eps)return false;
	double K = (x - p1.X) / (p2.X - p1.X);
	ret = p1 + K * (p2 - p1);
	return true;
}

void getInter(double x,point& up,point& down) {
	for(int i = 0;i<U - 1;i++)
		if(getInter(upper[i],upper[i + 1],x,up))break;
	for(int i = 0;i<L - 1;i++)
		if(getInter(lower[i],lower[i + 1],x,down))break;
}


void work() {
	double lh;
	tot = getArea();
	lh = 0.0;
	tot /= G;
	for(int i = 0;i<G - 1;i++) {
		double tl = lh,tr = W,mid,area;
		point u1,d1,u2,d2;
		getInter(lh,u1,d1);
		while(tr - tl > eps) {
			mid = (tl + tr) * 0.5;
			getInter(mid,u2,d2);
			s = 0;
			all[s++] = u1;
			for(int i = 0 ;i<U;i++)
				if(upper[i].X > lh && upper[i].X < mid)
					all[s++] = upper[i];
			all[s++] = u2;
			all[s++] = d2;
			for(int i = L - 1;i>=0;i--)
				if(lower[i].X > lh && lower[i].X < mid)
					all[s++] = lower[i];
			all[s++] = d1;
			area = getArea();
			if(area>tot)tr = mid;
			else tl = mid;
		}
		printf("%lf\n",tl);
		lh = tl;
	}
}

int main() {
	int T;
	scanf("%d",&T);
	for(int tc = 1;tc<=T;tc++) {
		printf("Case #%d:\n",tc);
		scanf("%d%d%d%d",&W,&L,&U,&G);
		double x,y;
		for(int i = 0;i<L;i++) {
			scanf("%lf%lf",&x,&y);
			lower[i] = point(x,y);
		}
		for(int i = 0;i<U;i++) {
			scanf("%lf%lf",&x,&y);
			upper[i] = point(x,y);
		}
		s = 0;
		for(int i =0 ;i<U;i++)
			all[s++] = upper[i];
		for(int i = L - 1;i>=0;i--)
			all[s++] = lower[i];
		work();
	}
}
