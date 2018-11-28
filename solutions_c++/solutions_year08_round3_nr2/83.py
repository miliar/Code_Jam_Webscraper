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

inline bool isUgly(ULL q) {
	return
		q % 2 == 0
		|| q % 3 == 0
		|| q % 5 == 0
		|| q % 7 == 0
		;
}

char a[42]; int v[42];
unsigned n;
ULL num_uglies;

void get_num_uglies(unsigned idx, ULL factor, SLL last_num) {
	SLL new_num = ((SLL)(v[idx] * factor)) + last_num;
	if(idx > 0) {
		// +
		get_num_uglies(idx - 1, 1, new_num);
		// -
		get_num_uglies(idx - 1, 1, -new_num);
		// no op
		get_num_uglies(idx - 1, factor * 10, new_num);
	} else if(isUgly(new_num >= 0 ? new_num : -new_num)) {
		// cout << ">>>>" << new_num << endl;
		++num_uglies;
	}
}

int main(void) {
	unsigned num_tests; cin >> num_tests;
	for(unsigned test_iter = 0; test_iter < num_tests; ++test_iter) {
		cin >> a;
		n = (unsigned)strlen(a);
		for(unsigned j = 0; j < n; ++j) v[j] = a[j] - '0';
		if(n == 1) {
			num_uglies = isUgly((ULL)v[0]) ? 1 : 0;
		} else {
			num_uglies = 0;
			get_num_uglies(n - 1, 1, 0);
		}
		cout << "Case #" << (test_iter + 1) << ": " << num_uglies << endl;
	}
	return 0;
}
