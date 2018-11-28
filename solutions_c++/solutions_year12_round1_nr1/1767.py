// created on: 2012-04-28
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
typedef vector<long long> VLL;
typedef signed long long LL; typedef unsigned long long ULL;
typedef pair<int,int> PII;

typedef map<int,int> MII;
typedef map<char,int> MCI;
typedef map<string,int> MSI;

LL tonum(string s){ stringstream in(s); LL x; in>>x; return x; }
string tostr(LL n){ stringstream in; in << n; string x; in>>x; return x; }
LL gcd(LL a, LL b) { while (1) { a=a%b; if(a==0) return b; b=b%a; if(b==0) return a; } }

/* end of pre-code */

double ee[111111], ff[111111], gg[111111];

int main() {
	freopen ("input.txt", "rb", stdin);
	freopen ("output.txt", "w", stdout);

	int T; cin >> T;
	int T_case = 0;
	int A, B;
	while (T--) {
		double ret = 99999999.0;
		cin >> A >> B;
		ff[0] = 1;
		ee[0] = 0;
		FORD(i, A, 1) {
			cin >> ee[i];
			ff[0] *= ee[i];
		}
		gg[0] = ff[0];

		FOR(i, 1, A) {
			ff[i] = ((ff[i-1] / (1-ee[i-1])) * (1-ee[i])) / ee[i];
			gg[i] = gg[i-1] + ff[i];
		}

		ret = min(ret, ff[0] * (B-A+1) + (1-ff[0]) * (2*B-A+2));
		ret = min(ret, B+2.0);

		FOR(i, 1, A) {
			ret = min(ret, (B-A+2*i+1) * (ff[0]+gg[i]-gg[0]) + (B-A+2*i+1+B+1) * (1-ff[0]-gg[i]+gg[0]));
		}
		printf("Case #%d: %.6lf\n", ++T_case, ret);
	}

	return 0;
}
