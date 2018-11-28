#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<climits>

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for(int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,C) for(__typeof(C.begin()) i=C.begin(); i!=C.end(); ++i)
#define MP make_pair
#define FI first
#define SE second
#define PB push_back

using namespace std;

typedef long long LL;
typedef long double LD;

const int gen=1257258;
const LD PI = 3.14159265358979323846264338327950288419716939937511;
LD tab[gen];

void testcase(int tNum) {

	LD f,R,t,r,g;
	scanf("%llf %llf %llf %llf %llf",&f,&R,&t,&r,&g);
	
	if(2*f>=g || f>=R-t) {
		printf("Case #%d: 1.000000\n",tNum);
		return;
	}
	
	LD res=0.0, sum=0.0, dif=(R-t-f)/(gen*2.0);
	
	FOR(i,0,gen) {
		LD x = (2*i+1)*0.5/gen*(R-t-f);
		LD len = sqrt((R-t-f)*(R-t-f)-x*x);
		
		tab[i] = 0.0;
		
		LD x0=x-dif, x1=x+dif;
		LD a,z;
		int k;
		
		a = x0/(g+2*r);
		k = (int)a;
		z = x0-k*(g+2*r);
		if(z<r+f)
			x0 = k*(g+2*r)+(r+f); else if(z>g+r-f)
			x0 = (k+1)*(g+2*r)+(r+f);
			
		a = x1/(g+2*r);
		k = (int)a;
		z = x1-k*(g+2*r);
		if(z<r+f)
			x1 = k*(g+2*r)-(r+f); else if(z>g+r-f)
			x1 = (k+1)*(g+2*r)-(r+f);
		
		a = len/(g+2*r);
		k=(int)a;
		z = len-k*(g+2*r);
		
		z -= r+f;
		if(z>g-2*f) z=g-2*f;
		
		LD ok = k*(g-2*f);
		if(z>0.0) ok += z;
		
		if(x0<x1) tab[i] = ok*(x1-x0);
		
		//printf("x=%llf x0=%llf x1=%llf len=%llf sum=%llf res=%llf k=%d z=%llf\n",x,x0,x1,len,sum,res,k,z);
		
	}
	
	sort(tab, tab+gen);
	FOR(i,0,gen) res += tab[i];
	
	res *= 4;
	
	res /= R*R*PI;
	
	printf("Case #%d: %.6llf\n",tNum,1.0 - res);
	
}

int main() {
	
	srand(time(0));
	int t;
	scanf("%d",&t);
	FOR(i,0,t) testcase(i+1);
	
	return 0;
}
