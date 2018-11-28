#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#define feq(x,y) (fabs((x)-(y))<eps)
#define flt(x,y) ((x)<(y)-eps)
#define fgt(x,y) ((x)>(y)+eps)
#define fle(x,y) ((x)<(y)+eps)
#define fge(x,y) ((x)>(y)-eps)
using namespace std;
const double inf = 1e40, eps = 1e-9;

struct Point{
	double x, y;
	Point(){}
	Point(double x, double y):x(x),y(y){}
	bool operator<(const Point &p)const{ return x<p.x || (x==p.x && y<p.y); }
	double operator^(const Point &p)const{ return x*p.y - y*p.x; };
	double operator*(const Point &p)const{ return x*p.x + y*p.y; };
	Point operator+(const Point &p)const{ return Point(x+p.x, y+p.y); };
	Point operator-(const Point &p)const{ return Point(x-p.x, y-p.y); };
	Point operator*(double u)const{ return Point(x*u, y*u); };
	double len(){ return sqrt(x*x+y*y); }
};

struct Cycle{
	Point p;
	double r;
	Cycle(){}
	Cycle(Point p, double r):p(p),r(r){}
};

int main(){
	int T, ca = 0;
	scanf("%d", &T);
	while (T--){
		int n;
		vector<Cycle> v; v.clear();
		scanf("%d", &n);
		for (int i=0; i<n; i++){
			int x, y, r;
			scanf("%d%d%d", &x, &y, &r);
			v.push_back( Cycle(Point(x,y), r));
		}

		double ans = inf;
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++){
				double f = ((v[i].p-v[j].p).len() + v[i].r + v[j].r)/2;
				if (f < ans) ans = f;
			}

		if (n==1) ans = min(ans, v[0].r);
		else if (n==2) {
			ans = min(ans, max(v[0].r, v[1].r));
		}

		printf("Case #%d: %.6lf\n", ++ca, ans);
	}
}
