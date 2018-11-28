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
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

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

struct st
{
	int c, prev, pos;
public:
	st(int _c, int _p, int _pos) { c=_c;  prev = _p; pos = _pos;}
};

bool operator<(const st &a, const st &b) {
	if (a.c != b.c) return a.c > b.c;
	if (a.pos != b.pos) return a.pos < b.pos;
	if (a.prev != b.prev) return a.prev > b.prev;
	return false;
}

int main() {
	freopen("C:\\Projects\\GCJ\\input", "rt", stdin);
	freopen("C:\\Projects\\GCJ\\output.txt", "wt", stdout);

	int c;
	cin >> c;
	
	long long res[10000] = {0};
	res[2] = 0;
	res[3] = 1;
	for (int i=4;i<9000;i++) {
		int temp = i;	
		res[i] = 1 + res[(temp)/2 + 1];
	}
	for (int z=0;z<c;z++)
	{
		long long l,p,fact;
		cin >> l >> p >> fact;

		long long count = 2;
		while ((p + fact - 1)/fact > l) {
			count++;
			l *= fact;
		}

		cout << "Case #" << (z+1) << ": " << res[count] << endl;
	}

	exit(0);
}
