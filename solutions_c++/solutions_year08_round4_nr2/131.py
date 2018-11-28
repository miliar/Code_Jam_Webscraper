#define _CRT_SECURE_NO_WARNINGS 1
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <string>
#include <bitset>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <assert.h>
#include <sstream>
#include <limits>
#include <list>
#include <stdlib.h>
using namespace std;
typedef unsigned long long ULL;
typedef signed long long SLL;
typedef unsigned short ushort;
typedef signed char schar;
typedef unsigned char uchar;

#define max_macro(a,b)    (((a) > (b)) ? (a) : (b))
#define min_macro(a,b)    (((a) < (b)) ? (a) : (b))

static unsigned n, m, a;
static unsigned lim;

// p <= n, q <= m
bool does_factor(unsigned v, unsigned& p, unsigned& q) {
	unsigned t;
	for(t = lim; t > 0; --t) {
		if(v % t == 0) break;
	}
	if(t > 0 && v / t <= n) {
		p = v / t;
		q = t;
		return true;
	}
	return false;
}

// Triangle area
int main(void) {
	unsigned CC; cin >> CC;
	for(unsigned j = 1; j <= CC; ++j) {
		cin >> n >> m >> a;
		bool swapped = false;
		if(n < m) {
			swap(n, m);
			swapped = true;
		}
		unsigned x2, y2, x3, y3;
		bool impossible = false;
		if(n * m < a) {
			impossible = true;
		} else {
			lim = (unsigned)sqrt((double)(a + 1)) + 1;
			lim = min_macro(lim, m);
			unsigned t;
			for(t = lim; t > 0; --t) {
				if(a % t == 0) break;
			}
			if(t > 0 && a / t <= n) {
				x2 = a / t; y2 = 0;
				x3 = x2; y3 = t;
			} else {
				// Brute force
				for(x2 = 1; x2 <= n; ++x2) {
					for(y3 = (a + x2 - 1)/x2; y3 <= m; ++y3) {
						unsigned v = x2*y3 - a;
						if(does_factor(v, x3, y2)) {
							goto herre;
						}
					}
				}
				impossible = true;
			}
herre:;
		}

		if(swapped) {
			swap(x2, y2);
			swap(x3, y3);
		}

		if(impossible) {
			cout << "Case #" << j << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << j << ": 0 0 " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
		}
	}
	return 0;
}
