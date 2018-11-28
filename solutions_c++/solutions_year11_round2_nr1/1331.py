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

VS mm;
string s;

int main() {
	freopen ("input.txt", "rb", stdin);
	freopen ("output.txt", "w", stdout);

	int T, N, t_case=0;
	cin >> T;
	while (T--) {
		printf("Case #%d:\n", ++t_case);
		cin >> N;
		REP(i, N) {
			cin >> s;
			mm.PB(s);
		}
		vector<double> wp(N), owp(N), oowp(N), _win(N), _play(N);
		// WP
		REP(i, N) {
			REP(j, N) {
				if (mm[i][j] == '.') continue;
				_play[i]++;
				_win[i] += mm[i][j] == '1';
			}
			wp[i] = _win[i] / _play[i];
		}
		// OWP
		REP(i, N) {
			double _sum = 0;
			double _cnt = 0;
			REP(j, N) {
				if (mm[i][j] == '.') continue;
				_sum += (_play[j]<=1||_win[j]-(mm[j][i]=='0')<0)?0:(_win[j]-(mm[j][i]=='1'))/(_play[j]-1);
				_cnt += 1;
			}
			owp[i] = _sum / _cnt;
		}
		// OOWP
		REP(i, N) {
			double _sum = 0;
			double _cnt = 0;
			REP(j, N) {
				if (mm[i][j] == '.') continue;
				_sum += owp[j];
				_cnt++;
			}
			oowp[i] = _sum / _cnt;
		}
		REP(i, N) {
			double rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			printf("%.12lf\n", rpi);
		}
		wp.clear(); owp.clear(); oowp.clear(); _win.clear(); _play.clear(); mm.clear();
	}
	return 0;
}

