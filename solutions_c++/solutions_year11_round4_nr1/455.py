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
typedef pair<double,double> PDD;

double X, S, R, t, N;

bool cmp(PDD a, PDD b) {
	return a.py < b.py;
}

int main() {
	freopen ("input.txt", "rb", stdin);
	freopen ("output.txt", "w", stdout);

	int T, t_case=0;
	cin >> T;
	vector<double> B, E, W;
	while (T--) {
		double ret = 0;
		cin >> X >> S >> R >> t >> N;
		B.clear(); E.clear(); W.clear();

		REP(i, N) {
			double bt, et, wt;
			cin >> bt >> et >> wt;
			B.PB(bt); E.PB(et); W.PB(wt);
		}
		double sul = 0;
		double cur = 0;
		REP(i, N) {
			sul += B[i] - cur;
			cur = E[i];
		}
		sul += X - cur;
		if (sul >= R*t) {
			sul -= R*t;
			ret += t;
			t = 0;
			ret += sul / S;
			sul = 0;
		} else {
			t -= sul / R;
			ret += sul / R;
			sul = 0;
		}
		vector<PDD> rat;
		REP(i, N) {
			rat.PB(PDD(E[i]-B[i], W[i]));
		}
		sort(ALL(rat), cmp);
		REP(i, N) {
			double t1 = (rat[i].px / (R+rat[i].py));
			if (t1 >= t) {
				rat[i].px -= (R+rat[i].py)*t;
				ret += t;
				t = 0;
				break;
			} else {
				rat[i].px = 0;
				ret += t1;
				t -= t1;
			}
		}
		REP(i, N) {
			if (rat[i].px == 0) continue;
			ret += rat[i].px / (S+rat[i].py);
		}
		printf("Case #%d: %.9lf\n", ++t_case, ret);
	}
	return 0;
}

