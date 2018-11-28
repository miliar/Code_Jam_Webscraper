#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <math.h>
using namespace std;

#define debug 0
#define dprintf debug&&printf


template <class T>
struct point {
  typedef T coord_type;
  typedef point S;
  typedef const S &R;
  T x, y;
  point(T _x=T(), T _y=T()) : x(_x), y(_y) { }
  bool operator< (R p) const {
    return x < p.x || x <= p.x && y < p.y;
  }
  S operator-(R p) const { return S(x - p.x, y - p.y); }
  S operator+(R p) const { return S(x + p.x, y + p.y); }
  S operator*(T d) const { return S(x * d, y * d); }
  S operator/(T d) const { return S(x / d, y / d); }
  T dot(R p)  const  { return x*p.x + y*p.y; }
  T cross(R p) const { return x*p.y - y*p.x; }
  T dist2() const { return dot(*this); }

  T dx(R p) const { return p.x - x; }
  T dy(R p) const { return p.y - y; }

  double dist() const { return sqrt(dist2()); }
  double angle() const { return atan2(y, x); }

  S unit() const { return *this / dist(); }
  S perp() const { return S(-y, x); }
  S normal() const { return perp().unit(); }

  double theta() {
    if (x==0 && y==0) return 0;
    double t = y / (x<0 ^ y<0 ? x-y : x+y);
    return x<0 ? y<0 ? t-2 : t+2 : t;
  }
};



int x[64], y[64], r[64];
double ans;

void t(int a, int b, int c){
	point<double> p(x[a], y[a]);
	double pr = r[a];
	point<double> q(x[b], y[b]);
	double qr = r[b];
	point<double> P = (p-q).unit()*pr+p;
	point<double> Q = (q-p).unit()*qr+q;
	double R1 = (P-Q).dist() / 2;
	double svar = R1;
	if(r[c] > svar)svar=r[c];
	dprintf("%lf %lf\n", R1, svar);
	if(svar<ans)ans=svar;
}

void test() {
	dprintf("\n");
	int n;
	int maxR=0;
	scanf("%d\n", &n);
	for(int i=0;i<n;i++){
		scanf("%d %d %d", &x[i], &y[i], &r[i]);
		if(r[i]>maxR)maxR=r[i];
	}
	if(n<=2){
		printf("%d\n", maxR);
	} else if(n==3){
		ans = 1e20;
		t(0,1,2);
		t(0,2,1);
		t(1,2,0);
		t(1,0,2);
		t(2,1,0);
		t(2,0,1);		
		printf("%lf\n", ans);
	} else
		printf("???\n");
}

int main(){
	int N;
	scanf("%d\n", &N);
	for(int fall=0;fall<N;fall++){	
		printf("Case #%d: ", fall+1);
		test();
	}
	return 0;
}
