#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
	int tc, tcN;
	scanf("%d", &tcN);
	for(tc=0; tc<tcN; ++tc){
		int X, S, R, N;
		double t;
		scanf("%d %d %d %lf %d", &X, &S, &R, &t, &N);
		vector<pair<double, double> > ar(N+1);
		for(int i=0; i<N; ++i){
			int a, o;
			double w;
			scanf("%d %d %lf", &a, &o, &w);
			ar[i] = make_pair(w, o-a);
			X -= o-a;
		}
		ar[N] = make_pair(0, X);
		sort(ar.begin(), ar.end());

		double res = 0;
		for(int i=0; i<N+1; ++i){
			double v = ar[i].first + R;
			double p = ar[i].second / v;
			if(t >= p){
				t -= p;
				res += p;
			}else{
				v = ar[i].first + R;
				double d = v * t;
				res += t;
				t = 0;
				d = ar[i].second - d;
				v = ar[i].first + S;
				p = d / v;
				res += p;
			}
		}

		printf("Case #%d: %.20f\n", tc+1, res);
	}
}
