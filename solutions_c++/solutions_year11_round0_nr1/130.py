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
const int maxn = 100 + 50;

int n;
char cor[maxn][10];
int pos[maxn];

int read() {
	cin >> n;
	rep(i,n) cin >> cor[i] >> pos[i];
	return 1;
}

struct S { int blue, orange, k, now; };
char f[maxn][maxn][maxn];
queue<S> q;

void update(S s) {
	if(s.blue <= 0 || s.blue >= maxn || s.orange <= 0 || s.orange >= maxn || f[s.blue][s.orange][s.k]) return;
	f[s.blue][s.orange][s.k] = 1, q.push(s);
}

int caso = 1;

void process() {
	memset(f,0,sizeof f);
	while(q.size()) q.pop();
	S ini = {1,1,0,0};
	update(ini);
	while(!q.empty()) {
		S s = q.front(); q.pop();
		if(s.k >= n) {
			printf("Case #%d: %d\n",caso++,s.now);
			return;
		}
		// push, toLeft, toRigth
		rep(i,3) rep(j,3) {
			S ns = s; int ok = 1;
			switch(i) {
				case 0:
					if(cor[s.k][0] == 'O' && pos[s.k] == s.orange) {
						ns.k++;
					} else ok = 0;
					break;
				case 1:
					ns.orange--;
					break;
				case 2:
					ns.orange++;
				break;
			}
			switch(j) {
				case 0:
					if(cor[s.k][0] == 'B' && pos[s.k] == s.blue) {
						ns.k++;
					} else ok = 0;
					break;
				case 1:
					ns.blue--;
					break;
				case 2:
					ns.blue++;
				break;
			}
			ns.now++;
			update(ns);
		}
	}
	assert(0);
}

int main() {
	// solve
	int t; cin >> t;
	while(t-- && read()) {
		process();
	}	
	return 0;
}

