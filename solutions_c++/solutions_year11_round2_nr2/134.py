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

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;

#define eps 1e-10
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f3fLL

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})
#define rep(x,n) for(int x = 0; x < (n); x++)

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

// var
const int maxn = 200 + 10;
int n, d;
int p[maxn], v[maxn];

int read() {
	scanf("%d %d",&n,&d);
	rep(i,n) {
		scanf("%d %d",p+i,v+i);
	}
	return 1;
}

int func(double tempo) {
	double pos = -(1LL<<40);
	rep(i,n) rep(j,v[i]) {
		double npos = max(pos + d, p[i] - tempo);
		double need = fabs(npos - p[i]);
		if(need < tempo || fabs(need-tempo) < 1e-12) {
			pos = npos;
		} else return 0;
	}
	return 1;
}

void process() {
	double res = 1;
	while(!func(res)) res *= 2;
	double take = res;
	for(int k = 100; k >= 0; k--) {
		double nres = res - take; take /= 2;
		if(nres >= 0 && func(nres)) {
			res = nres;	
		}
	}
	static int caso = 1;
	printf("Case #%d: %.7lf\n",caso++,res);
}

int main() {
	// solve
	int t; cin >> t;
	while(t-- && read()) {
		process();
	}
	return 0;
}
