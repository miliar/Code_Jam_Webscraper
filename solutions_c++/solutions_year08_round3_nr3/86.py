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
// void hang() { while(true); }
static void crash() { *(int *)0 = 0; }
#define The_PI 3.14159265358979323846
#define max_macro(a,b)    (((a) > (b)) ? (a) : (b))
#define min_macro(a,b)    (((a) < (b)) ? (a) : (b))
#if 0
#define my_assert(t)		do {  } while(0)
#elif 0
void unexpected_func() {
	int answer = 42;
}
#define my_assert(t)		do { if(!(t)) unexpected_func(); } while(0)
#else
#define my_assert(t)		assert(t)
#endif

#define EPS_FOR_PRINT	1E-7
#define MAG 1000000007

typedef vector<unsigned> VU;

int main(void) {
	unsigned num_tests; cin >> num_tests;
	for(unsigned test_iter = 0; test_iter < num_tests; ++test_iter) {
		ULL n, m, x, y, z;
		cin >> n >> m >> x >> y >> z;
		VU aaa((size_t)m); unsigned * a = &aaa[0];
		VU bbb((size_t)n); unsigned * b = &bbb[0];
		for(unsigned j = 0; j < m; ++j) cin >> a[j];
		for(unsigned j = 0; j < n; ++j) {
			b[j] = a[j % m];
			a[j % m] = (x * a[j % m] + y * (j + 1)) % z;
		}
		VU ttt((size_t)n); unsigned * t = &ttt[0];
		unsigned s = 0;
		for(unsigned r = 0; r < n; ++r) {
			t[r] = 1;
			for(unsigned j = 0; j < r; ++j) {
				if(b[j] < b[r]) {
					t[r] += t[j];
					t[r] %= MAG;
				}
			}
			s += t[r];
			s %= MAG;
		}
		cout << "Case #" << (test_iter + 1) << ": " << s << endl;
	}
	return 0;
}
