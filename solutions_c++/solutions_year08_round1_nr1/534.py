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

int main(void) {
	unsigned num_tests; cin >> num_tests;
	for(unsigned t_iter = 0; t_iter < num_tests; ++t_iter) {
		unsigned nn;
		cin >> nn;
		vector<SLL> v[2]; v[0].resize(nn); v[1].resize(nn);
		for(unsigned t = 0; t < 2; ++t) {
			for(unsigned j = 0; j < nn; ++j) {
				cin >> v[t][j];
			}
			sort(v[t].begin(), v[t].end());
		}
		reverse(v[0].begin(), v[0].end());
		SLL s = 0;
		for(unsigned j = 0; j < nn; ++j) {
			s += (v[0][j] * v[1][j]);
		}
		cout << "Case #" << (t_iter + 1) << ": " << s << endl;
	}
	return 0;
}
