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
	Point(){}
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
		int A[N][N];
		for (int i = 0 ; i < N; ++i){
			char s[N+10];
			scanf("%s", s);
			for (int j = 0 ; j < N; ++j){
				A[i][j] = s[j] - '0';
			}
		}
		int ans = 0;
		for (int i = 0 ; i < N; ++i){
			bool ok = 1;
			for (int j = i+1; j < N; ++j)
				if (A[i][j])
					ok = 0;
			if (ok) continue;
			for (int j = i+1; j < N; ++j){
				ok = 1;
				for (int k = i+1 ; k < N; ++k)
					if (A[j][k]) ok = 0;
				if (!ok) continue;
				for (int k = j; k > i; --k){
					int tmp[N];
					memcpy(tmp, A[k], sizeof(tmp));
					memcpy(A[k], A[k-1], sizeof(tmp));
					memcpy(A[k-1], tmp, sizeof(tmp));
					ans++;
				}
				break;
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
