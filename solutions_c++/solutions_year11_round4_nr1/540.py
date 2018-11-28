#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX_N = 1009;
int ws[MAX_N];
int bs[MAX_N], es[MAX_N], ls[MAX_N];
int as[MAX_N];
int S, R, X, N, _t;
pair<double, double> roads[MAX_N];

double solve(){
	double t = _t;
	double ret = 0;
	double d1 = 0;
	for(int i=0; i<N+1; i++){
		d1 += as[i];
	}
	if(d1/R > t){
		d1 -= R*t;
		ret += t;
		t = 0;
		ret += d1/S;
	}
	else{
		ret += d1/R;
		t -= d1/R;
	}
	for(int i=0; i<N; i++){
		roads[i] = make_pair(ws[i], ls[i]);
	}
	sort(roads, roads+N);
	for(int i=0; i<N; i++){
		if(roads[i].second/(R+roads[i].first) > t){
			roads[i].second -= (R+roads[i].first)*t;
			ret += t;
			t = 0;
			ret += roads[i].second/(S+roads[i].first);
		}
		else{
			ret += roads[i].second/(R+roads[i].first);
			t -= roads[i].second/(R+roads[i].first);
		}
	}
	return ret;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){
		scanf("%d%d%d%d%d", &X, &S, &R, &_t, &N);
		for(int i=0; i<N; i++){
			scanf("%d%d%d",bs+i, es+i, ws+i);
		}
		as[0] = bs[0];
		for(int i=0; i<N; i++){
			as[i+1] = (i==N-1?X:bs[i+1]) - es[i];
			ls[i] = es[i] - bs[i];
		}
		printf("Case #%d: %.9f\n",c, solve());
	}
	return 0;
}
