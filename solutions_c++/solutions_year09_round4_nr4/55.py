
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
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; }
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
typedef complex<ld> P;
typedef  long long ulli;
#define maxn 102
#define eps 0.00000001
ld r[maxn];
P sr[maxn];
ulli n;
ld R;
const ld pi = M_PI;

P wczytaj() {
	ld x, y;
	cin >> x >> y;
	return P(x, y);
}

ld getPole(ld a, ld b, ld c) {
	ld p = (a + b + c) / 2;
	ld x = p * (p - a) * (p - b) * (p - c);
	if (x < 0) return -1;
	return sqrt(x);
}

P getSr(P p1, P p2, ld d, ld a, ld b) {
	ld ar = getPole(d, a, b);
	if (ar < -0.5) return P(0, 0);
	ld h = (2 * ar) / d;
	ld x = sqrt(SQR(a) - SQR(h));
	P wek = (p2 - p1);
	wek *= (1 / d);
	P pros = (wek * polar(1.0, -pi / 2));
	pros *= h;
	wek *= x;
	return p1 + pros + wek;
}	

P getO(P p1, ld r1, P p2, ld r2) {
	ld dis = abs(p1 - p2);		
	ld a = R - r1;
	ld b = R - r2;
	P o = getSr(p1, p2, dis, a, b);
	//if (real(o) < -1000) return o;
/*
	cout << "____________" << endl;
	cout << "GETO " << endl;
	cout << o << endl;
	debug(R);
	cout << r1 << " " << r2 << endl;
	cout << abs(o - p1) << endl;
	cout << abs(o - p2) << endl;
	assert(abs((abs(o - p1)  + r1) - R) <= 0.00001);
	assert(abs((abs(o - p2)  + r2) - R) <= 0.00001);

	cout << endl;
*/
	return o;
}

ulli getMask(P o) {
	ulli mask = 0;
	fup(i, 0, n - 1) {
		if (abs(o - sr[i]) + r[i] <= R + eps) mask += (1LL << (lli)(i));
	}
	return mask;
}

void wypisz(ulli a) {
	
	cout << "MAS " << endl;
	fup(i, 0, n - 1) cout << (bool)(a & (1LL << (lli)i));
	cout << endl;
}
bool moge(ld _R) {
	R = _R;
	ulli wyn = (1LL << (lli)n) - 1;
	vector<ulli> tos;
	fup(i, 0, n - 1) fup(j, 0, n - 1) {
		if (i == j) continue;
		P o = getO(sr[i], r[i], sr[j], r[j]);
		//cout << "P " << o << endl;
//		cout << i << " " << j << endl;
//		wypisz(getMask(o));
		tos.PB(getMask(o));
	}
	fup(i, 0, n - 1) {
		P o = sr[i];
		//cout << o << endl;
	//	wypisz(getMask(o));	
		tos.PB(getMask(o));
	}
	//cout <<" _____" << endl;
	//fup(i, 0, siz(tos) -1) wypisz(tos[i]);
	fup(i, 0, siz(tos) - 1) fup(j, 0, siz(tos) - 1) {
		ulli mask = tos[i] | tos[j];
		if (mask == wyn) return true;
	}
	return false;
}

int main(){
	int cas; 
	cin >> cas;
	fup(i, 1, cas) {
		cin >> n;
		fup(i, 0, n - 1) {
			sr[i] = wczytaj();
			cin >> r[i];
		}
		ld s, e;
		s = 0;
		e = 50000;
		fup(i, 1, 70) {
			ld q = (s + e) / 2;
			if (moge(q)) {
				e = q;
			} else s = q;
		}
		printf("Case #%d: %.8lf\n", i, (s + e) / 2);
	}

	return 0;	
}


