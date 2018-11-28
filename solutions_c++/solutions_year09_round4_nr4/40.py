#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const double eps = 1e-8;
const double pi = acos(-1.0);
inline int dcmp(const double &a,const double &b=0,const double &zero=1E-8){ 
	if(a-b<-zero)return -1;
	return a-b>zero;
}
inline int Sign(double a) {
	return a < -eps ? -1 : a > eps;
}
inline double Arc_Sin(double a) {
	if (Sign(a + 1) <= 0) return -pi / 2;
	if (Sign(a - 1) >= 0) return pi / 2;
	return asin(a);
}
inline double Arc_Cos(double a) {
	if (Sign(a + 1) <= 0) return pi;
	if (Sign(a - 1) >= 0) return 0;
	return acos(a);
}
inline double Sqr(double a) {
	return a * a;
}
inline double Sqrt(double a) {
	return a <= 0 ? 0 : sqrt(a);
}
struct point {
	double x, y;
	point(double v1 = 0, double v2 = 0): x(v1), y(v2){}
	void Input() {
		scanf("%lf %lf", &x, &y);
	}
	void Output() const {
		printf("%lf %lf", x, y);
	}
	double Length() const {
		return Sqrt(Sqr(x) + Sqr(y));
	}
	point Rotate(double a) const {
		return point(x * cos(a) - y * sin(a), x * sin(a) + y * cos(a));
	}
	int Side() const {
		if (Sign(x) < 0 || !Sign(x) && Sign(y) < 0) return 0;
		if (Sign(x) > 0 || !Sign(x) && Sign(y) > 0) return 1;
		return -1;
	}
	point Perp () const {
		return point(-y, x);
	}
	point Unit() const {
		return *this / Length();
	}
	point operator + (const point &b) const{
		return point(x + b.x, y + b.y);
	}
	point operator - (const point &b) const{
		return point(x - b.x, y - b.y);
	}
	point operator * (double b) const{
		return point(x * b, y * b);
	}
	point operator / (double b) const{
		return point(x / b, y / b);
	}
};
bool operator == (const point &a, const point &b) {
	return !Sign(a.x - b.x) && !Sign(a.y - b.y);
}
bool operator < (const point &a, const point &b) {
	return Sign(a.x - b.x) ? Sign(a.x - b.x) < 0 : Sign(a.y - b.y) < 0;
}
double Det(const point &a, const point &b) {
	return a.x * b.y - a.y * b.x;
}
double Dot(const point &a, const point &b) {
	return a.x * b.x + a.y * b.y;
}
double Dist(const point &a, const point &b, const point &c) {
	return abs(Det(a - c, b - c) / (a - b).Length());
}
double Angle(const point &a, const point &b) {
	return Arc_Cos(Dot(a, b) / a.Length() / b.Length());
}
double Dis(const point &a,const point&b) {
	return (a - b).Length();
}
bool Line_Intersect(const point &a, const point &b, const point &c, const point &d, point &e) {
	double s1 = Det(c - a, d - a);
	double s2 = Det(d - b, c - b);
	if (!Sign(s1 + s2)) return 0;
	e = (b - a) * (s1 / (s1 + s2)) + a;
	return 1;
}
int Side(const point &a, const point &b, const point &c) {
	return Sign(Det(c - a, b - a));
}
bool In_The_Seg(const point &a, const point &b, const point &c) {
	if (Sign(Dist(a, b, c))) return 0;// Not needed when you make sure it does technically.
	return Sign(Dot(a - c, b - c)) <= 0;
}
bool Seg_Intersect(const point &a, const point &b, const point &c, const point &d, point &e) {
	double s1 = Det(c - a, d - a);
	double s2 = Det(d - b, c - b);
	if (!Sign(s1 + s2)) return 0;
	e = (b - a) * (s1 / (s1 + s2)) + a;
	return In_The_Seg(a, b, e) && In_The_Seg(c, d, e);
}
struct Circle {
	point o;
	double r;//  Squared
	bool Inside(point a) {
		return Sqr(a.x - o.x) + Sqr(a.y - o.y) <= r;
	}
	void Calc(point a, point b) {
		o.x = (a.x + b.x) / 2;
		o.y = (a.y + b.y) / 2;
		r = Sqr(a.x - o.x) + Sqr(a.y - o.y);
	}
	void Calc(point a, point b, point c) {// Not certain if a, b and c lie in the same line, which needs prejudging.
		double a1 = 2 * (a.x - b.x);
		double b1 = 2 * (a.y - b.y);
		double c1 = Sqr(a.x) - Sqr(b.x) + Sqr(a.y) - Sqr(b.y);
		double a2 = 2 * (a.x - c.x);
		double b2 = 2 * (a.y - c.y);
		double c2 = Sqr(a.x) - Sqr(c.x) + Sqr(a.y) - Sqr(c.y);
		o.x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1);
		o.y = (c1 * a2 - c2 * a1) / (a2 * b1 - a1 * b2);
		r = Sqr(a.x - o.x) + Sqr(a.y - o.y);
	}
	bool Intersect_With_Line(point fr, point to, point &A, point &B) const {
		if (Sign(Det(o - fr, to - fr)) > 0) swap(fr, to);
		double R = Sqrt(r);
		double h = Dist(fr, to, o);
		if (Sign(h - R) > 0) return 0;
		point mm = (to - fr).Unit().Rotate(-pi / 2) * h + o;
		double l = Sqrt(Sqr(R) - Sqr(h));
		point vv = (to - fr).Unit() * l;
		A = mm - vv;
		B = mm + vv;
		return 1;
	}
	bool Contain(const Circle &a) const {
		return Sign(Sqrt(a.r) + (o - a.o).Length() - Sqrt(r)) < 0;
	}
	bool Disjunct(const Circle &a) const {
		return Sign(Sqrt(a.r) + Sqrt(r) - (o - a.o).Length()) < 0;
	}
};
bool Intersect(Circle a, Circle b, point &A, point &B) {
	if (a.Contain(b) || b.Contain(a) || a.Disjunct(b)) return 0;
	double s1 = (a.o - b.o).Length();
	double s2 = (a.r - b.r) / s1;
	double aa = (s1 + s2) / 2;
	double bb = (s1 - s2) / 2;
	point mm = (b.o - a.o) * (aa / (aa + bb)) + a.o;
	double h = Sqrt(a.r - Sqr(aa));
	point vv = (b.o - a.o).Unit().Rotate(pi / 2) * h;
	A = mm + vv;
	B = mm - vv;
	return 1;
}

