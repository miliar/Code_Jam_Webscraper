#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,n) FORD(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define SIZE(c) ((int)(c).size())
#define MP make_pair
#define FT first
#define SD second
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<double> VD;
typedef vector<LD> VLD;
typedef vector<LL> VLL;
typedef vector<bool> VB;
typedef istringstream ISS;
typedef ostringstream OSS;

template<class T>
class ARR2 {
	T *arr;
public:
	int n, m;
	ARR2(int n, int m) : n(n), m(m) {
		arr = new T[n * m];
	}
	ARR2(const ARR2<T>& a) : n(a.n), m(a.m) {
		arr = new T[n * m];
		REP(i,n * m)
			arr[i] = a.arr[i];
	}
	ARR2& operator=(ARR2& a) {
		if (&a != this)
			return *this;
		delete[] arr;
		n = a.n;
		m = a.m;
		arr = new T[n * m];
		REP(i,n * m)
			arr[i] = a.arr[i];
		return *this;
	}
	~ARR2() {
		delete[] arr;
	}
	T *operator[](int i) {
		return arr + i * m;
	}
};

class HK {
	ARR2<bool>& g;
	vector<int> match;
	stack<int> path;
	vector<bool> was1, was2;
public:
	HK(ARR2<bool>& g) : g(g), match(g.n, -1), path(), was1(), was2() {
		REP(j,g.m) {
			was1.clear();
			was1.resize(g.n);
			was2.clear();
			was2.resize(g.m);
			HK_rec(j);
			while (!path.empty()) {
				int i = path.top();
				path.pop();
				match[i] = path.top();
				path.pop();
			}
		}
	}
	bool HK_rec(int j) {
		was2[j] = 1;
		path.push(j);
		REP(i,g.n) if (!was1[i] && g[i][j] && match[i] != j) {
			was1[i] = 1;
			path.push(i);
			if (match[i] == -1 || !was2[match[i]] && HK_rec(match[i]))
				return 1;
			path.pop();
		}
		path.pop();
		return 0;
	}
	vector<int> operator()() const {
		return match;
	}
};

VS room;
int num[80][80];

int main() {
	int ccc;
	cin >> ccc;
	REP(cc,ccc) {
		int n, m;
		cin >> n >> m;
		room.clear();
		REP(i,n) {
			string line;
			cin >> line;
			room.PB(line);
		}
		int dim[2];
		dim[0] = dim[1] = 0;
		REP(i,n) REP(j,m) if (room[i][j] == '.')
			num[i][j] = (dim[j&1]++);
		ARR2<bool> g(dim[0],dim[1]);
		REP(i,dim[0]) REP(j,dim[1])
			g[i][j] = 0;
		REP(i,n) for (int j = 0; j < m; j += 2)
			if (room[i][j] == '.') {
				if (j > 0) {
					FOR(ii,i-1,i+2)
						if (ii >= 0 && ii < n && room[ii][j-1] == '.')
							g[num[i][j]][num[ii][j-1]] = 1;
				}
				if (j < m-1) {
					FOR(ii,i-1,i+2)
						if (ii >= 0 && ii < n && room[ii][j+1] == '.')
							g[num[i][j]][num[ii][j+1]] = 1;
				}
			}
		VI match = HK(g)();
		int res = 0;
		FORE(it,match)
			if (*it != -1)
				res++;
		cout << "Case #" << cc+1 << ": " << dim[0]+dim[1]-res << endl;
	}
}
