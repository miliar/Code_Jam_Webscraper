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
#include<limits>

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
const LL oo =  numeric_limits<LL>::max();
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

struct pos {
	LL X,Y;
	double R;
};

vector<pos> input;
double get_radius(pos& p1, pos& p2) {
	return (sqrt((p1.X - p2.X)*(p1.X - p2.X) + (p1.Y - p2.Y)*(p1.Y - p2.Y)) + p1.R + p2.R) / 2.0;
}

double solve(int N) {
	if(N==1) return input[0].R;
	if(N==2) return max(input[0].R,input[1].R);
	double a,b,c;
	a = max(get_radius(input[0],input[1]),input[2].R);
	b = max(get_radius(input[1],input[2]),input[0].R);
	c = max(get_radius(input[0],input[2]),input[1].R);
	return min(min(a,b),c);
}

int main() {
	int C;
	cin>>C;
	FOR(c,1,C) {
		int N;
		cin>>N;
		input.resize(N);
		REP(n,N) {
			cin>>input[n].X>>input[n].Y>>input[n].R;
		}
		cout << "Case #" << c <<": " << fixed << setprecision(20) << solve(N) << endl;
	}
}
