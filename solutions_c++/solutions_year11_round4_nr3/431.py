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

VI pr;
char sv[1000001];

int main() {
	freopen ("input.txt", "rb", stdin);
	freopen ("output.txt", "w", stdout);

	int t_case = 0;
	int rt = 1000000;
	FOR(i, 2, rt) {
		if (sv[i]) continue;
		pr.PB(i);
		FORX(j, i, rt, i) sv[j] = 1;
	}

	int T;
	LL N, ret;
	cin >> T;
	while (T--) {
		cin >> N;
		ret = 0;
		LL mn = 0;
		LL mx = 0;
		REP(i, SZ(pr)) {
			if (N < pr[i]) break;
			LL N2 = N;
			int cnt = 0;
			while (N2 >= pr[i]) {
				cnt++;
				N2 /= pr[i];
			}
			/* cout << pr[i] << " " << cnt << endl; */
			mn += 1;
			mx += cnt;
		}
		if (N == 1) mn = 1;
		mx += 1;
		ret = mx - mn;
		printf("Case #%d: %lld\n", ++t_case, ret);
	}

	return 0;
}

