#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

typedef double D;
const D eps=1e-8;

struct P { // точка
	D x,y;
	P() {} 
	P(D x, D y): x(x), y(y) {} 
	P operator +(P a) {
		return P(x+a.x,y+a.y);
	}
	P operator -(P a) {
		return P(x-a.x,y-a.y);
	}
	P operator *(D k) { // умножение на скаляр
		return P(x*k,y*k);
	}
	D operator *(P a) { // векторное произведение
		return x*a.y-y*a.x;
	}
	D operator ^(P a) { // скалярное произведение
		return x*a.x+y*a.y;
	}
	D len() {
		return sqrt(x*x+y*y);
	}
	P perp() { // ортогональный вектор
		return P(y,-x);
	}
	P norm() { // нормированный вектор
		D l=len();
		if (abs(l)<eps) 
			return P(x,y);
		else
			return P(x/l,y/l);
	}
	bool operator ==(P a) {
		return abs(x-a.x)<eps && abs(y-a.y)<eps;
	}
	void load() {
		cin>>x>>y;
	}
};

struct L { // прямая, заданная уравнением ax+by+c=0
	D a,b,c;
	L() {}
	L(D a, D b, D c): a(a), b(b), c(c) {}
};

L getLine(P p1, P p2) { // дано: две несовпадающих точки p1 и p2. возвращает прямую, их содержащую
	D x0=p1.x, y0=p1.y;
	D al=(p2-p1).x, be=(p2-p1).y;
	return L(be,-al,al*y0-be*x0);
}

P getPoint(L l1, L l2) { // дано: две прямые l1 и l2, которые пересекаются. возвращает точку пересечения
	D det=l1.a*l2.b-l1.b*l2.a;
	D det1=-(l1.c*l2.b-l1.b*l2.c);
	D det2=-(l1.a*l2.c-l1.c*l2.a);
	return P(det1/det,det2/det);
}

struct C { // окружность с центром в точке о и радиусом r
	P o;
	D r;
	C() {}
	C(P o, D r): o(o), r(r) {}
	void load() {
		o.load();
		cin>>r;
	}
};

vector<P> crossCircleAndLine(C c, L l) {
	vector<P> res; // результат
	D al,be; // направляющий вектор прямой l
	al=l.b;
	be=-l.a;
	D x0,y0; // точка на прямой l
	if (abs(l.a)<eps) {
		x0=0;
		y0=-l.c/l.b;
	} else {
		y0=0;
		x0=-l.c/l.a;
	}
	// теперь x=x0+al*t, y=y0+be*t, подставляем в уравнение окружности и решаем квадратное уравнение a*t^2+b*t+c=0;
	D A,B,C,t;
	A=sqr(al)+sqr(be);
	B=2*al*(x0-c.o.x)+2*be*(y0-c.o.y);
	C=sqr(x0-c.o.x)+sqr(y0-c.o.y)-sqr(c.r);
	D d=B*B-4*A*C; // дискриминант
	if (d<-eps) return res; // решений нет
	if (d<0) d=0; // чтобы не было RE при d чуть меньшем нуля
	t=(-B+sqrt(d))/(2*A); // одно решение
	res.push_back(P(x0+al*t,y0+be*t));
	t=(-B-sqrt(d))/(2*A); // второе решение
	res.push_back(P(x0+al*t,y0+be*t));
	return res;
}

vector<P> crossTwoCircles(C c1, C c2) {
	// вычев из одного уравнения окружности другое, получим уравнение прямой ax+by+c=0
	D a,b,c;
	a=2*(c2.o.x-c1.o.x); 	
	b=2*(c2.o.y-c1.o.y);
	c=sqr(c2.r)-sqr(c1.r)+sqr(c1.o.x)-sqr(c2.o.x)+sqr(c1.o.y)-sqr(c2.o.y);
	return crossCircleAndLine(c1,L(a,b,c));
}

int n;
C c[50];

bool inside(C c1, C c2) { // c1 in c2
	D d=(c1.o-c2.o).len();
	return d+c1.r<c2.r+eps;
}

bool check(P o1, P o2, D r) {
	for (int i=0; i<n; i++)
		if (!inside(c[i],C(o1,r)))
			if (!inside(c[i],C(o2,r)))
				return false;
	return true;
}

bool check(D x) {
	for (int i=0; i<n; i++) {
		if (x<c[i].r-eps) continue;
		for (int j=i+1; j<n; j++) {
			if (x<c[j].r-eps) continue;
			C c1(c[i].o,x-c[i].r);
			C c2(c[j].o,x-c[j].r);
			vector<P> cr1=crossTwoCircles(c1,c2);
			cr1.pb(c[i].o);
			cr1.pb(c[j].o);
			for (int t1=0; t1<sz(cr1); t1++) {
				for (int ii=0; ii<n; ii++) {
					if (x<c[ii].r-eps) continue;
					for (int jj=ii+1; jj<n; jj++) {
						if (x<c[jj].r-eps) continue;
						C cc1(c[ii].o,x-c[ii].r);
						C cc2(c[jj].o,x-c[jj].r);
						vector<P> cr2=crossTwoCircles(cc1,cc2);
						cr2.pb(c[ii].o);
						cr2.pb(c[jj].o);
						for (int t2=0; t2<sz(cr2); t2++) 
							if (check(cr1[t1],cr2[t2],x))
								return true;
					}
				}
			}
		}
	}
	return false;
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst);
		cin>>n;
		for (int i=0; i<n; i++)
			c[i].load();
		double l=0, r=1e20;
		for (int step=0; step<100; step++) {
			double m=(l+r)/2;
			if (check(m))
				r=m;
			else
				l=m;
		}
		printf("%.20lf\n",r);
	}

	return 0;
}
