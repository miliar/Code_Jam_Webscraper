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

LL L,D,N;
vector<string> pat;
vector<pair<int,string> > dict_input;

void parse(vector<string>& pp, const string& p) {
	bool in_p = false;
	string cur;
	string::const_iterator it = p.begin();
	while(it != p.end()) {
		if(*it == '(') {
			in_p = true;
		}
		else
		if(*it ==')') {
			in_p = false;
			pp.push_back(cur);
			cur.resize(0);
		}
		else {
			cur.push_back(*it);
			if(!in_p) {
				pp.push_back(cur);
				cur.resize(0);
			}
		}
		++it;
	}
}

bool pred(pair<int,string>& p) {
	return p.first == 1;
}

int main() {
	int T;
	cin>>T;
	FOR(t,1,T) {
		int N;
		cin>>N;
		double X=0, Y=0, Z=0, Vx=0, Vy=0, Vz=0;
		REP(n,N) {
			int x,y,z,vx,vy,vz;
			cin>>x>>y>>z>>vx>>vy>>vz;
			X += x;	
			Y += y;
			Z += z;
			Vx += vx;
			Vy += vy;
			Vz += vz;
		}
		double tmin;
		if((Vx*Vx + Vy*Vy+ Vz*Vz)<=eps) tmin = 0.0;
		else
			tmin = -(X*Vx + Y*Vy + Z*Vz)/(Vx*Vx + Vy*Vy+ Vz*Vz);
		if(tmin <= eps || -tmin >= eps) tmin = 0.0;
		double sol = ((X+tmin*Vx)*(X+tmin*Vx)+(Y+tmin*Vy)*(Y+tmin*Vy)+(Z+tmin*Vz)*(Z+tmin*Vz))/(N*N);
		sol = sqrt(sol);
		cout << "Case #" << t << ": "; 
		cout << fixed << setprecision(20) << sol << " "; 
		cout << fixed << setprecision(20) << tmin << endl;
	}
}
