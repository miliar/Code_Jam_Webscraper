#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int _mx[100], _my[100];
int dx[100], dy[100];
#define SQR(x) ((x)*(x))
const double eps = 1e-10;
const double pi = acos(-1.0);
int sgn(double x) { return (x > eps) - (x < -eps); }

double dabs(double x) {return x+eps;}

struct P { 
	double x, y;
	P(const double &_x = 0,const double &_y=0):x(_x), y(_y){}
	bool operator == (const P & a) const{
		return sgn(a.x-x) == 0 && sgn(a.y - y) == 0;
	}
	P operator+(const P & b) const{return P(x + b.x, y+b.y);}
	P operator-(const P & b) const{return P(x - b.x, y-b.y);}
	P operator*(const double & t) const{return P(x*t, y*t); }

	P turn_right() const { return P(-y, x); }
	P turn_left() const { return P(y, -x); }
	P zoom(double r) const {
		double t = r/sqrt(SQR(x) + SQR(y));
		return P(x*t, y*t);
	}
};

//两点间距离
double dist(const P & a, const P & b) { return sqrt(SQR(a.x-b.x) + SQR(a.y-b.y)); }
double dist2(const P & a, const P & b) { return SQR(a.x-b.x) + SQR(a.y-b.y);}
//叉积
double cross(double x1, double y1, double x2, double y2) {return x1*y2-x2*y1;}
double cross(const P&a, const P&b, const P&c){return cross(b.x-a.x,b.y-a.y,c.x-a.x,c.y-a.y);}
//点积
double dmul(double x1, double y1, double x2, double y2) {return x1*x2+y1*y2;}
double dmul(const P&a, const P&b, const P&c){return dmul(b.x-a.x,b.y-a.y,c.x-a.x,c.y-a.y);}

bool between(const P&a, const P&b, const P& c) { 
	return sgn(dmul(a, b, c)) <= 0;
}

//判断线段与直线的相交情况：
// 输入： 直线上两点la lb, 线段端点sa sb
// 输出 2 : 线段端点落在直线上
//      1 : 规范相交
//      0 : 不相交
int segment_line_intersection(const P &la, const P &lb, const P& sa, const P& sb) {
	int d1, d2;
	d1 = sgn(cross(la, lb, sa));
	d2 = sgn(cross(la, lb, sb));
	if ((d1^d2) == -2) return 1;
	if (d1*d2==0) return 2;
	return 0;
}

//计算两直线交点
// 输入: 直线ab和直线cd
// 0 : 两直线不相交
// 1 : 相交
// 2 : 两直线重合
int line_intersection(const P& a, const P& b, const P& c, const P& d, P& p) {
	double s1 = cross(a, b, c);
	double s2 = cross(a, b, d);
	if (sgn(s1) == 0 && sgn(s2) == 0) return 2;
	else if (sgn(s1 - s2) == 0) return 0;
	else {
		p.x = (c.x*s2-d.x*s1) / (s2 - s1);
		p.y = (c.y*s2-d.y*s1) / (s2 - s1);
		return 1;
	}
}

//判断两条线段是否相交并计算交点
//返回值：
// 0 - 不相交
// 1 - 规范相交
// 2 - 非规范相交 (端点处)
int segment_intersection(const P& a, const P& b, const P& c, const P& d, P &p){
	double s1, s2, s3, s4;
	int d1, d2, d3, d4;
	d1 = sgn(s1=cross(a,b,c));
	d2 = sgn(s2=cross(a,b,d));
	d3 = sgn(s3=cross(c,d,a));
	d4 = sgn(s4=cross(c,d,b));
	if ((d1^d2)==-2 && (d3^d4)==-2) //规范相交计算交点
	{
		p.x = (c.x*s2-d.x*s1)/(s2-s1);
		p.y = (c.y*s2-d.y*s1)/(s2-s1);
		return 1;
	}
	//检测非规范相交
	if((d1==0 && between(c, a, b)) ||
		(d2==0 && between(d, a, b)) ||
		(d3==0 && between(a, c, d)) ||
		(d4==0 && between(b, c, d)))
		return 2;
	return 0;
}

//点线距离，点p，直线ab
double point_line_dist(const P& a, const P& b, const P& p){
	return abs(cross(p, a, b)) / dist(a, b);
}


struct C { //圆
	P m;
	double r;
	C(const P &_m=P(0,0),const double &_r=0):m(_m), r(_r){}

	bool operator == (const C &c) const{return m==c.m && sgn(r-c.r)==0;}
	//是否覆盖点p
	bool cover(const P & p) const{return sgn(dist(p, m) - r) < 0;}
	//是否在圆c内
	bool in(const C& c) const{return sgn(dist(c.m, m) - c.r + r) < 0;}

