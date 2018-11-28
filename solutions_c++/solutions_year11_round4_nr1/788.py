#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstdio>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i) 
#define FILL(v,x) memset((v), (x), sizeof(v));
#define INF 0x3f3f3f3f
#define EPS 1E-8
#define debug(x) cerr << #x << " = " << x << "\n"; 
#define debugv(x,n) cerr << #x << " = ["; REP(i,n) cerr << x[i] << ","; cerr << "\b]\n";
typedef long long int64;
typedef pair<int,int> pii;

pair <int,pii > w[2000];

int cmp(double a, double b){
	if (fabs(a-b)<1E-8) return 0;
	if (a<b) return -1;
	return 1;
}

int main() {
	int nt;

	scanf("%d",&nt);
	for (int ct=1; ct<=nt; ct++) {
		int x,s,r,n;
		double t;
		scanf("%d %d %d %lf %d",&x,&s,&r,&t,&n);
		REP(i,n) {
			scanf("%d %d %d",&w[i].first, &w[i].second.first, &w[i].second.second);
		}

		w[n].first=x; w[n].second.first=x;
		w[n].second.second=0;
		n++;

		sort(w,w+n);

		int pos = 0;
		double res = 0;

		REP(i,n) {
			int p = w[i].first, q = w[i].second.first;
			int vw = w[i].second.second;
			double run = min(t, (double) (p - pos) / r);
			double wlk = ((p-pos) -(r*run)) / s;
			
			t-=run;

			//printf("%d %d %lf %lf\n",pos, p, run, wlk);

			res+= run + wlk;
			pos = q;
		}

		bool us[2000];
		memset(us,0,sizeof(us));

		REP(i,n) {
			int mn = -1;
			REP(j,n) {
				int pj = w[j].first, qj = w[j].second.first;
				int vwj = w[j].second.second;
				if (!us[j] && (mn == -1 || vwj < w[mn].second.second))
					mn = j;
			}
			int p = w[mn].first, q = w[mn].second.first;
			int vw = w[mn].second.second;
			
			us[mn]=true;
			
			double run = min(t, (double) (q - p) / (r+vw));
			double wlk = ((q-p) -((r+vw)*run)) / (s+vw);
			
			t-=run;
			res+= run + wlk;

			//printf("%d %d %lf %lf\n",p, q, run, wlk);
			pos = q;
		}
		printf("Case #%d: %.7lf\n",ct, res);
	}

	return 0;
}
