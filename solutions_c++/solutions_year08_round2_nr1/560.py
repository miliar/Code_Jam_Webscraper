#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <limits>
#include <fstream>
using namespace std;

typedef long long i64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

//#define _CRT_SECURE_NO_WARNINGS
#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define REPD(i,n) for (int i((n)-1); i >= 0; --i)
#define FILL(a,c) memset(&a, c, sizeof(a))
#define MP(x,y) make_pair((x), (y))
#define ALL(v) (v).begin(), (v).end()
#define _B begin()
#define _E end()
#define NUM(T) numeric_limits<T>()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

ifstream fin("A.in");
ofstream fout2("A.out");

int main() {
	int C_TEST = 0;
	fin >> C_TEST;
	FOR(test, 1, C_TEST) {
		long long n, A, B, C, D, x0, y0, M;
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long X = x0, Y = y0;
		ofstream fout1("A1.out");
		fout1 << X << ' ' << Y << endl;
		FOR(i, 1, n-1) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			fout1 << X << ' ' << Y << endl;
		}
		fout1.close();
		ifstream ffin("A1.out");
		set< pii > c;
		REP(i,n) {
			int x, y;
			ffin >> x >> y;
			c.insert(MP(x,y));
		}
		vector<pii> v;
		v.insert(v.end(),c.begin(),c.end());
		
		int ans = 0;
		FOR(i, 0, n-3)
			FOR(j, i+1, n-2)
				FOR(k, j+1, n-1) {
					int ix = (v[i].first + v[j].first + v[k].first);
					int iy = (v[i].second + v[j].second + v[k].second);
					if (!(ix%3) && !(iy%3))
						ans++;
				}
		fout2 << "Case #" << test << ": ";
		fout2 << ans;
		(test==C_TEST) ?
			fout2 << "" :
			fout2 << endl;
	}
	return 0;
}