
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

const int base = (1 << 23);
const int STALA = base / 2;

struct ltree {
	int t[2 * base + 1];
	void clear() {
		CLR(t);
	}
	void add(int x, int y) {
	//	cout << "ADD " << x << " " << y << endl;
		x += base;
		while (x) {
			t[x] += y;
			x >>= 1;
		}
	}
	int get_val(int x) {
		return t[x + base];
	}

	int get_kth(int k) {
		int act = 1;
		while (act < base) {
			if (t[act * 2] >= k) {
				act = act * 2;
			} else {
				k -= t[act * 2];
				act = act * 2 + 1;
			}
		}
		return act - base;
	}

	int get_rank(int x) {
		x += base;
		int sum = 0;
		sum += t[x];
		while (x) {
			if (x & 1) {
				sum += t[x - 1];
			}	
			x >>= 1;
		}
		return sum;
	}
};

ltree tree;

void prepare() {
	tree.clear();
	fup(i, 0, base - 1) tree.add(i, 1);
}

lli binom(lli n) {
	return (n*(n - 1)) / 2;
}
lli get_cost(lli l, lli r, lli pos) {
	lli step = (r - l - 1);
	lli start = (r - l + 1);
	lli c1, c2;
	lli d1 = pos - l;
	lli d2 = r - pos;
	c1 = start + step * d1 - binom(d1) * 2;
	c2 = start + step * d2 - binom(d2) * 2;
	return max(c1, c2);
}

int get_zero(int l, int r, int pos) {
	int z = pos - l;
	return r - z;
}

int dodaj_p(int pos) {
	//cout << "ADD " << pos << endl;
	int val = tree.get_val(pos);
	//debug(val);
	if (val == 1) {
		tree.add(pos, -1);
		return 0;
	} else {
		int left, right;
		int rank = tree.get_rank(pos);
		left = tree.get_kth(rank) + 1;
		right = tree.get_kth(rank + 1) - 1;

	//	debug(left);
	//	debug(right);
		int zero = get_zero(left, right, pos);
		tree.add(zero, 1);

		tree.add(left - 1, -1);
		tree.add(right + 1, -1);
		return get_cost(left, right, pos);
	}
}

int main() {
	int a, b, c;
	//cin >> a >> b >> c;
	//cout << get_cost(a, b, c) << endl;
	//return 0;
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		prepare();
		int p;
		cin >> p;
		lli sum = 0;

		fup(i, 1, p) {
			int pos, ile;
			cin >> pos >> ile;
			pos += STALA;
			fup(j, 1, ile) sum += dodaj_p(pos);
		}
		printf("Case #%d: %lld\n", c, sum);
//		cout << sum << endl;
	}
	return 0;
}


