// Tim  defines
#include <vector> 
#include <queue> 
#include <set>
#include <map>

#include <numeric>
#include <algorithm> 
#include <string.h> 

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 

using namespace std;
//#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define Rep(i,n) for (int i=0;i<(n);++i)
#define RepV(i,v) for (int i=0;i<sz(v);++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
typedef long long LL;
typedef pair <int,int> PI;
typedef pair<double, double> PD;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;
const int oo = (1<<30);
const double eps = 1e-10;
const double INF = 1e10;

int n,m, T;
vector<double> r;
vector<PD> v;

PD operator- (PD a, PD b){
	return make_pair(a.first-b.first,a.second-b.second);
}

double sq(double x, double y){
	return sqrt(x*x+y*y);
}

double sq(PD x){
	return sq(x.first, x.second);
}

double go(int a, int b){
	return sq(v[a] - v[b]) + r[a]+r[b];
}

int main() { 
	freopen("D.in","rt",stdin);
	freopen("D.out","wt",stdout);
	scanf("%d",&T);
	For(TT,1,T){
		scanf("%d\n",&n);
		v.resize(n);
		r.resize(n);
		Rep(i,n){
			scanf("%lf%lf%lf",&v[i].first,&v[i].second,&r[i]);
		}

		double res = INF;
		if (n == 1) res = 2*r[0];
		if (n == 2) res = 2*max(r[0],r[1]);
		if (n == 3) {
			res = min(res,go(0,1));
			res = min(res,go(2,1));
			res = min(res,go(0,2));
		}




		printf("Case #%d: %.6lf\n",TT,res/2.0);
	}
	

	return 0;
}


