#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << (int)*i << " "; cout << endl; }

typedef long long ll;

const double eps = 1e-10;
const int inf  = 0x3f3f3f3f;
const ll INF = 0x3f3f3f3f3f3f3f3fLL;

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define rep(x,n) fr(x,0,n)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

// var
int X, _S, R, T, N;
int B[1<<10], E[1<<10], W[1<<10];

int read() {
	cin >> X >> _S >> R >> T >> N;
	rep(i,N) cin >> B[i] >> E[i] >> W[i];
	return 1;
}

#define F first
#define S second

vector< pair<ll,ll> > vet;

int comp(pair<ll,ll> a, pair<ll,ll> b) {
	return a.S < b.S;
	//return a.F * (b.S + R) > b.F * (a.S + R); 
	if(a.F != b.F) return a.F > b.F;
	return a.S < b.S;
}

void process() {
	static int caso = 1;
	printf("Case #%d:", caso++);
	
	vet.clear();
	for(int at = 0, prox = 0; at < X;) {
		int dist = X - at, v = 0;
		if(prox < N) {
			dist = B[prox] - at;
		}
		vet.push_back( pair<ll,ll>(dist, v) );
		at += dist;
		if(prox < N) {
			v += W[prox];
			dist = min(X, E[prox]) - at;
			vet.push_back( pair<ll,ll>(dist, v) );
			at += dist;
			prox++;
		}
	}
	
	sort(vet.begin(),vet.end(),comp);
	
	double tot = 0, _t = T;
	
	rep(i,vet.size()) {
		double dist = vet[i].F, v = vet[i].S + R;
		double ndist = min(dist, v * _t);
		double resta = dist - ndist;

		dist = ndist;
		tot += dist / v;
		_t -= dist / v;
		
		tot += resta / (_S + vet[i].S);
	}
	
	printf(" %.7lf\n", tot);
}

int main() {
	// solve
	int t; scanf("%d",&t);
	while(t-- && read()) {
		process();
	}
	return 0;
}

