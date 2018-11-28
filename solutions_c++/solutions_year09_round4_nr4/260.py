#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

struct point{
	double x,y;
	void read(){
		scanf("%lf%lf",&x,&y);
	}
};

struct circle{
	point p;
	double r;
};

circle plants[45];

int n;

double sq(double x){
	return x * x;
}

double dist(point a,point b){
	return sqrt(sq(a.x-b.x) + sq(a.y-b.y));
}

bool ok(point p1,point p2,double r){
	for(int i=1;i<=n;i++){
		if(min(dist(p1,plants[i].p),dist(p2,plants[i].p)) > r - plants[i].r + 1E-8) return 0;
	}
	return 1;
}

point posp[10000];
int cp;

bool check(double r){
	for(int i=1;i<=n;i++) posp[i] = plants[i].p;
	cp = n;
	for(int i=1;i<=n;i++){
		for(int j=i+1;j<=n;j++){
			circle c1,c2;
			c1.p = plants[i].p;
			c2.p = plants[j].p;
			c1.r = r - plants[i].r;
			c2.r = r - plants[j].r;
			double d = dist(c1.p,c2.p);
			if(d > c1.r + c2.r) continue;
			if(d < abs(c1.r - c2.r)) continue;
			if(abs(c1.r - c2.r) < 1E-9 && d < 1E-9) continue;
			double a = (sq(c1.r) - sq(c2.r) + sq(d)) / (2 * d);
			double h = sqrt(sq(c1.r) - sq(a));
			point md;
			md.x = c1.p.x + a * (c2.p.x - c1.p.x) / d;
			md.y = c1.p.y + a * (c2.p.y - c1.p.y) / d;
			point p1,p2;
			p1.x = md.x + h * (c2.p.y - c1.p.y) / d;
			p1.y = md.y - h * (c2.p.x - c1.p.x) / d;
			p2.x = md.x - h * (c2.p.y - c1.p.y) / d;
			p2.y = md.y + h * (c2.p.x - c1.p.x) / d;
			posp[++cp] = p1;
			posp[++cp] = p2;
		}
	}
	for(int i=1;i<=cp;i++){
		for(int j=i;j<=cp;j++){
			if(ok(posp[i],posp[j],r)) return 1;
		}
	}
	return 0;
}

void alg(){
	scanf("%d",&n);
	double l=0,r=100000;
	for(int i=1;i<=n;i++){
		plants[i].p.read();
		scanf("%lf",&plants[i].r);
		l = max(l,plants[i].r);
	}
	while(r-l > 1E-7){
		double c = (r+l)/2;
		if(check(c)) r=c;
		else l=c;
	}
	printf("%.7lf\n",(l+r)/2.0);
}

int main(){
	int d;
	scanf("%d",&d);
	for(int i=1;i<=d;i++){
		printf("Case #%d: ",i);
		alg();
	}
}
