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

int main() {
	freopen ("input.txt", "rb", stdin);
	freopen ("output.txt", "w", stdout);

	int T, N, P;
	string R;
	int O_pos, B_pos;
	int t_case = 0;
	VI rr, bb, nn;
	cin >> T;
	while (T--) {
		cin >> N;
		rr.clear(); bb.clear(); nn.clear();
		O_pos = 1; B_pos = 1;
		int ret = 0;
		REP(i, N) {
			cin >> R >> P;
			if (R == "O") { rr.PB(P); nn.PB(0); }
			if (R == "B") { bb.PB(P); nn.PB(1); }
		}
		int r = 0, b = 0, t;
		REP(i, N) {
			if (nn[i] == 0) {
				t = abs(O_pos-rr[r]) + 1;
				ret += t;
				if (abs(B_pos-bb[b]) <= t) B_pos = bb[b];
				else if (B_pos < bb[b]) B_pos += t;
				else B_pos -= t;
				O_pos = rr[r];
				r++;
			}
			if (nn[i] == 1) {
				t = abs(B_pos-bb[b]) + 1;
				ret += t;
				if (abs(O_pos-rr[r]) <= t) O_pos = rr[r];
				else if (O_pos < rr[r]) O_pos += t;
				else O_pos -= t;
				B_pos = bb[b];
				b++;
			}
		}
		cout << "Case #" << ++t_case << ": " << ret << endl;
	}
	return 0;
}

