#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FORS(i,s) for(int i=0;(s)[i];i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back
#define EPS 1e-8
#define FZ(x) (fabs(x)<EPS)

int n;

double w,l;

#define RR ((rand()%1000)/1000.0)

struct C{
	double x;
	double y;
	double r;

	static double Dist(const C &a, const C &b){
		return sqrt((a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y));
	}

	static bool Rep(C &a, C &b){
		double d = Dist(a,b);
		if(d >= a.r+b.r+EPS)return false;
		d = (a.r+b.r+EPS-d)/2.0;
		double tx = a.x-b.x, ty = a.y-b.y;
		if(FZ(tx) && FZ(ty)){
			a.x += RR-0.5;
			a.y += RR-0.5;
			b.x += RR-0.5;
			b.y += RR-0.5;
			return true;
		}

		double m = d / sqrt(tx*tx+ty*ty);
		a.x += m*tx; a.y += m*ty;
		b.x -= m*tx; b.y -= m*ty;

		return true;
	}

	bool Conf(){
		bool r = false;
		if(x < 0+EPS){
			x = 0+EPS; r = true;
		}
		if(y < 0+EPS){
			y = 0+EPS; r = true;
		}
		if(x > w-EPS){
			x = w-EPS; r = true;
		}
		if(y > l-EPS){
			y = l-EPS; r = true;
		}
		return r;
	}
};

C a[10000];


int main() {

int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d%lf%lf", &n, &w, &l);
	srand(n+12);

	FOR(i,0,n){
		scanf("%lf", &a[i].r);
		a[i].r *= 2.0;
		a[i].x = RR * w;
		a[i].y = RR * l;
	}

	bool ok = false;
	int nit = 0;
	while(!ok){
		ok = true;
		FOR(i,0,n)FOR(j,i+1,n){
			if(C::Rep(a[i],a[j])) ok = false;
		}
		FOR(i,0,n) if(a[i].Conf()) ok = false;

		if(ok) break;
		nit++;

		if((nit > 100) && nit < 800 && (nit % 10 == 0)){
			FOR(i,0,n){
				a[i].x += RR - 0.5;
				a[i].y += RR - 0.5;
			}
		}

		/*if(nit % 100 == 0){
			FOR(i,0,n){
				printf(" %.8f %.8f", a[i].x, a[i].y);
			}
			printf("\n");
		}*/
		//if(nit > 1000)break;
	}

	printf("Case #%d:", ++tt);
	FOR(i,0,n){
		printf(" %.12f %.12f", a[i].x, a[i].y);
	}
	printf("\n");
}
	return 0;
}


