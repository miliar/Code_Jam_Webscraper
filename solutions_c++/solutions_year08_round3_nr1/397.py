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

ifstream fin("in.txt");
ofstream fout("out.txt");

int main() {
	int C_TEST = 0;
	fin >> C_TEST;
	FOR(test, 1, C_TEST) {
		int P, K, L;
		fin >> P >> K >> L;
		vector<i64> f(L);
		REP(i,L)
			fin >> f[i];
		sort(f._B,f._E,greater<i64>());
		int count = 0;
		i64 sum = 0;
		FOR(i,1,P) {
			FOR(j,1,K) {
				if (count>=L)
					break;
				sum += f[count]*i;
				count++;
			}
			if (count>=L)
				break;
		}
		fout << "Case #" << test << ": ";
		(test==C_TEST) ?
			fout << sum :
			fout << sum << endl;
	}
	return 0;
}