/*
 * C.cpp
 *
 *  Created on: May 7, 2011
 *      Author: loai
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
using namespace std;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int K;
	scanf("%d\n", &K);
	for (int test = 1; test <= K; test++) {
		int n;
		scanf("%d ", &n);
		int xorSum = 0, MIN = 1 << 28;
		int realSum = 0;
		REP(i,n) {
			int c;
			scanf("%d", &c);
			MIN = min(MIN, c);
			xorSum ^= c;
			realSum += c;
		}
		if (xorSum != 0) {
			printf("Case #%d: NO\n", test);
			continue;
		}
		printf("Case #%d: %d\n", test, realSum - MIN);
	}
}

