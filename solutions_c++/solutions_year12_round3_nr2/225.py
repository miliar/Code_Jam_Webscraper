#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <string.h>
#include <cassert>

#ifdef _DEBUG
#define typeof(X) std::identity<decltype(X)>::type //C++0x (for vs2010)
#else
#define typeof(X) __typeof__(X) // for gcc
#endif

#define sz(a)  int((a).size())
#define FOREACH(it, c) for (typeof((c).begin()) it=(c).begin(); it != (c).end(); ++it)
#define FOR(i,count) for (int i = 0; i < (count); i++)
#define V_CIN(v) do{for(int i = 0; i < sz(v); i++) cin >> (v)[i];}while(0)
#define all(c) (c).begin(),(c).end()

using namespace std;
static const double EPS = 1e-5;
typedef long long ll;
const int MODULO = 1000000007;
const int INF = 100000000; //1e8

typedef pair<ll,int> P;

double D;
int N,A;
double t[2010],x[2010];

void solve1(double a){
	double my = 0.0;
	double v = 0.0;
	for(int i = 1; i < N; i++){
		double next = x[i];
		double time_diff = t[i] - t[i-1]; 
		double other_v = (x[i] - x[i - 1]) / time_diff;
		if(next > D){
			next = D;
			time_diff = (next - x[i - 1]) / (x[i] - x[i - 1]) * time_diff;
		}
		double diff = next - my;
		double time = (-v + sqrt(v * v + 2 * a * diff)) / a;

		if(time < time_diff){
			my += v * time_diff + 1/2.0 * a * time_diff * time_diff;
			v += a * time_diff;
			time = time_diff;
		} else {
			my = x[i];
			v = other_v;
		}

		if(next >= D) {
			double ans = t[i - 1] + time;
			printf("%.10f\n",ans);
			return;
		}
	}
	return ;
}

void solve()
{
	double a[250];
	cin >> D >> N >> A;
	FOR(i,N) cin >> t[i] >> x[i];
	t[N] = t[N-1] + 0.0001; x[N] = INT_MAX;
	N++;
	FOR(i,A) cin >> a[i];

	FOR(i,A){
		solve1(a[i]);
	}
}

int main(){
	int t;
	cin >> t;
	FOR(i,t){
		printf("Case #%d:\n",i+1);
		solve();
	}
	return 0;
}