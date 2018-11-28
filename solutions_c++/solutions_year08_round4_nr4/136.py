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

static char ainp[50010], aperm[50010];
static unsigned k;

#define max_macro(a,b)    (((a) > (b)) ? (a) : (b))
#define min_macro(a,b)    (((a) < (b)) ? (a) : (b))

int main(void) {
	unsigned CC; scanf(" %u", &CC);
	static unsigned pv[20]; 
	for(unsigned it = 1; it <= CC; ++it) {
		scanf(" %u %s", &k, &ainp);
		for(unsigned j = 0; j < k; ++j) pv[j] = j;
		unsigned len = (unsigned)strlen(ainp);
		unsigned r = len/k;
		unsigned cprsize = UINT_MAX;
		do {
			// Fill Block
			for(unsigned u = 0; u < len; u += k) {
				for(unsigned j = 0; j < k; ++j) {
					aperm[u + j] = ainp[u + pv[j]];
				}
			}
			unsigned sum = 1;
			for(unsigned j = 1; j < len; ++j) {
				if(aperm[j] != aperm[j - 1]) ++sum;
			}
			cprsize = min_macro(cprsize, sum);
		} while(next_permutation(pv, pv + k));
		printf("Case #%d: %d\n", it, cprsize);
	}
	return 0;
}
