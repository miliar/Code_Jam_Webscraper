
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

#define maxn 50

int pos[maxn];
int v[maxn];

int main() {
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		int n, k , b, t;
		cin >> n >> k >> b >> t;
		fup(i, 1, n) cin >> pos[i];
		fup(i, 1, n) cin >> v[i];
		int sum = 0;
		int ah = 0;
		int jest = 0;
		fdo(i, n, 1) {
			if (jest >= k) break;
			if (v[i] * t >= (b - pos[i])) {
				sum += ah;
				jest++;	
			} else {
				ah++;
			}
		}
		if (jest >= k) {
			printf("Case #%d: %d\n", c, sum);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", c);

		}
		
	}
	return 0;
}


