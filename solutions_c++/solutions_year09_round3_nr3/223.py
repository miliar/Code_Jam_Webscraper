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
	int N;
	cin >> N;
	REP(i, N) {
		int P, Q;
		cin >> P >> Q;
		vector<int> num(Q);
		cin >> num;
		REP(j, num.size())
			num[j]--;
		sort(num.begin(), num.end());
		int min_cost;
		min_cost = 99999999;
		do {
			vector<int> pris(P, 1);
			int ccost;
			ccost = 0;
			REP(j, num.size()) {
				pris[num[j]] = 0;
				for (int k=num[j]-1; k >= 0; k--) {
					if (pris[k])
						ccost++;
					else
						break;
				}
				for (int k=num[j]+1; k < pris.size(); k++) {
					if (pris[k])
						ccost++;
					else
						break;
				}
			}
			remin(min_cost, ccost);
		}
		while (next_permutation(num.begin(), num.end()));
		cout << "Case #" << i+1 << ": " << min_cost << "\n";
	}
}
