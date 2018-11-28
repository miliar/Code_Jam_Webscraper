//: Piotr Skotnicki
// Google Code Jam 2011
// Qualification Round
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
	int N, P;
    char R;
    int ile = 0;
	cin >> N;

    int posB = 1;
    int posO = 1;
    int revposB = 1;
    int revposO = 1;

    REP(i,N) {
		cin >> R >> P;

        if(R == 'O') {
            if(posO < P) {
                while(posO < P) {
                    ++posO;
                    ++posB;
                    --revposB;
                    ++ile;
                }
            } else {
                while(revposO > P) {
                    --revposO;
                    ++posB;
                    --revposB;
                    ++ile;
                }
            }
            posO = P;
            revposO = P;
            ++posB;
            --revposB;
            ++ile;
        } else {
            if(posB < P) {
                while(posB < P) {
                    ++posB;
                    ++posO;
                    --revposO;
                    ++ile;
                }
            } else {
                while(revposB > P) {
                    --revposB;
                    ++posO;
                    --revposO;
                    ++ile;
                }
            }
            posB = P;
            revposB = P;
            ++posO;
            --revposO;
            ++ile;
        }
	}
    
	cout << ile;
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
	freopen(TASK"-small-attempt1.in", "r", stdin);
	freopen(TASK"-small-attempt1.out", "w", stdout);
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
