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
ll n, pd, pg;

int read() {
	cin >> n >> pd >> pg;
	return 1;
}

ll gcd(ll x, ll y) {
	while(x) {
		y %= x;
		swap(x,y);
	}
	return max(y,1LL);
}

void process() {
	string s("Broken");
	if( (pg == 100 && pd != 100) || (pg == 0 && pd != 0) ) {} 
	else if(100/gcd(100,pd) <= n) {
		s = string("Possible");
	}
	static int caso = 1;
	printf("Case #%d: %s\n",caso++,s.c_str());
}

int main() {
	// solve
	int t; cin >> t;
	while(t-- && read()) {
		process();
	}
	return 0;
}

