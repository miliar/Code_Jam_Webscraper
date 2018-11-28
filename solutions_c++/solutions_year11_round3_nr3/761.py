#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <list>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORE(it,V) for(__typeof(V.begin()) it = V.begin(); it != V.end(); ++it)
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
typedef long long LL;

LL gcd(LL a, LL b) {
	if (b == 0) return a;
	return gcd(b, a%b);
}

const LL duzo = 100000000000000000;

const int MAXN = 100000;
LL dzielniki[MAXN];
LL elce[MAXN];

void testcase() {
	vector<LL> liczby;
	LL n, L, H;
	scanf("%lld%lld%lld", &n, &L, &H);
	LL xLcm = 0, xGCD = 0;
	REP(i,n) {
		LL v;
		scanf("%lld", &v);
		liczby.PB(v);
	}
	sort(liczby.begin(), liczby.end());

	FORE(it,liczby)
		if (*it != 1)
		xGCD = gcd(xGCD, *it);

	LL pierwszaNieJeden = 1;
	int index = -1;
	int gdziech = 0;
	FORE(it,liczby) if (*it > 1) {
		pierwszaNieJeden = *it;
		index = gdziech;
	} else ++gdziech;

	dzielniki[n] = 0;
	for (int i = n-1; i >= 0; --i)
		dzielniki[i] = gcd(liczby[i], dzielniki[i+1]);
	xLcm = 1;
	bool czy_sie_da = true;

	LL result = duzo;
	int gdzie = 0;
	FORE(it,liczby) {
		++gdzie;
		LL naszg = gcd(xLcm, *it);
		double potenc = (double)xLcm / (double)naszg * (double) (*it);
		if (potenc > 100000000000000000.0) {
			czy_sie_da = false;
			break;
		}
		xLcm /= naszg;
		xLcm *= (*it);
		elce[gdzie-1] = xLcm;

		if (dzielniki[gdzie]%xLcm != 0) continue;
		LL beg = 1, end = H;
		while (beg <= end) {
			LL sr = (beg+end)/2LL;
			double tmp = (double)sr * (double) xLcm;
			if ( tmp > 100000000000000000.0 ) {
				end = sr-1;
				continue;
			}
			LL wyn = sr * xLcm;
			if (wyn <= H && wyn >= L && dzielniki[gdzie]%wyn == 0) 
				result = min(result, wyn);
			if (wyn < L) beg = sr+1;
			else end = sr-1;
		}
	}
	
	// sprawdzic wszystkie dzielniki gcd

	LL pierw = (LL)(sqrt((double)xGCD));

	for(LL i = 1; i <= pierw+1; ++i) {
		if (xGCD % i == 0) {
			if (i <= H && i >= L)
				result = min(result, i);
			LL tmp = xGCD / i;
			if (tmp <= H && tmp >= L) {
				result = min(result, tmp);
			}
		}
	}



/*	int brut = -1;

	FOR(i,L,H) {
		bool ok = true;
		FORE(it,liczby)
			if (i % (*it) == 0 || (*it)%i == 0)
				continue;
			else ok = false;
		if (ok) { brut = i; break; }
	}

	printf("WYNIK BRUTA: %d\n", brut);*/
	if (result == duzo) {
		printf("NO\n");
	} else {
		printf("%lld\n", result);
	}

}

int main() {
	int t, v = 0;
	for (scanf("%d", &t); t--;) {
		printf("Case #%d: ", ++v);
		testcase();
	}
}
