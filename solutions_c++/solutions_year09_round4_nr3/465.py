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

int N, P[20][30];
int bin[20][30], bc[20], cnt, ans;
bool G[30][30];

void go(int lv){
	if (lv == N){
		ans = min(ans, cnt);
		return ;
	}
	if (cnt >= ans) return;
	for (int i = 0 ; i < cnt; ++i){
		//for each bin
		bool ok = 1;
		for (int j = 0 ; j < bc[i] && ok; ++j)
			ok = G[lv][bin[i][j]];
		if (ok){
			bin[i][bc[i]++] = lv;
			go(lv+1);
			bc[i]--;
		}
	} 
	//or try a new bin
	bc[cnt] = 0;
	bin[cnt][bc[cnt]] = lv;
	bc[cnt] = 1;
	cnt++;
	go(lv+1);
	cnt--;
	bc[cnt]=0;
}

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		printf("Case #%d: ", ++ca);
		int K;
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; ++i)
			for (int j = 0 ; j < K; ++j)
				scanf("%d", &P[i][j]);
		memset(G, 0, sizeof(G));
		for (int i = 0 ; i < N; ++i)
			for (int j = i+1 ; j < N; ++j){
				bool ok = 1;
				for (int k = 0 ; ok && k < K-1; ++k){
					if (P[i][k] > P[j][k] && P[i][k+1] < P[j][k+1]) ok = 0;
					if (P[i][k] < P[j][k] && P[i][k+1] > P[j][k+1]) ok = 0;
					//Point a(k, P[i][k]), b(k+1, P[i][k+1]);
					//Point c(k, P[j][k]), d(k+1, P[j][k+1]);
					//ok &= !checkintersect(a, b, c, d);
				}
				for (int k = 0 ; ok && k < K; ++k)
					ok = (P[i][k] != P[j][k]);
				//printf("%d %d-> %d\n", i, j, ok);
				G[i][j] = G[j][i] = ok;
			}
		ans = N;	
		memset(bc, 0, sizeof(bc));
		cnt = 0;
		go(0);
		printf("%d\n", ans);
	}
	return 0;
}

