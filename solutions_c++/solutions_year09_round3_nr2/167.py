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
		double x, y, z, dx, dy, dz, cx, cy, cz, cdx, cdy, cdz;
		x = y = z = dx = dy = dz = 0;
		int N;
		cin >> N;
		REP(j, N) {
			cin >> cx >> cy >> cz >> cdx >> cdy >> cdz;
			x += cx;
			y += cy;
			z += cz;
			dx += cdx;
			dy += cdy;
			dz += cdz;
		}
		x /= (double)N;
		y /= (double)N;
		z /= (double)N;
		//cout << x << " " << y << " " << z << "\n";
		dx /= (double)N;
		dy /= (double)N;
		dz /= (double)N;
		double t;
		if ((dx*dx + dy*dy + dz*dz) < 1e-8) { t = 0;} else
			t = -(x*dx+y*dy+z*dz) / (dx*dx + dy*dy + dz*dz);
		if (t < 0) t = 0;
		cout << "Case #" << i+1 << ": ";
		printf("%.8lf %.8lf\n",sqrt((x+t*dx)*(x+t*dx)+(y+t*dy)*(y+t*dy)+(z+t*dz)*(z+t*dz)), t);// << "\n";
	}
}
