#include <string.h>
#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<string>
using namespace std;
const double eps = 1e-8;
const double pi = acos(-1.0);
const double inf = 1e200;
inline int sgn(double x) {
	return x < -eps ? -1 : x > eps;
}
inline double sqr(double x) {
	return x * x;
}
inline double a2r(double a) { //角度到弧度
	return a * pi / 180;
}
inline double r2a(double r) { //弧度到角度
	return r / pi * 180;
}
struct P {
	double x,y;
	P(double x = 0,double y = 0):x(x),y(y) {};
	friend bool operator ==(const P& p1, const P& p2) {
		return sgn(p1.x - p2.x) == 0 && sgn(p1.y - p2.y) == 0;
	}
	friend bool operator <(const P& p1, const P& p2) {
		return sgn(p1.x - p2.x) == 0 ? sgn(p1.y - p2.y) < 0 : p1.x < p2.x;
	}
	friend bool operator >(const P& p1, const P& p2) {
		return sgn(p1.x - p2.x) == 0 ? sgn(p1.y - p2.y) > 0 : p1.x > p2.x;
	}
	friend P operator +(const P& p1, const P& p2) {
		return P(p1.x + p2.x, p1.y + p2.y);
	}
	friend P operator -(const P& p1, const P& p2) {
		return P(p1.x - p2.x, p1.y - p2.y);
	}
	friend P operator *(const P& p, double a) {
		return P(p.x * a,p.y * a);
	}
	friend P operator /(const P& p, double a) {
		return P(p.x / a,p.y / a);
	}
	friend inline double operator ^(const P& p1, const P& p2) { //点乘
		return p1.x * p2.x + p1.y * p2.y;
	}
	friend inline double operator *(const P& p1, const P& p2) { //叉乘
		return p1.x * p2.y - p1.y * p2.x;
	}
	friend inline double dot(const P& o,const P& a,const P& b) {
		return (a - o) ^ (b - o);
	}
	friend inline double cross(const P& o,const P& a,const P& b) { //2倍三角形oab有向面积
		return (a - o) * (b - o);
	}
	friend double dist(const P& p1, const P& p2) {
		return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
	}
	friend double dist2(const P& p1, const P& p2) {
		return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
	}
	double len() const {
		return sqrt(x * x + y * y);
	}
	double len2() const {
		return x * x + y * y;
	}
	//求向量v的极角，角度范围为 [0,2*pi)
	double angle() const {
		double t = atan2(y,x);
		return sgn(t) >= 0 ? t : t + 2 * pi;
	}
	P trunc(double l) const {
		l /= len();
		return P(x * l, y * l);
	}
	P turn_left() const { //法向量
		return P(-y, x);
	}
	P turn_right() const { //法向量
		return P(y, -x);
	}
	P rotate(double th, const P& p) const { //绕点p逆时针转th弧度
		double c = cos(th), s = sin(th);
		return P(c * (x - p.x) - s * (y - p.y) + p.x, s * (x - p.x) + c * (y - p.y) + p.y);
	}
	bool input() {
		return scanf("%lf %lf", &x, &y) == 2;
	}
	void output() const {
		printf("%lf %lf\n", x, y);
	}
};

//以下直线相关
struct line {
	P a, b;
	line() {}
	line(P a, P b):a(a), b(b) {}
	friend double dist(const P& p, const line& l) { //点到直线距离
		return fabs(cross(p, l.a, l.b)) / dist(l.a, l.b);//到线段所在直线距离
	}
	//判定两直线位置关系,并求出交点(如果存在).
	//完全重合(2),有交点(1),平行无交(0),参数错误(-1)
	friend int ins(line l1, line l2, P& p) { //直线与直线相交
		if (l1.a == l1.b || l2.a == l2.b) return -1;
		double c1 = (l1.b - l1.a) * (l2.b - l2.a),//cross(l1.a,l1.b,l2.b);
			c2 = (l2.a - l1.a) * (l2.b - l2.a);//cross(l1.a,l2.a,l2.b);
		if (sgn(c1) == 0) {
			if (sgn(c2) == 0) {
				return 2;//两线重叠
			} else {
				return 0;//两线平行不重叠
			}
		} else {
			p = l1.a + (l1.b - l1.a) * (c2 / c1);
			return 1;
		}
	}
	friend bool sameside(const P& p1, const P& p2, const line& l) { //两个点是否在直线同侧,是则返回true
		return sgn(cross(p1, l.a, l.b) * cross(p2, l.a, l.b)) > 0;
	}
	void input() {
		a.input(), b.input();
	}
};

