#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<ext/hash_map>
#include<ext/hash_set>
#include<queue>
#include<functional>
#include<cmath>
#include<cstdlib>
#define EPS 1e-9

struct Point{
	double x,y;
	Point(){x=y=0;}
	Point(double x,double y):x(x),y(y){}
	inline Point operator-(const Point &p)const{ return Point(x-p.x,y-p.y); }
	inline Point operator+(const Point &p)const{ return Point(x+p.x,y+p.y); }
	inline double operator^(const Point &p)const{ return x*p.y-y*p.x;}
	inline Point operator*(double u)const{ return Point(x*u,y*u); }
	inline double len()const{ return sqrt(x*x+y*y); }
	Point operator/(double r) {
		return Point(x/r, y/r);
	}
	Point rot(double t) { return Point(x*cos(t) - y*sin(t), x*sin(t) + y*cos(t)); }
	void read(){ scanf("%lf%lf",&x,&y); }
	void out(){ printf("(%.2lf %.2lf)\n",x,y); }
};

bool checkintersect(Point &a,Point &b, Point &c,Point &d){
	double w=(b-a)^(d-c);
	if (fabs(w)<EPS) return false;
	double u=((c-a)^(d-c))/w;
	double v=((a-c)^(b-a))/-w;
	return u>EPS && u<1-EPS && v>-EPS && v<1+EPS;
}

Point intersect(Point &a,Point &b,Point &c,Point &d){
	double w=(b-a)^(d-c);
	double u=((c-a)^(d-c))/w;
	return a+(b-a)*u;
}

using namespace std;
using namespace __gnu_cxx;

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		int N;
		scanf("%d", &N);
		Point P[N];
		int R[N];
		for (int i = 0 ; i < N; ++i){
			P[i].read();
			scanf("%d", &R[i]);
		}
		if (N == 1){ printf("%.10f\n", 1.*R[0]); continue;}
		double ans = 1e30;
		if (N == 2){
			ans = max(1.*R[0], 1.*R[1]);
			double tr = 0;
			tr = ((P[0] - P[1]).len() + R[0] + R[1])/2.;
			ans = min(ans, tr);
			printf("%.10f\n", ans);
			continue;
		}

		for (int i = 0 ; i < N; ++i)
			for (int j = i+1 ; j < N; ++j){
				double tr = 0;
				tr = ((P[i]-P[j]).len() + R[i] + R[j])/2.;
				Point G = (P[i]+P[j])/2.;
				Point rem = P[3-i-j];
				int k = 3-i-j;
				tr = max(tr, 1.*R[k]);
				ans = min(ans, tr);
			}
		printf("%.10f\n", ans);
	}
	return 0;
}

