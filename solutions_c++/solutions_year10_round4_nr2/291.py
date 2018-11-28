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

//hash_map<string, int> hm;

int prices[10000];
int misses[10000];
bool heap[10000];
long long memo[1030][12];

int p, teams;

long long solve(int base, int payed) {
	if(base >= teams)
		if(payed < p - misses[base - teams])
			return 1000000000000000LL;
		else
			return 0;
	if(memo[base][payed] >= 0)
		return memo[base][payed];
	long long res1 = solve(base + base, payed) + solve(base + base + 1, payed);
	long long res2 = solve(base + base, payed + 1) + solve(base + base + 1, payed + 1) + prices[base];
	return memo[base][payed] = min(res1, res2);
}

int main(void) {
#ifndef ONLINE_JUDGE
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	int tt, it, i, j;
	long long result;
	scanf("%d", &tt);
	for(it = 1; it <= tt; it++) {
		scanf("%d", &p);
		teams = 1 << p;
		for(i = 0; i < teams; i++)
			scanf("%d", &misses[i]);
		for(i = teams / 2; i > 0; i /= 2) {
			for(j = i; j < 2 * i; j++) {
				scanf("%d", &prices[j]);
				heap[j] = false;
			}
		}
		for(i = 0; i < 1030; i++)
			for(j = 0; j < 12; j++)
				memo[i][j] = -1;
		result = solve(1, 0);
		
		
		
		printf("Case #%d: %lld\n", it, result);
	}
}
