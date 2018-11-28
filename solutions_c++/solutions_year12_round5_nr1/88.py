#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <vector>
//#define DEBUG
#ifdef DEBUG
	#define DEB printf
	#define FF fflush(stdout)
	#define unordered_set set
	#define unordered_map map
#else
	#define DEB(...) 
	#define FF
#endif
#define REP(x, n) for(int x = 0; x < (n); x++)
#define FOR(x, b, e) for(int x = (b); x <= (e); x++)
#define FORD(x, u, d) for(int x = (u); x >= (d); x--)
#define VAR(x, a) __typeof(a) x = (a)
#define FOREACH(x, c) for(VAR(x, (c).begin()); x != (c).end(); x++)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

using namespace std;
using namespace tr1;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<pair<int, int> > VPII;
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int INF = 1000000001;

const int N = 1000;

int t;
int n, p[N], l[N];
int tab[N];

bool comp(int a, int b) {
	int va = 100 * l[a] + (100 - p[a]) * l[b];
	int vb = 100 * l[b] + (100 - p[b]) * l[a];
	if(va < vb) return true;
	if(va > vb) return false;
	return a < b;
}

int main() {
	scanf("%d", &t);
	
	REP(xx, t) {
		scanf("%d", &n);
		REP(i, n) scanf("%d", &l[i]);
		REP(i, n) scanf("%d", &p[i]);
		REP(i, n) tab[i] = i;
		REP(i, n) REP(j, n - 1) if(!comp(tab[j], tab[j + 1])) swap(tab[j], tab[j + 1]);

		printf("Case #%d: ", xx + 1);
		REP(i, n) printf("%d ", tab[i]);
		printf("\n");
	}

	return 0;
}
