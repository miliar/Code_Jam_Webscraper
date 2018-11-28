/*
 * Template for code jam - different includes and templates
 * Real task code is in the end
 * Mikhail Dektyarow <mihail.dektyarow@gmail.com>, 2009
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
#include <string>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<class T1, class T2>inline istream& operator>> (istream& s, pair<T1, T2> &p) {	return s >> p.first >> p.second;}
template<class T1, class T2>inline ostream& operator<< (ostream& s, const pair<T1, T2>p) {	return s << "(" << p.first << " " << p.second << ")";}
template<class T1>inline ostream& operator<< (ostream& s, const vector<T1> container) {
	for (typename vector<T1>::const_iterator i = container.begin(); i != container.end(); i++) {
		s << *i << " ";
	}
	return s;
}
template<class T1>inline istream& operator>> (istream&s, vector<T1> &container) {
	for (typename vector<T1>::iterator i = container.begin(); i != container.end(); i++) {
		s >> *i;
	}
	return s;
}
typedef pair<int,int> ipair;
typedef long long int int64;
template<class T>T euclid(T a, T b, T &x, T &y) {
	if (b > a)
		swap(a, b);
	if (b == 0) {
		x = 1;
		y = 0;
		return a;
	}
	T x2 = 1, x1 = 0, y2 = 0, y1 = 1, q, r;
	while (b > 0) {
		q = a / b;
		r = a - q * b;
		x = x2 - q * x1;
		y = y2 - q * y1;
		a = b;
	   	b = r;
		x2 = x1; x1 = x;
	   	y2 = y1;
		y1 = y;
	}
	x = x2;
	y = y2;
	return a;
}
/*
 * Real code
 */

int main(void) {
	int T;
	cin >> T;
	REP(i, T) {
		char s[5000];
		char *sc;
		vector<int> dig(300, -1);
		//map<char, int> dig;
		cin >> s;
		sc=s;
		int k;
		k = 1;
		dig[sc[0]]=1;
		while(sc[1]==sc[0])sc++;
		sc++;
		dig[sc[0]]=0;
		sc++;
		k=2;
		REP(j, strlen(sc)) {
			if (dig[sc[j]] == -1) {
				dig[sc[j]] = k;
				k++;
			}
		}
		//cout << dig['0'] << " " << dig['1'] << "\n";
		unsigned long long int res;
		res = 0;
		REP(j, strlen(s)) {
			res *= k;//dig.size();
			res += dig[s[j]];
		}
		cout << "Case #" << i+1 << ": " << res << "\n";
	}
}