	//计算圆上两点与圆心所成夹角
	double calc_angle(const P&a, const P&b) const{
		double k = dmul(m, a, b) / SQR(r);
		k=min(k, 1.0); k=max(k, -1.0);
		return acos(k);
	}
};
//圆与直线相交判定
bool circle_line_intersec(const C & c, const P &a, const P &b) {
	return sgn(SQR(cross(c.m,a,b)) - c.r*c.r*dist2(a,b))<=0; //取等=时相切
}
//圆与线段相交判定
bool circle_seg_intersec(const C & c, const P &a, const P &b) {
	if (c.cover(a) || c.cover(b)) return true;
	return (sgn(dmul(a,b,c.m))>0 && sgn(dmul(b,a,c.m))>0)
		&& (sgn(SQR(cross(c.m,a,b)) - c.r*c.r*dist2(a,b))<=0); //取等=时相切
}

//求 扇形-对应三角形剩余部分的面积
double calc_area(const C& c, const P& a, const P&b){
	return (SQR(c.r) * c.calc_angle(a, b) - cross(c.m, a, b))*0.5;
}

//求两圆交点
bool circle_intersection(const C & a, const C & b, P& c1, P& c2) {
	double dd = dist(a.m, b.m);
	if (sgn(dd - (a.r + b.r)) >= 0) {
		return false;
	}
	double l = (dd + (SQR(a.r) - SQR(b.r)) / dd) / 2;
	double h = sqrt(SQR(a.r) - SQR(l));
	c1 = a.m + (b.m - a.m).zoom(l) + (b.m - a.m).turn_left().zoom(h);
	c2 = a.m + (b.m - a.m).zoom(l) + (b.m - a.m).turn_right().zoom(h);
	return true;
}

//calc_area 用以计算N个圆的面积并
struct OpCmp {
	P m;
	OpCmp(const P&_m):m(_m){}
	bool operator()(const P& a, const P& b){
		return atan2(a.y - m.y, a.x - m.x) < atan2(b.y -m.y, b.x - m.x);
	}
};

int const mx[] = {0, 0, 1, -1};
int const my[] = {-1, 1, 0, 0};

double calc_area(const vector<C> & data) {
	vector < C > c;
	for (int i = 0; i < data.size(); ++i) {
		if (sgn(data[i].r) == 0) continue;
		int cFlag = false;
		for (int j = i+1; j <data.size(); ++j)
			if (data[i] == data[j]) {
				cFlag = true;
				break;
			}
			if (cFlag) continue;
			for (int j = 0; j < data.size(); ++j)
				if (i != j && data[i].in(data[j])) {
					cFlag = true;
					break;
				}
				if (!cFlag) {
					c.push_back(data[i]);
				}
	}

	vector< vector<P> > points(c.size());
	for (int i = 0; i < c.size(); ++i)
		for (int k = 0; k < 4; ++k)
			points[i].push_back(P(mx[k], my[k]).zoom(c[i].r)+c[i].m);

	for (int i = 0; i < c.size(); ++i)
		for (int j = i+1; j < c.size(); ++j) {
			P a, b;
			if (circle_intersection(c[i], c[j], a, b)) {
				points[i].push_back(a);
				points[i].push_back(b);
				points[j].push_back(a);
				points[j].push_back(b);
			}
		}

		double res = 0;
		for (int i = 0; i < c.size(); ++i) {
			sort(points[i].begin(), points[i].end(), OpCmp(c[i].m));
			points[i].erase(
				unique(points[i].begin(),points[i].end()), points[i].end());

			for (int j = 0; j < points[i].size(); ++j){
				P a = points[i][j];
				P b = points[i][(j+1)%points[i].size()];
				P m = (a+b-c[i].m-c[i].m).zoom(c[i].r) + c[i].m;
				bool flag = true;
				for (int k = 0; k < c.size(); ++k)
					if (k!=i && c[k].cover(m)){
						flag = false;
						break;
					}
					if (flag) {
						res += cross(P(0,0), a, b) / 2;
						res += calc_area(c[i], a, b);
					}
			}
		}
		return res;
}

vector<C> cir;

void solve() {
	int n, m;
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%d%d", _mx+i, _my+i);
	for (int i = 0; i < m; ++i)
		scanf("%d%d", dx+i, dy+i);
	C A, B;
	A.m.x = _mx[0]; A.m.y = _my[0];
	B.m.x = _mx[1]; B.m.y = _my[1];
	for (int i = 0; i < m; ++i) {
		A.r = dist(P(dx[i],dy[i]), A.m);
		B.r = dist(P(dx[i],dy[i]), B.m);
		cir.clear();
		cir.push_back(A);
		cir.push_back(B);
		double ans = pi* (SQR(A.r) + SQR(B.r)) - calc_area(cir);
		printf(" %.8f", ans);
	}
}

int main() {
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d:", ++tc);
		solve();
		putchar('\n');
	}
	return 0;
}
