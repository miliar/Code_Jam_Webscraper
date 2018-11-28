#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)
#define FORE(i,a) for (__typeof(a.begin()) i=a.begin(); i!=a.end(); i++)

double boost(double D, int W, int R, double &t){
	if (t < 1e-9) return D / W;
	double lo=0, hi=t;
	REP(i,100){
		double mid = (lo+hi)/2;
		double travel = R * mid;
		if (travel > D){
			hi = mid;
		} else {
			lo = mid;
		}
	}
	double need = (lo+hi)/2;
	t -= need;
	D -= need * R;
//	printf("%lf, d = %lf\n",need, D);
	need += D / W;
	return need;
}

int nTC,X,S,R,N;
double t;

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d: ",TC);
		scanf("%d %d %d %lf %d",&X,&S,&R,&t,&N);

		vector<pair<int,int> > arr;
		int walk = X, B,E,w;
		double res = 0;
		REP(i,N){
			scanf("%d %d %d",&B,&E,&w);
			int ele = E - B;
			walk -= ele;
			arr.push_back(make_pair(w,ele));
		}
		if (walk > 0) arr.push_back(make_pair(0,walk));
		sort(arr.begin(), arr.end());
		REP(i,arr.size()){
			int W = arr[i].first, D = arr[i].second;
			res += boost(D,W+S,W+R,t);
			//printf("walk = %d, w=%d, r=%d, t=%lf, %lf\n",walk,S,R,t,res);
		}
		printf("%.9lf\n",res);
	}
}
