#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
#include <cstdio>
using namespace std;
#define pb push_back
#define all(c) c.begin(), c.end()
typedef long long int64;

struct Point
{
	int x;
	int y;
	Point(int x_, int y_): x(x_), y(y_)
	{ }
};

template<class T> T sqr(const T& t) {return t * t;}
template<class T> T abs(const T& t) {return ((t > 0) ? (t) : (-t));}

class Fraction
{
public:
	long long p, q;
	Fraction(long long p_, long long q_): p(p_), q(q_)
	{ }
	Fraction operator- (const Fraction& f) const{
		return Fraction(p * f.q - q * f.p, q * f.q);
	}
};

void initialize()
{
    freopen("L.in", "r", stdin);
    freopen("_.out", "w", stdout);
}

int divv(int a, int b) {
	if (a % b == 0) return a / b;
	return (a / b) + 1;
}

Fraction diff(long long l, long long r, int mult, int t)
{
	// no:(t - 1) / l, 
	// yes: r / div(t / c)
	long long p1 = t - 1, q1 = l;
	long long p2 = r, q2 = t;
	return Fraction(p1, q1) - Fraction(p2, q2);
}

int solve(long long l, long long r, int mult) {
	if (l * mult >= r) return 0;
	int down = l, up = r;
	while (up - down > 1) {
		int sr = (down + up) / 2;
		Fraction val = diff(l, r, mult, sr);
		if (val.p < 0) {
			down = sr;
		}
		else {
			up = sr;
		}
	}
	if (diff(l, r, mult, down).p < 0)
		return solve(down, r, mult) + 1;
	else 
		return solve(l, down, mult) + 1;
}

int main()
{
    initialize();

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++tt) {
		int l, r, mult;
		cin >> l >> r >> mult;
		printf("Case #%d: %d\n", tt, solve(l, r, mult));
	}

    return 0;
}