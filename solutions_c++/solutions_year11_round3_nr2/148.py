#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>

using namespace std;

// For vim: auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while

#define ALL(c) c.begin(), c.end()
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(int)(b); ++i)
#define FOREACH(X,C) for(typeof(C.begin()) X=C.begin();X!=C.end();++X)
#define PB push_back
#define SS stringstream
#define EPS (1e-9)
#define INF (1<<30)
#define SQR(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define EQUAL(a,b) (ABS((a)-(b))<eps)
#define px first
#define py second

#define S size()
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define FORX(i,a,b,x) for (int i=(a); i<=(int)(b); i+=x)
#define FORD(i,a,b) for (int i=a; i>=b; --i)

#define REV(c) reverse(c.begin(), c.end())
#define SORT(c) sort(c.begin(), c.end())

typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<string> VS; typedef vector<VS> VVS;
typedef signed long long LL; typedef unsigned long long ULL;
typedef pair<int,int> PII;

typedef map<int,int> MII;
typedef map<char, int> MCI;
typedef map<string, int> MSI;

LL tonum(string s){ stringstream in(s); LL x; in>>x; return x; }
string tostr(LL n){ stringstream in; in << n; string x; in>>x; return x; }
LL gcd(LL a, LL b) { while (1) { a=a%b; if(a==0) return b; b=b%a; if(b==0) return a; } }

/* end of pre-code */

LL T, N, L, t, C, t_case=0;
LL ret, K;
vector<LL> nn;
vector<LL> cc;

int main() {
	freopen ("input.txt", "rb", stdin);
	freopen ("output.txt", "w", stdout);

	cin >> T;
	while (T--) {
		cin >> L >> t >> N >> C;
		REP(i, C) { cin >> K; cc.PB(K); }
		while (1) {
			if (SZ(nn) >= N) break;
			REP(i, C) {
				nn.PB(cc[i]);
				if (SZ(nn) >= N) break;
			}
		}

		/* REP(i, N) cout << nn[i] << " "; cout << endl; */

		ret = 0;
		LL cr = 0;
		while (1) {
			/* ret += 2; */
			if (ret + 2*nn[cr] <= t) {
				ret += 2*nn[cr];
				nn[cr] = 0;
				cr++;
			} else break;
			if (cr >= N) break;
		}
		if (cr < N && ret < t) {
			nn[cr] -= (t-ret)/2;
			ret = t;
		}
		/* REP(i, N) cout << nn[i] << " "; cout << endl; */

		if (cr >= N) {
			cout << "Case #" << ++t_case << ": " << ret << endl;
			nn.clear(); cc.clear();
			continue;
		}
		SORT(nn); REV(nn);
		int ts = min(L, N);
		REP(i, ts) ret += nn[i];
		FOR(i, ts, N-1) ret += nn[i]*2;

		cout << "Case #" << ++t_case << ": " << ret << endl;
		nn.clear(); cc.clear();
	}

	return 0;
}

