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

using namespace std;
LL f[1000001], d[1000001], l[1000001], n, D;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("temp.in", "r", stdin); freopen("temp.out", "w", stdout);
#endif
int TEST; scanf("%d", &TEST);
for (int ti = 1; ti <= TEST; ti++){
	scanf("%I64d", &n); for (int i = 1; i <= n; i++) scanf("%I64d%I64d", &d[i], &l[i]);
	scanf("%I64d", &D);
	f[1] = d[1];
	bool ok = f[1] + d[1] >= D;
	for (int i = 2; i <= n; i++){
		f[i] = 0;
		for (int j = 1; j < i; j++) if (d[j] + f[j] >= d[i]){
			f[i] = max(f[i], min(l[i], d[i] - d[j]));
		}
		if (d[i] + f[i] >= D) ok = true;
	}
	printf("Case #%d: ", ti);
	cerr << ti << endl;
	puts(ok ? "YES" : "NO");
}
}
