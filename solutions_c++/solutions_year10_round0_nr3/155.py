#include <cstdio>
#include <iostream>
#include <algorithm>

#define MAXN 1000

using namespace std;

typedef long long LL;

int nTC;
int nkali, n;
int eachGroup;
int A[MAXN + 2];
int next[MAXN + 2];
int cost[MAXN + 2];

int main () {
	scanf ("%d", &nTC);
	
	for (int tc = 1; tc <= nTC; tc++) {
		scanf ("%d%d%d", &nkali, &eachGroup, &n);
		
		for (int i = 0; i < n; i++) {
			scanf ("%d", &A[i]);
		}
		
		for (int i = 0; i < n; i++) {
			LL sum = 0, j;
			bool first = true;
			for (j = i; !(j == i && !first) && sum + A[j] <= eachGroup; j = (j + 1) % n) {
				sum = sum + (LL)A[j];
				first = false;
			}
			cost[i] = (int)sum;
			next[i] = j;
		}
		
		long long ret = 0;
		int cur = 0;
		for (int i = 0; i < nkali; i++) {
			ret = ret + (LL)cost[cur];
			cur = next[cur];
		}
		
		printf ("Case #%d: %lld\n", tc, ret);
	}
	
	return 0;
}
