
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

vector<int> primes;
int pot10[10];

#define STALA 1000005
bool prime[STALA + 7];
void do_primes() {
	fup(i, 2, STALA) {
		if (prime[i]) continue;
		int act = 2 * i;
		while (act <= STALA) {
			prime[act] = 1;
			act += i;
		}
	}
	fup(i, 2, STALA) if (prime[i] == 0) primes.PB(i);
}

vector<lli> t;
lli pot(lli a, lli n, lli mod) {
	if (n == 0) return 1;
	if (n % 2) {
		return (a * (pot(a, n - 1, mod))) % mod;
	}
	else {
		lli x = pot(a, n / 2, mod);
		return (x * x) % mod;	
	}
}

int dupa = 0;
int kto = -1;


void check_val(int v) {
	if (kto == -1) {
		kto = v;
		return;
	} else {
		if (kto != v) { dupa = 1; }
	}
}

void checkX(lli X, lli p) {
	lli Y = t[1] - (X * t[0]) % p;
	Y = (Y + 2 * p) % p;
	lli last = -1;
	fup(i, 0, siz(t) - 2) {
		lli W = (t[i] * X + Y) % p;
		W = (W + 2 * p) % p;
		if (W != t[i + 1]) return ;
	}
	last = (t.back() * X + Y) % p;
	last = (last + 2 * p) % p;
	check_val(last);

}


void check(lli p) {
	if (dupa) return ;
	fup(i, 0, siz(t) - 1) {
		if (t[i] >= p) return ;
	}

	if (siz(t) == 2) {
		fup(X, 0, p - 1) {
			if (dupa) break;
			checkX(X, p);
		}		
		return ;
	}

	fup(i, 0, 0) {
		fup(j, 1, 1) {
			if (t[i] != t[j]) {
				lli a, b, c, d;
				a = t[i];
				b = t[i + 1];
				c = t[j];
				d = t[j + 1];
				lli zz = (a - b + p) % p;
				lli odw = pot(zz, p - 2, p);
				lli X = (((b - d + p) % p) * odw) % p;
				checkX(X, p);
				return ;
			}
		}
	}
	//TO SAMO 
	check_val(t[0]);
}

int main() {
	pot10[0] = 1;
	fup(i, 1, 8) pot10[i] = pot10[i - 1] * 10;
	do_primes();

	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		dupa = 0;
		kto = -1;
		int k, d;
		cin >> d >> k;
		t.clear();
		fup(i, 1, k) {
			int a; cin >> a;
			t.PB(a);
		}
		if (c == 17) {
//			cout << "CHUJ " << d << " " << k << endl;
//			debugv(t);		
		}
		if (k == 1) {
			printf("Case #%d: I don't know.\n", c);
			continue;
		} 
		FORE(it, primes) {
//			cout << "CHECK " << (*it) << endl;
			if (*it <= pot10[d]) {
				check(*it);
			} else break;
		}
		if (dupa) {
			printf("Case #%d: I don't know.\n", c);
		} else {

			printf("Case #%d: %d\n", c, kto);
		}




		
		
	}
	return 0;
}