//以下圆相关
struct C {
	P o;//圆心
	int id;
	double r;
	C():r(0) {}
	C(P o,double r = 0):o(o), r(r) {}
	C(const P& a, const P& b, const P& c) { //三角形abc外接圆
		// 先判(sgn((b - a) * (c - a)) != 0) 不共线
		double c1 = (sqr(a.x) + sqr(a.y) - sqr(b.x) - sqr(b.y)) / 2;
		double c2 = (sqr(a.x) + sqr(a.y) - sqr(c.x) - sqr(c.y)) / 2;
		o.x = (c1 * (a.y - c.y) - c2 * (a.y - b.y)) / ((a - b) * (a - c));
		o.y = (c1 * (a.x - c.x) - c2 * (a.x - b.x)) / ((a - c) * (a - b));
		r = dist2(o, a); 
	}
	friend void tangent(const P& p, const C& c, P& p1, P& p2) { //求圆外点到圆的切点
		double d = dist(p, c.o);
		P t = c.o + (p - c.o) * (c.r / d);
		double th = acos(c.r / d);
		p1 = t.rotate(th, c.o);
		p2 = t.rotate(2 * pi - th, c.o);
	}
	friend int relation(const C& c1, const C& c2) { //两圆关系:
		double d = dist(c1.o, c2.o);
		if (sgn(d - fabs(c1.r - c2.r)) > 0 && sgn(d - c1.r - c2.r) < 0) return 1; //相交
		if (sgn(d - c1.r - c2.r) == 0) return 2;//外切
		if (sgn(d - fabs(c1.r - c2.r)) == 0) return 3;//内切
		if (sgn(d - c1.r - c2.r) > 0) return 4;//相离
		if (sgn(d - fabs(c1.r - c2.r)) < 0) return 5;//内含
		return 0; //error
	}
	friend int ins(const C& c1, const C& c2, P& p1, P& p2) { //圆与圆相交(相切)
		double d = dist(c1.o, c2.o);
		if (sgn(d - (c1.r + c2.r)) > 0 || sgn(d - fabs(c1.r - c2.r)) < 0) { //相离
			return 0;
		}
		if (sgn(d) == 0 && sgn(c1.r - c2.r) == 0) { //重合
			return 3;
		}
		double cosa = (sqr(c1.r) + sqr(d) - sqr(c2.r)) / (2 * c1.r * d);
		double sina = sqrt(max(0., 1. - sqr(cosa)));
		p1 = p2 = c1.o;
		p1.x += c1.r / d * ((c2.o.x - c1.o.x) * cosa + (c2.o.y - c1.o.y) * -sina);
		p1.y += c1.r / d * ((c2.o.x - c1.o.x) * sina + (c2.o.y - c1.o.y) * cosa);
		p2.x += c1.r / d * ((c2.o.x - c1.o.x) * cosa + (c2.o.y - c1.o.y) * sina);
		p2.y += c1.r / d * ((c2.o.x - c1.o.x) * -sina + (c2.o.y - c1.o.y) * cosa);        
		if (sgn(p1.x - p2.x) == 0 && sgn(p1.y - p2.y) == 0) {
			return 1; //相切
		} else {
			return 2; //相交
		}
	}
	friend int ins(const C& c, line l, P& p1, P& p2) { //圆与直线是否相交(相切)
		if (c.o == l.a) swap(l.a, l.b);
		double d = fabs((c.o - l.a) * (l.b - l.a)) / (l.b - l.a).len();
		P v = (l.b - l.a).turn_right(), p;
		line mid(c.o, c.o + v);
		ins(mid, l, p);
		int sign = sgn(d - c.r);
		if (sign < 0) { //相交 2个交点
			double d = dist(c.o, p);
			if (p == l.a) swap(l.a, l.b);
			P v1 = l.a - p;
			p1 = p + v1 * sqrt((sqr(c.r) - sqr(d))) / v1.len();
			p2 = p * 2- p1; //p2 = p1.rotate(pi,p);
			return 2;
		} else if (sign == 0) { //相切
			p1 = p;
			return 1;
		} else {
			return 0; //相离
		}
	}
	friend double intersectionarea(C& C1, C& C2) { //圆C1和C2相交面积
		P &c1 = C1.o, &c2 = C2.o;
		double &r1 = C1.r, &r2 = C2.r;
		if (r1 > r2) swap(c1, c2);
		double d, a1, a2, p, area;
		d = sqrt(sqr(c1.x - c2.x) + sqr(c1.y - c2.y));
		if (sgn(r1 + d - r2) <= 0) return pi * sqr(r1);
		if (sgn(r1 + r2 - d) <= 0) return 0;
		a1 = acos((sqr(r1)+sqr(d)-sqr(r2)) / (2*r1*d));
		a2 = acos((sqr(r2)+sqr(d)-sqr(r1)) / (2*r2*d));
		p = (r1 + r2 + d) / 2;
		area = 2 * sqrt(p * (p-r1) * (p-r2) * (p-d));
		area = a1 * sqr(r1) + a2 * sqr(r2) - area;
		return area;
	}
	friend int incircle(const P& p, const C& c) { //点是否在圆内(边上)
		int sign = sgn(dist(p,c.o) - c.r);
		if (sign < 0) return 1; //相交
		else if (sign == 0) return 2; //相切
		else return 0; //相离
	}/*因为圆为凸集,所以判断点集,折线,多边形是否在圆内时,只需要逐一判断点是否在圆内即可*/

