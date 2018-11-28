#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define pt complex<double>
//kAc
const double pi = acos(-1.0), eps = 1e-9;
const int dx[8] = {1, -1, 0, 0, 1, 1, -1, -1};
const int dy[8] = {0, 0, 1, -1, 1, -1, -1, 1};
const int MO = (int)(1e9 + 7);

#define ALL(x) x.begin(), x.end()
#define fr(x, E) for (__typeof(E.begin()) x = E.begin(); x != E.end(); x++)
#define MP make_pair
#define PB push_back
#define FR first
#define SC second
#define ERR cerr << "ERROR" << endl
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PIII pair<PII, int>
#define PDI pair<double, int>
#define PID pair<int, double>
#define SZ(a) (int)((a).size())
#define VEC vector
#define STR string
#define ISS istringstream
#define OSS ostringstream
#define CLR(a, b) memset(a, b, sizeof(a))
#define gmin(a, b) { if (b < a) a = b; }
#define gmax(a, b) { if (b > a) a = b; }
#define y1 hehehe
using namespace std;

int n;
VEC<int> T;
int next[1000001], h[1000001];
bool doit(int l, int r, int k)
{
	if (l == r) return true;
	for (int i = l; i < r; i++) if (next[i] > r) return false;
	int now = l;
	VEC<int> T; T.clear();
	while(1){
		T.PB(now);
		if (now == r) break;
		now = next[now];
	}
	fr(x, T){
		int t = *x;
		h[t] = h[r] - (r - t) * k;
	}
	for (int i = 0; i < SZ(T) - 1; i++){
		int l = T[i], r = T[i + 1];
		if (doit(l + 1, r, k + 1) == false) return false;
	}
	return true;
}
int main()
{
freopen("temp.in", "r", stdin); freopen("temp.out", "w", stdout);
int TEST; cin >> TEST;
for (int ti = 1; ti <= TEST; ti++){
	printf("Case #%d: ", ti);
	scanf("%d", &n); for (int i = 1; i < n; i++) scanf("%d", &next[i]);
	h[n] = 1000000;
	if (!doit(1, n, 0)) puts("Impossible");
	else{
		for (int i =1 ; i <= n; i++) printf("%d ", h[i]);
		puts("");	
	}
}	
}

