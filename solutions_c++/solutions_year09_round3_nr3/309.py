#include<iostream>
#include<iomanip>
#include<iterator>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<complex>
#include<bitset>
#include<cstdio>
#include<cassert>
#include<cmath>
#include<ctime>
#include<sys/time.h>
#include<stdexcept>

using namespace std;

template<class T> inline int SIZE(const T& c) {return c.size();}
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORB(i,a,b) for(int i=(a),_b=(b)-1;i<=_b;i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define REP(i,n) FORB(i,0,(n))
#define FORA(i,c) REP(i,SIZE(c))

#define _it(c) __typeof((c).begin())
#define FORE(e,c) for(_it(c) e=(c).begin();e!=(c).end();e++)

#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define ALL(x) (x).begin(),(x).end()
#define CLEAR(x,c) memset(x,c,sizeof(x)) 
#define DUMP(x) FORE(__it,x) cout << *__it << ' ';cout<<endl
#define DUMPP(x) FORE(__it,x) cout << "(" << __it->X << ", " << __it->Y << ")" << ' ';cout<<endl
#define SORT(x) sort(ALL(x))
#define SIZEA(x) sizeof(x)/sizeof(*(x))

#define pi acos(-1.)
#define eps 1e-7
#define inf 1e17
#define maxn 100
#define maxp 1100000

typedef long long LL;
const LL oo = LONG_LONG_MAX;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<double> VD;
typedef vector<vector<double> > VVD;
typedef pair<int, int> PI;

template<typename T> inline T max(T x, T y, T z) {return std::max(x,std::max(y,z));}
template<typename T> inline T min(T x, T y, T z) {return std::min(x,std::min(y,z));}
template<typename T> inline void check_max(T& x,const T& y) {x = max(x,y);}
template<typename T> inline void check_min(T& x,const T& y) {x = min(x,y);}

template<typename T> inline void s2v(string s,T& x) {istringstream(s)>>x;}
template<typename T> inline string v2s(const T& x) {ostringstream os;os<<x;return os.str();}


template<typename T>
class __mapa {
	map<T,int> m;
	vector<T> v;
public:
	int size() const {return m.size();}
	int operator()(const T& s) {
		if(m.insert(make_pair(s,m.size())).second) v.push_back(s);
		return m[s];
	}
	const T& operator()(const int ix) const {
		if(ix<0||ix>=size()) throw std::out_of_range(string("__mapa::()(int)"));
		return v[ix];
	}
};

// modulo arithmetic
template<typename T> T gcd(T a, T b) {return b?gcd(b,a%b):a;}
template<typename T> T lcm(T a, T b) {return a*b/gcd(a,b);} // possible overflow
LL pmod(LL x, LL p, LL m) {
	if(p==0) return 1;
	if(p==1) return x%m;
	if(p%2) return (x%m)*pmod(x,p-1,m) % m;
	else {
		LL y = pmod(x,p/2,m);
		return y*y % m;
	}
}


LL solve(LL P, LL Q, vector<LL>& l) {
	sort(ALL(l));
	LL _min_gold_count = oo;
	do {
		LL gold_count = 0;
		vector<LL> cells(P,1);
		REP(k,l.size()) {
			LL pos = l[k]-1;
			LL tp = pos+1;
			while(tp<P && cells[tp] == 1) {
				gold_count++;
				tp++;
			}
			tp = pos-1;
			while(tp>=0 && cells[tp] == 1) {
				gold_count++;
				tp--;
			}
			cells[pos]=0;
		}
		_min_gold_count = min(_min_gold_count,gold_count);
	} while(next_permutation(ALL(l)));
	return _min_gold_count;
}

int main() {
	int T;
	cin>>T;
	FOR(t,1,T) {
		LL P,Q;
		cin>>P>>Q;
		vector<LL> l(Q);
		REP(q,Q) cin>>l[q];
		cout << "Case #" << t << ": " << solve(P,Q,l) << endl;;
	}
}
