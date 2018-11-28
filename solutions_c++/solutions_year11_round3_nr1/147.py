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

	int T, R, C, t_case=0;
	VS mm;
	string s;
	cin >> T;
	while (T--) {
		cout << "Case #" << ++t_case << ":" << endl;
		cin >> R >> C;
		REP(i, R) { cin >> s; mm.PB(s); }

		int imp = 0;
		REP(i, R) {
			REP(j, C) {
				if (mm[i][j] == '#') {
					if (j+1<C && mm[i][j+1] == '#' &&
							i+1<R && mm[i+1][j] == '#' &&
							i+1<R && j+1<C && mm[i+1][j+1] == '#') {
						mm[i][j] = '/'; mm[i][j+1] = '\\';
						mm[i+1][j] = '\\'; mm[i+1][j+1] = '/';
						i = -1;
						break;
					} else {
						imp = 1;
						break;
					}
				}
			}
			if (imp) break;
		}
		if (imp) {
			cout << "Impossible" << endl;
		} else {
			REP(i, R) cout << mm[i] << endl;
		}
		mm.clear();
	}
	return 0;
}

