
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
#define DEBU false
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
#define MAXN 1005

int kiedy[MAXN];
lli kasa[MAXN];
int roz[MAXN];
int R, k, n;

pair<lli, lli> jazda(int p) {
	//cout << "JAZDA " << p << endl;
	lli sum = 0;
	int nowy = p;
	fup(i, 1, n) {
		int next = (p + i - 1) % n;
		if (sum + roz[next] > k) {
			nowy = next;
			break;
		}
	//	cout << i << " " << roz[next] << endl;
		sum += roz[next];
	}
	return MP(sum, nowy);
}

int main() {
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		cin >> R >> k >> n;		
		fup(i, 0, n - 1) cin >> roz[i];
		fup(i, 0, n - 1) kiedy[i] = -1;
		kiedy[0] = 0;
		kasa[0] = 0;
		int Cstart = -1, Cdl;
		lli Ckasa;
		int act = 0;
	//	cout << "CAS $$$$$$$$$$$$$$$$$$$$$$$$ " << c << endl;
		debug(R);
		debug(k);
		debug(n);
		fup(ride, 1, R) {
			pair<lli, lli> nowa = jazda(act);
		//	cout << "Ride: " << ride << " " << nowa.first << " " << nowa.second << endl;
			kasa[ride] = kasa[ride - 1] + nowa.FI;

			if (kiedy[nowa.SE] != -1) {
				Cstart = kiedy[nowa.SE];
				act = nowa.SE;
				Cdl = ride - Cstart;
				Ckasa = kasa[ride] - kasa[Cstart];
				break;
			} 
			kiedy[nowa.SE] = ride;
			act = nowa.SE;
		}
		debug(Cstart);
		debug(Cdl);
		debug(Ckasa);
		lli wyn = 0;
		if (Cstart == -1) {
			wyn = kasa[R];
		} else {
			lli z = (R - Cstart) / Cdl;
			while (Cstart + z * Cdl - 1 > R) --z;
			debug(z);
			wyn = kasa[Cstart] + z * Ckasa;
			lli x = Cstart + z * Cdl;
			debug(x);
			while (x < R) {
				pair<lli, lli> nowa = jazda(act);
				wyn += nowa.FI;
				act = nowa.SE;
				++x;
			}
		}
		cout << "Case #" << c << ": " << wyn << endl;

	}

	return 0;
}


