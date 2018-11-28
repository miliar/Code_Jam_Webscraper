//: Piotr Skotnicki
// Google Code Jam 2011
// Round 1B
// A
#include <iostream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <iterator>
#include <bitset>
#include <sstream>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <ctime>

using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back

#define VAR(a,b) __typeof(b) a=(b)
#define ITER(it,a) __typeof((a).begin()) it=(a).begin(),it##_end=(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,a) for(ITER(it,a);it!=it##_end;++it)
#define FALL(i,a) for(int i=0,i##_size=(a).size();i<i##_size;++i)
#define RANGE(i,a,b,c) for(int i=(a);i<=(c);i+=(b))
#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define LEN(a) (sizeof(a)/sizeof(*(a)))
#define TAB(a) (a),(a)+LEN(a)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((b),(a),sizeof(a))
#define OUT(a) cout << a
#define OUTL(a) cout << a << endl
#define ABS(a) ((a)<0?-(a):(a))
#define MIN(a,b) ((a)<=(b)?(a):(b))
#define MAX(a,b) ((a)>=(b)?(a):(b))
#define LOG(a) (log(a)/log(2.0))
#define QSORT(a) random_shuffle(a);sort(a)
#define QSORTO(a,b) random_shuffle(a);sort(a,(b))
#define REVERSE(v) reverse(ALL(v))
#define UNIQUE(v) QSORT(ALL(v)),(v).resize(unique(ALL(v))-(v).begin())
#define NUM(v,a) (int)(lower_bound(ALL(v),(a))-(v).begin())
#define TWO(x) (1<<(x))
#define CONTAINS(a,v) ((a).find(v)!=(a).end())
#define HAS(a,v) (find(ALL(a),v)!=(a).end())

#define DEBUG 1
#define DB(a) if(DEBUG){cerr << __LINE__ << ": " << #a << " = " << a << endl;}
#define DBV(a) if(DEBUG){cerr << __LINE__ << ": " << #a << " = "; FOREACH(__i,a) cerr << *__i << " "; cerr << endl;}
#define DBT(a) if(DEBUG){cerr << __LINE__ << ": " << #a << " = "; REP(__i,LEN(a)) cerr << a[__i] << " "; cerr << endl;}
#define DBTN(a,n) if(DEBUG){cerr << __LINE__ << ": " << #a << " = "; REP(__i,n) cerr << a[__i] << " "; cerr << endl;}

template<class T> inline string str(const T& a) {ostringstream os("");os<<a;return os.str();}
int toInt(const string& s){int r;istringstream in(s);in>>r;return r;}

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<PI> VPI;
typedef vector<VPI> VVPI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef map<string,int> MSI;
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<LD,LD> PD;
typedef stringstream SS;

const int INF = 1000000000;
const LL INFLL = LL(INF) * LL(INF);
const double EPS = 1e-9;
inline bool is_zero(double v) { return (v > -EPS && v < EPS); }


void solve() {
	int n;
	cin >> n;
	string line;
	
	vector<double> wp(n);
	vector<double> owp(n);
	vector<double> oowp(n);

	VS score;

	REP(i,n) {
		cin >> line;
		score.PB(line);

		int played = 0;
		int wins = 0;
		int losses = 0;
		
		FALL(j,line) {
			char c = line[j];
			if(c == '.') {

			} else if(c == '1') {
				++played;
				++wins;
			} else {
				++played;
				++losses;
			}
		}
		wp[i] = (double(wins)/played);
	}

	//DBV(wp);

	REP(i,n) {
		VS c(score);

		double wp2 = 0.0f;
		int ile = 0;

		REP(g,n) if(g != i) {
			line = c[g];
			int played = 0;
			int wins = 0;
			int losses = 0;
			bool count = false;
			FALL(j,line) {
				char c = line[j];
				if(j != i) {
					if(c == '.') {

					} else if(c == '1') {
						++played;
						++wins;
					} else {
						++played;
						++losses;
					}
				} else {
					if(c != '.') {
						count = true;
					}
				}
			}
			if(count) {
				++ile;
				wp2 += (double(wins)/played);
			}
		}

		owp[i] = wp2 / ile;
	}

	//DBV(owp);

	REP(i,n) {
		int ile = 0;
		double wp3 = 0.0f;
		REP(j,n) if(i != j) {
			if(score[i][j] != '.') {
				wp3 += owp[j];
				++ile;
			}
		}
		oowp[i] = wp3 / ile;
	}

	//DBV(oowp);

	cout.precision(12);
	cout.setf(ios::fixed, ios::floatfield);
	cout << endl;
	REP(i,n) {
		cout << (0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		if(i < n - 1)
			cout << endl;
	}
}

int main(int argc, char* argv[]) {
    ios_base::sync_with_stdio(false);

#define TASK "A"

#define LARGE 1
#define SMALL 1
#define TEST 1

#if LARGE
    freopen(TASK"-large.in", "r", stdin);
    freopen(TASK"-large.out", "w", stdout);
#elif SMALL
    freopen(TASK"-small-attempt0.in", "r", stdin);
    freopen(TASK"-small-attempt0.out", "w", stdout);
#elif TEST
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int T;
    cin >> T;
    FOR(i, 1, T) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }

    fflush(stdout);
    return 0;
}