#include<iostream>
using namespace std;

Circle a[50]; 
Circle b[50];

point c[5000];


int n;
inline bool check(const point&p1,const int i){
	if((p1-b[i].o).Length()>Sqrt(b[i].r)+eps)
		return 0;
	return 1;
}

long long d[5000];

bool check(double r){
	for(int i=0;i<n;i++){
		c[i]=b[i].o=a[i].o;
		b[i].r=Sqr(a[i].r-r);
	}
	int m=n;
	for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++)
			if(Intersect(b[i],b[j],c[m],c[m+1]))m+=2;
	for(int i=0;i<m;i++) d[i]=0;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
			if(check(c[i],j)){
				d[i]+=(long long)1<<j;
			}
	long long all=1;
	for(int i=0;i<n;i++)
		all*=2;
	all--;
	for(int i=0;i<m;i++)
		for(int j=i;j<m;j++)
			if((d[i]|d[j])==all)return 1;
	return 0;
}

main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	cout.flags(ios::fixed);
	cout.precision(6);
	for(int kase=1;kase<=t;kase++){
		cout<<"Case #"<<kase<<": ";
		cin>>n;
		for(int i=0;i<n;i++){
			a[i].o.Input();
			double t;
			scanf("%lf",&t);
			a[i].r=t;
		}
		double l=0,r=1e7;
		for(int i=0;i<n;i++)
			l>?=a[i].r;
		while(r-l>1e-7)
			if(check((l+r)/2))r=(l+r)/2;
			else l=(l+r)/2;
		cout<<l<<endl;
	}
}
