#include<cstdio>
#include<cstring>
#include<queue>
#include<algorithm>
#include<vector>
#include<map>
#define MAX_N 1010
#define EPS (1e-15)
using namespace std;
int X, S, R, t, N;
int B[MAX_N], E[MAX_N], w[MAX_N];
double solve(){
	vector<pair<pair<int, int>, int> > v;
	vector<pair<int, pair<int, int> > > v2;

	int wod;
	double tt = 0;
	double res = 0;

	for(int i=0;i<N;++i){
		v.push_back(make_pair(make_pair(B[i], E[i]), w[i]));
	}
	sort(v.begin(), v.end());

	wod = 0;
	wod += v[0].first.first;
	for(int i=0;i<N-1;++i){
		wod += v[i+1].first.first - v[i].first.second;
	}
	wod += X - v[N-1].first.second;
	for(int i=0;i<N;++i){
		v2.push_back(make_pair(w[i], make_pair(B[i], E[i])));
	}
	sort(v2.begin(), v2.end());
	tt = t;
	tt = max(0.0, tt - (double)wod / R);
	res += t - tt;
	if(wod - R * tt > EPS){
		res += (double)(wod - R * (t - tt)) / S;
	}
	for(int i=0;i<N;++i){
		double tmp;
		int e, b, ww;
		ww = v2[i].first;
		b = v2[i].second.first;
		e = v2[i].second.second;
		if(tt > 0.0){
			tmp = min(tt, (double)(e - b) / (ww + R));
			res += tmp;
			res += (double)(e - b - (ww + R) * tmp) / (ww + S);
			tt = tt - tmp;
		}
		else{
			res += (double)(e - b) / (ww + S);
		}
	}
	return res;
}
int main(){
	int T;
	scanf("%d", &T);
	for(int i=1;i<=T;++i){
		scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		for(int j=0;j<N;++j){
			scanf("%d%d%d", &B[j], &E[j], &w[j]);
		}
		printf("Case #%d: %.10lf\n", i, solve());
	}
	return 0;
}
