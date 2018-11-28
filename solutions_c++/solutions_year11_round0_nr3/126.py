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
int n, a[1<<10];

int read() {
	scanf("%d",&n);
	rep(i,n) scanf("%d",a+i);
	return 1;
}

int caso = 1;

void process() {
	sort(a,a+n);
	ll _xor = 0, _sum = 0;
	rep(i,n) _xor = _xor ^ a[i], _sum += a[i];
	printf("Case #%d: ",caso++);
	if(_xor) printf("NO\n");
	else printf("%lld\n",_sum-a[0]);
}

int main() {
	// solve
	int t; cin >> t;
	while(t-- && read()) {
		process();
	}
	return 0;
}


