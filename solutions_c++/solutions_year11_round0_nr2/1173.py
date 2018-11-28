#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <limits>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#pragma comment(linker, "/STACK:64000000")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
template<typename T>
inline T SQR(T a) { return a * a; }
class __NT{};
template<class T, class U> struct __TL {
	typedef T __T; typedef U __U;
};
template<class, class, template<class, bool> class, bool> struct __IB;
template<class T, class U, class K, template<class, bool> class C, bool B>
struct __IB<T, __TL<U, K>, C, B> : public __IB<T, K, C, B>, public C<U, B> {
	typedef __TL<U, typename __IB<T, K, C, B> :: __RE> __RE;
};
template<class T, class U, template<class, bool> class C, bool B>
struct __IB <T, __TL<T, U>, C, B> : public __IB<T, U, C, B> {
	typedef typename __IB<T, U, C, B> :: __RE __RE;
};
template<class T, template<class, bool> class C, bool B>
struct __IB<T, __NT, C, B> : public C<T, B> {
	typedef __TL<T, __NT> __RE;
};
template<typename T, bool b>
struct __IP {
	operator T () const {
		return b ? (std::numeric_limits <T> :: has_infinity ? std::numeric_limits <T> :: infinity() : std::numeric_limits <T> :: max ()) : 
			(std::numeric_limits<T> :: lowest());
	}
};
#define _I(x,y) __IB<x,y,__IP,0>::__RE

template<bool B = true>
struct __IF : 
	public __IB<int, _I(ll, _I(double, _I(long double, _I(char, _I(unsigned char, _I(bool, _I(float, _I(ull, __NT)))))))), __IP, B> {
		__IF<!B> operator- () const {
			return __IF<!B>();
		}
};
__IF<> INF;
const double PI = 2 * asin (1.0);
#define MP make_pair
#define pb push_back
#define CLR(x) memset((x), 0, sizeof(x))
#define REP(i,n)for (int i = 0; i < (int)(n); ++i)
#define FOR(i,a,b)for (int i = a; i < (int)(b); ++i)
#define FORIT(it, x) for (auto it = (x).begin(); it != (x).end(); ++it)
#define ALL(x)(x).begin(),(x).end()
#define RALL(x)(x).rbegin(),(x).rend()
#define SZ(x) int((x).size())
#define EXIST(container, val) ((container).find ((val)) != (container).end ())
#define FAIL ++(*(int*)0)
#define file_name "filename"
void solve ();
int main (int argc, char *argv[]) {
#ifdef LOCAL
	clock_t st = clock ();
#endif
	ios::sync_with_stdio (false);
	solve ();
#ifdef LOCAL
	std::cerr << std::endl << "Solved in: " << fixed << setprecision (3) 
		<< (double) (clock () - st) / CLOCKS_PER_SEC << " s." << std::endl;
#endif
	return 0;
}
/////////////////////////////////////////////////////////////////////////////////////////////////
const double eps = 1e-6;
const int maxn = 1e6;
// Code here.

void solve () {
	// Code here.
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	string str, cur, text;
	FOR(ik, 0, T) {
		int n1, n2, n3, k, m;
		fin >> n1;
		map<char, vector<char> > MapOpp;
		map< pair<char, char>, char > MapConv;
		FOR(j, 0, n1) {
			fin >> cur;
			MapConv[MP(cur[0], cur[1])] = cur[2];
			MapConv[MP(cur[1], cur[0])] = cur[2];
		}
		fin >> n1;
		FOR(j, 0, n1) {
			fin >> cur;
			MapOpp[cur[0]].push_back(cur[1]);
			MapOpp[cur[1]].push_back(cur[0]);
		}
		multiset<char> used;
		fin >> n1 >> str;
		char last = -1;
		text = "";
		FOR(i, 0, SZ(str)) {
			char cur = str[i];
			if(EXIST(MapConv, MP(cur, last))) {
				used.erase(used.find(last));
				last = MapConv[MP(cur, last)];
				text.pop_back();
				text.push_back(last);
				continue;
			}
			//
			bool skip = false;
			for(auto it = MapOpp[cur].begin(); it != MapOpp[cur].end(); ++it) {
				if(EXIST(used, *it)) {
					used.clear();
					last = -1;
					skip = true;
					text.clear();
					break;
				}
			}
			if(skip)
				continue;
			last = cur;
			used.insert(cur);
			text += cur;
		}
		// comemnt.

		fout << "Case #" << ik + 1<< ": [";
		FOR(i, 0, SZ(text)) {
			fout << text[i];
			if(i != SZ(text) - 1) {
				fout << ", ";
			}
		}
		fout << "]\n";
	}
}
