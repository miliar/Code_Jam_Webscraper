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



//struct Freq {
//	unsigned idx;
//	unsigned cnt;
//};

int main(void) {
	unsigned nt; cin >> nt;
	for(unsigned j = 0; j < nt; ++j) {
		unsigned p, k, l;
		cin >> p >> k >> l;
		static unsigned freq[1000];
		memset(freq, 0, sizeof(unsigned) * 1000);
		for(unsigned q = 0; q < l; ++q) cin >> freq[q];
		sort(freq, freq + l);
		reverse(freq, freq + l);
		ULL c = 0;
		unsigned kp = 0;
		for(unsigned r = 0; r < l; ++r) {
			if(r % k == 0) {
				++kp;
			}
			c += kp*freq[r];
		}
		cout << "Case #" << (j + 1) << ": " << c << endl;
	}
	
	return 0;
}
