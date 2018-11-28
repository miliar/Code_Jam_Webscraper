#include <map> 
#include <set> 
#include <queue> 
#include <bitset> 
#include <valarray> 
#include <complex> 
#include <iostream> 
#include <sstream> 
#include <cmath> 
#include <algorithm> 
#include <string> 
#include <cassert> 

using namespace std;

// prewritten code

#define Size(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define RepV(i,v) for (int i=0;i<Size(v);++i)
#define All(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Abs(a) ((a)<0?-(a):(a))
#define VVI vector<vector<int> >
#define VI vector<int>
#define VVS vector<vector<string> >
#define VS vector<string>
#define ForEach(it,a) for (typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)
#define DBG(x) cout << #x <<" = "<< x << endl;
#define DBGA(x) {cout << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cout<<x[i]<<' '; cout<<endl;}
#define DBGV(x) {cout << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cout<<x[i]<<' '; cout<<endl;}

const string problem_name = "C-large";

const long double eps = 1e-14;
const long double pi = acos(-1.0);

bool eq(long double a, long double b){
	return Abs(a-b) < eps;
}

bool ls(long double a, long double b){
	return a + eps < b;
}

bool gt(long double a, long double b){
	return b + eps < a;
}

bool lse(long double a, long double b){
	return ls(a,b) || eq(a,b);
}

bool gte(long double a, long double b){
	return gt(a,b) || eq(a,b);
}

inline long double perv(long double rr, long double x, long double y0){
	long double a;

	if (eq(x,rr)) a = pi/2;
	else a = atan( x/sqrt(rr*rr-x*x) );

	long double res = x*sqrt(rr*rr-x*x)+rr*rr*a;

	return res/2.0 - y0*x;
}

long double solve(long double R, long double t, long double r, long double g){
	if (gte(t,R)) return 1.0;
	if (lse(g,0)) return 1.0;
	if (gte(r,R-t)) return 1.0;
	long double rr = R-t, sq = 0.0;

	for (long double x = r; ls(x,rr); x += (g+2*r))
		for (long double y = r; ls(y*y,rr*rr-x*x); y += (g+2*r)){
			long double xl, xr, nx=x+g, ny=y+g;

			if ( gte(ny,sqrt(rr*rr-x*x)) ) {
				xl = x; xr = Min(nx,sqrt(rr*rr-y*y));
				
				sq += perv(rr,xr,y)-perv(rr,xl,y);

			} else if (gte(nx,sqrt(rr*rr-ny*ny))) {
				
				xr = Max(Min(nx,sqrt(rr*rr-y*y)),x);
				
				xl = Max(sqrt(rr*rr-ny*ny),x);

				sq += perv(rr,xr,y)-perv(rr,xl,y);
				sq += (xl-x)*g;

			} else {
				sq += g*g;
			}
		}
	return 1 - sq*4.0/(pi*R*R);
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);

	int tt;
	scanf("%d",&tt);

	For(z,1,tt){
		printf("Case #%d: ",z);

		long double f, R, t, r, g;
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		printf("%.6lf\n",solve(R,t+f,r+f,g-2*f));

	}
	return 0;
}
