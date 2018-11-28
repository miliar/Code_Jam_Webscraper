/*
Compiled and Tested using Visual C++ 2008 Express Edition.
ONLINE_JUDGE is a macro for the Sphere Online Judge (SPOJ), where G++
compilers are used.
*/

#define _CRT_SECURE_NO_WARNINGS
//#define TEST

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<list>
#include<deque>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<time.h>
using namespace std;

#ifndef ONLINE_JUDGE
#include<hash_map>
using namespace stdext;
#else
#include<ext/hash_map>
using namespace __gnu_cxx;

namespace __gnu_cxx {
	template<> struct hash<string> {
		size_t operator()(const string& x) const {
			return hash<const char*>() (x.c_str());
		}
	};
}
#endif

int main(void) {
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
	int t, it, n, k, mask;
	scanf("%d", &t);
	for(it = 1; it <= t; it++) {
		scanf("%d %d", &n, &k);
		mask = (1 << n) - 1;
		if((mask & k) == mask)
			printf("Case #%d: ON\n", it);
		else
			printf("Case #%d: OFF\n", it);
	}
}
