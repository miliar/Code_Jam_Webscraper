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

int g[1010];
long long bucksAfterRound[1010]; // for the first rounds
int lastRoundStartingWithGroup[1010];

int main(void) {
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
	int t, it, r, k, n, i, round, next, last;
	long long load, p, totalBucks;
	scanf("%d", &t);
	for(it = 1; it <= t; it++) {
		scanf("%d %d %d", &r, &k, &n);
		bucksAfterRound[0] = p = 0;
		for(i = 0; i < n; i++) {
			scanf("%d", &g[i]);
			p += g[i];
			lastRoundStartingWithGroup[i] = -1;
		}
		if(p <= k) {
			printf("Case #%d: %lld\n", it, p * r);
			continue;
		}
		round = 1;
		next = 0;
		while(round <= r) {
			if(lastRoundStartingWithGroup[next] > 0)
				break;
			last = next;
			load = g[last];
			while(load <= k) {
				last++;
				if(last >= n)
					last = 0;
				load += g[last];
			}
			load -= g[last];
			bucksAfterRound[round] = bucksAfterRound[round - 1] + load;
			lastRoundStartingWithGroup[next] = round;
			next = last;
			if(next < 0)
				next = n - 1;
			round++;
		}
		if(round > r) {
			printf("Case #%d: %lld\n", it, bucksAfterRound[r]);
			continue;
		}
		int cycleStart = lastRoundStartingWithGroup[next];
		int cycleSize = round - cycleStart;
		int nCycles = (r - round + 1) / cycleSize;
		long long cycleBucks = bucksAfterRound[round - 1] - bucksAfterRound[cycleStart - 1];
		cycleBucks *= nCycles;
		totalBucks = bucksAfterRound[round - 1] + cycleBucks;
		round += nCycles * cycleSize;
		while(round <= r) { // if it works, don't change it...
			last = next;
			load = g[last];
			while(load <= k) {
				last++;
				if(last >= n)
					last = 0;
				load += g[last];
			}
			load -= g[last];
			totalBucks += load;
			next = last;
			if(next < 0)
				next = n - 1;
			round++;
		}
		printf("Case #%d: %lld\n", it, totalBucks);
	}
}
