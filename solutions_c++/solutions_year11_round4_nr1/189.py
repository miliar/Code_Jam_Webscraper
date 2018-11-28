#include <map>        
#include <set>        
#include <queue> 
#include <cmath>       
#include <cstdio>      
#include <vector>        
#include <string>        
#include <sstream>       
#include <iostream>       
#include <algorithm>        
using namespace std;        
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)        
#define FORE(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)        
#define SET(x, v) memset(x, v, sizeof (x))        
#define sz size()        
#define cs c_str()        
#define pb push_back        
#define mp make_pair       
    
typedef long long ll;

vector<pair<int, pair<int, int> > > dat;
int main() {
	int e = 0, T;
	scanf("%d",&T);
	while(T--) {
		double ans = 0.;
		int x, s, r, t, n;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		double tt = t, ss = s, rr = r;
		dat.resize(n*2+10);
		int last = 0;
		int nn = 0;
		FOR(i,0,n) {
			int st, end, w;
			scanf("%d%d%d",&st,&end,&w);
			if(last < st) {
				dat[nn] = mp(0, mp(last, st) );
				nn++;
			}
			dat[nn] = mp(w, mp(st, end) );
			nn++;
			last = end;
		}
		if(last < x) {
			dat[nn] = mp(0, mp(last, x) );
			nn++;
		}
		dat.resize(nn);
		sort(dat.begin(), dat.end());
		double dist = 0.;
		//for(int i = n-1;i>=0;--i) {
		FOR(i,0,nn) {
			if(tt > 0.) {
				double tmp = (dat[i].second.second - dat[i].second.first) / (rr + dat[i].first);
				if(tmp <= tt) {
					tt-= tmp;
					ans += tmp;
				}
				else {
					ans += tt +  ((dat[i].second.second - dat[i].second.first) - (tt * (rr+dat[i].first))) / (ss + dat[i].first);
					tt = 0.;
				}
			}
			else {
				ans += (dat[i].second.second - dat[i].second.first) / (ss + dat[i].first);
			}
			dist += dat[i].second.second - dat[i].second.first;
			/*
			printf("\t[+%d: %d..%d] (tt = %.6lf, dist = %.6lf, ans = %.6lf)\n", dat[i].first,
				dat[i].second.first,
				dat[i].second.second,
				tt, dist, ans);
			*/
		}
		/*
		printf("%d %d %d %d %d\n", x, s, r, t, n);
		printf("ans  = %.10lf\n", ans);
		printf("tt   = %.10lf\n", tt);
		printf("dist = %.10lf\n\n", dist);
		*/
		if(tt > 0.) {
			double tmp = (x - dist) / rr;
			if(tmp <= tt) 
				ans += tmp;
			else {
				ans += tt + ((x - dist) - tt*rr) / ss;
			}
		}
		else
			ans += (x - dist) / ss;
		printf("Case #%d: %.10lf\n", ++e, ans);
	}
	return 0;
}

/*
Case #1: 4.000000
Case #2: 5.500000
Case #3: 3.538095238

*/