#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <ctime>
#include <climits>
#include <cassert>
//#pragma comment(linker, "/STACK:640000000")
#ifdef _Win32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define next ksdjgsd
#define prev lsfnasd
using namespace std;
typedef long long ll;
typedef double ld;
typedef pair<int, int> pi;
typedef pair<ld, pi> pii;

const ld E=1e-8;
const int inf=(int)1e9;

struct pt{
	ld x, y;
	pt(){}
	pt(ld _x, ld _y):x(_x), y(_y){}
};


int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	for(int tt=0;tt<tn;tt++){
		//cerr<<tt<<"\n";
		int w, l, u, g;
		scanf("%d%d%d%d", &w, &l, &u, &g);
		pt lb[110];
		pt ub[110];
		pii f[210];
		ld x, y;
		//cerr<<"OK\n";
		for(int i=0;i<l;i++){
			scanf("%lf%lf", &x, &y);
			lb[i].x=x;
			lb[i].y=y;
			f[i]=mp(x, mp(i, 0)); 
		}
		for(int i=0;i<u;i++){
			scanf("%lf%lf", &x, &y);
			ub[i].x=x;
			ub[i].y=y;
			f[i+l]=mp(x, mp(i, 1)); 
		}
		//cerr<<"OK\n";
		sort(f, f+u+l);
		x=0;
		ld S=0;
		ld la=0, ua=0;
		ld ly=lb[0].y, uy=ub[0].y;
		//cerr<<"OK\n";
		for(int i=0;i<u+l;i++){
			ld x2=f[i].fs;
			S+=(uy-ly)*(x2-x);
			S+=0.5*(x2-x)*(x2-x)*(ua-la);
			ly+=la*(x2-x);
			uy+=ua*(x2-x);
            if(i<u+l-2){
            	int k=f[i].sc.fs;
            	if(f[i].sc.sc==0) la=(lb[k+1].y-lb[k].y)/(lb[k+1].x-lb[k].x);
				else ua=(ub[k+1].y-ub[k].y)/(ub[k+1].x-ub[k].x);
			}
			x=x2;
		//	cerr<<i<<" s="<<S<<" ly="<<ly<<" uy="<<uy<<" la="<<la<<" ua="<<ua<<endl;
		}
		//cerr<<S<<endl;
		ld res[210];
		int h=1;
		x=0;
		la=0, ua=0;
		ly=lb[0].y, uy=ub[0].y;
		ld s=0;
		//cerr<<"OK\n";
		for(int i=0;i<u+l;i++){
			ld x2=f[i].fs;
			ld s2=s;
			s2+=(uy-ly)*(x2-x);
			s2+=0.5*(x2-x)*(x2-x)*(ua-la);
			while(s2>=S*h/g-E){
				//cerr<<h<<" ";
				ld ds=S*h/g-s;
				ld dy=uy-ly;
				ld da=ua-la;
				ld t;
				if(fabs(da)>E) t=(-dy+sqrt(dy*dy+2*da*ds))/da;
				else t=ds/dy;
				res[h++]=x+t;
				//cerr<<"OK\n";
			}
			ly+=la*(x2-x);
			uy+=ua*(x2-x);
            if(i<u+l-2){
            	int k=f[i].sc.fs;
            	if(f[i].sc.sc==0) la=(lb[k+1].y-lb[k].y)/(lb[k+1].x-lb[k].x);
				else ua=(ub[k+1].y-ub[k].y)/(ub[k+1].x-ub[k].x);
			}
			x=x2;
			s=s2;		
		}
		//cerr<<"OK\n";
		printf("Case #%d:\n", tt+1);
		for(int i=1;i<g;i++) printf("%.10lf\n", res[i]);
	}
				
	return 0;
}