	void input() {
		o.input();
		scanf("%lf", &r);
	}
	void output() {
		o.output();
		printf("%lf\n", r);
	}
	double area() {
		return pi * sqr(r);
	}
	double perimeter() {
		return 2 * pi * r;
	}
};
int n;
C c[1006];
int pt1(C a,C b)
{
	return a.r>b.r;
}
int pt2(C a,C b)
{
	return a.id<b.id;
}
double w,l;
int yz(int k)
{
	if(c[k].o.x<0||c[k].o.y<0||c[k].o.x>w||c[k].o.y>l)return 0;
	//cout<<c[k].o.x<<"  "<<c[k].o.y<<endl;
	for(int i=0;i<k;i++)
	{
		if(dist(c[i].o,c[k].o)<c[k].r+c[i].r+eps)return 0;
	}
	return 1;
}
line le[4];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;cin>>t;
	while(cin>>n>>w>>l)
	{	
		for(int i=0;i<n;i++)
			cin>>c[i].r,c[i].id=i;
		sort(c,c+n,pt1);
		c[0].o=P(0,0);
		c[1].o=P(w,l);
		le[0].a=le[1].a=P(0,0);
		le[0].b=le[3].a=P(w,0);
		le[1].b=le[2].a=P(0,l);
		le[2].b=le[3].b=P(w,l);
	//	for(int i=0;i<n;i++)
	//		cout<<c[i].id<<" "<<c[i].r<<"  "<<c[i].o.x<<"  "<<c[i].o.y<<endl;
		//cout<<c[0].r<<endl;
		for(int i=2;i<n;i++)
		{
			int fk=1;
			while(fk)
			{
				int k=rand()%i;
				C o=c[k];
				o.r+=c[i].r;
				for(int q=0;q<4;q++)
				{
					P p1,p2;
					if(ins(o,le[q],p1,p2))
					{
						c[i].o=p1;
						if(yz(i)){fk=0;break;}
						c[i].o=p2;
						if(yz(i)){fk=0;break;}
					}
					int z=rand()%i;
					if(z!=k)
					{
						C o2=c[z];
						o2.r+=c[i].r;
						if(ins(o,o2,p1,p2))
						{
							c[i].o=p1;
							if(yz(i)){fk=0;break;}
							c[i].o=p2;
							if(yz(i)){fk=0;break;}
						}
					}
					c[i].o.x=(rand()%10000)/10000.0*w;
					c[i].o.y=(rand()%10000)/10000.0*l;
					if(yz(i)){fk=0;break;}
						
				}
			}
			//cout<<c[i].o.x<<"  "<<c[i].o.y<<"   "<<c[i].r<<endl;
		}
		sort(c,c+n,pt2);
		printf("Case #%d:",cas++);
		for(int i=0;i<n;i++)
		{
//			cout<<c[i].id<<" "<<c[i].r<<"  "<<c[i].o.x<<"  "<<c[i].o.y<<endl;
			printf(" %.1lf %.1lf",c[i].o.x,c[i].o.y);
		}
		cout<<endl;
	}

}