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

#define M 100003


long long comb[510][510];
long long ways[510][510];

long long nWays(int n, int rank) {
	int i;
	long long result = 0;
	if(rank == 1)
		return 1;
	if(ways[n][rank] > 0)
		return ways[n][rank];
	for(i = 1; i < rank; i++) {
		result += nWays(rank, i) * comb[n - 1 - rank][rank - i - 1];
		result %= M;
	}
	ways[n][rank] = result;
	return result;
}


int main(void) {
#ifndef ONLINE_JUDGE
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
#endif
	int t, it, i, j, n;
	long long result;

	comb[0][0] = 1;
	for(i = 1; i <= 500; i++)
		comb[0][i] = 0;
	for(i = 1; i <= 500; i++) {
		comb[i][0] = 1;
		for(j = 1; j <= 500; j++)
			comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % M;
	}

	scanf("%d", &t);
	for(it = 1; it <= t; it++) {
		scanf("%d", &n);
		result = 0;
		for(i = 1; i < n; i++) {
			result += nWays(n, i);
			result %= M;
		}
		printf("Case #%d: %lld\n", it, result);
	}
}
