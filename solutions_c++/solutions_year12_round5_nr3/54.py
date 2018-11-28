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

typedef long long LL;
typedef vector<int> VI;
typedef pair<LL, LL> PII;
typedef vector<pair<LL, LL> > VPII;
typedef unsigned long long ULL;
typedef long double LD;

//const int INF = 1000000001;
const int N = 200;

int t;
LL m, f, n;
PII meal[N + 1];
VPII meals;

bool comp(PII a, PII b) {
	if(a.ST == b.ST) return a.ND > b.ND;
	return a.ST < b.ST;
}


int main() {
	scanf("%d", &t);
	
	REP(xx, t) {
		scanf("%lld%lld%lld", &m, &f, &n);
		REP(i, n) {
			scanf("%lld%lld", &meal[i].ST, &meal[i].ND);
			meal[i].ND++;
		}
		n++;
		meal[n - 1] = MP(0, 0);
		sort(meal, meal + n, comp);
		meals.clear();
		meals.PB(meal[0]);
		FOR(i, 1, n - 1) if(meal[i].ND > meals.back().ND) meals.PB(meal[i]); 

		
/*		REP(i, n) {
			DEB("%lld %lld, ", meal[i].ST, meal[i].ND);
		}
		DEB("\n");
*/
		REP(i, SIZE(meals)) {
			DEB("%lld %lld, ", meals[i].ST, meals[i].ND);
		}
		DEB("\n");
		
		LL csum = f, clen = 0, res = 0, cres;

		REP(i, SIZE(meals)) {
			csum += (meals[i].ND - clen) * meals[i].ST;
			clen = meals[i].ND;
			cres = (m / csum) * clen;
			if(i < SIZE(meals) - 1) {
				cres += min((m % csum) / meals[i + 1].ST , (m / csum) * (meals[i + 1].ND - clen));
			}
			DEB("csum = %lld, clen = %lld, cres = %lld\n", csum, clen, cres);
			res = max(res, cres);
		}
		
		csum = f, clen = 0;
		DEB("Type 2\n");
		
		FOR(i, 1, SIZE(meals) - 1) {
			LL ocsum = csum, oclen = clen;
			csum += (meals[i].ND - clen) * meals[i].ST;
			clen = meals[i].ND;
			LL n1 = m / csum, n2 = n1 + 1;
			cres = (m / csum) * clen;
			if(ocsum <= (m % csum)) {
				cres += oclen + (m % csum - ocsum) / meals[i].ST;
			}
			DEB("csum = %lld, clen = %lld, cres = %lld\n", csum, clen, cres);
			res = max(res, cres);
			
			if(n2 * ocsum <= m) {
				cres = n2 * oclen + ((m - n2 * ocsum) / meals[i].ST);
				res = max(res, cres);
			}
			DEB("csum = %lld, clen = %lld, cres = %lld\n", csum, clen, cres);
		}

		printf("Case #%d: %lld\n", xx + 1, res);

	}

	return 0;
}
