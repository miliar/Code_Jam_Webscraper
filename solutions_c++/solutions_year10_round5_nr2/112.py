
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

#define STALA 1000000

int ile[STALA + 5];
void dodaj(int v) {
	fup(i, 0, STALA + 4 - v) {
		ile[i + v] = min(ile[i + v], ile[i] + 1);	
	}
}
int main() {
	int cas;
	cin >> cas;
	lli L;
	fup(c, 1, cas) {
		int n;
		cin >> L;
		cin >> n;
		fup(i, 0, STALA) ile[i] = inf;
		ile[0] = 0;
		vector<int> moz;
		fup(i, 1, n) {
			int a;
			cin >> a;
			dodaj(a);
			moz.PB(a);
		}
		lli mini = -1;

		FORE(it, moz) {
			lli v = *it;
			lli res = L % v;
			lli x = L / v;
			while (res < STALA) {
				lli cost = ile[res] + x;	
				if (ile[res] < inf) {
					if (mini == -1) mini = cost;
					if (cost < mini) mini = cost;
				}
				--x;
				res += v;
			}
		}
		if (mini == -1) {
			printf("Case #%d: IMPOSSIBLE\n", c);
		} else 
		printf("Case #%d: %lld\n", c, mini);
	}
	return 0;
}


