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

int tmap[101][101][3];
char cmap[101][101];
vector<pair<int,int> > loc;
LL T,H,W;

// N,W,E,S
int dr[4][2] = { {-1,0},{0,-1},{0,1},{1,0} };

bool valid(int h,int w) {
	return h>=1 && h <=H && w>=1 && w <=W;
}

void mark() {
	FOR(h,1,H) {
		FOR(w,1,W) {
			int _min = tmap[h][w][0]; 
			for(int i=0;i<4;i++) {
				int th = h + dr[i][0];
				int tw = w + dr[i][1];
				if(valid(th,tw) && _min > tmap[th][tw][0]) {
					tmap[h][w][1] = tmap[th][tw][1];
					_min = tmap[th][tw][0];
				}
			}
		}
	}
}

void solve() {
	FOR(h,1,H) FOR(w,1,W) {
		int nh,nw;
		nh = h;
		nw = w;
		while(tmap[nh][nw][1] != tmap[nh][nw][2]) {
			tmap[h][w][1] = tmap[nh][nw][1];
			int lb = tmap[nh][nw][1];
			nh = loc[lb].first;
			nw = loc[lb].second;
		}
	}
}

int main() {
	cin>>T;
	FOR(t,1,T) {
		cin>>H>>W;
		int label = 0;
		loc.resize(H*W+1);
		FOR(h,1,H) {
			FOR(w,1,W) {
				cin>>tmap[h][w][0];
				tmap[h][w][1] = tmap[h][w][2] = label;
				loc[label] = make_pair(h,w);
				label++;
			}
		}
		cout << "Case #"<< t << ": " <<endl;
		mark();
		solve();

		char lab='a';
		map<int,char> mapa;
		FOR(h,1,H) {
			FOR(w,1,W) {
				if(mapa.find(tmap[h][w][1]) == mapa.end()) {
					mapa[tmap[h][w][1]] = lab++;
				}
				cmap[h][w] = mapa[tmap[h][w][1]];
			}
		}
		/*
		FOR(h,1,H) {
			FOR(w,1,W) {
				cout << tmap[h][w][1] << " ";
			}
			cout << endl;
		}
		*/

		FOR(h,1,H) {
			FOR(w,1,W) {
				cout << cmap[h][w] << " ";
			}
			cout << endl;
		}
	}
}
