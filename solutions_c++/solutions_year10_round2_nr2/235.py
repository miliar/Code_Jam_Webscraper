#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)

typedef pair<int,int> PII;
typedef long long ll;

ll cx[100], cv[100], cmi[100];

void Run(int testcase) {
	printf("Case #%d: ", testcase);

	ll N, K, B, T;
	scanf(" %lld %lld %lld %lld", &N, &K, &B, &T);

	FOR (i, 0, N)
		scanf(" %lld", &cx[i]);
	FOR (i, 0, N)
		scanf(" %lld", &cv[i]);

	int canmakeit = 0;
	FOR (i, 0, N)
		if (T*cv[i] >= B-cx[i]) {
			canmakeit++;
			cmi[i] = 1;
		}
		else
			cmi[i] = 0;

	if (canmakeit < K) {
		printf("IMPOSSIBLE\n");
		return;
	}

	// iterate through the end

	ll swaps = 0, saved = 0;

	for (ll i = N-1; i >= 0 && saved < K; i--) {
		if (cmi[i])
			saved++;
		else
			swaps += K-saved;
	}

	printf("%d\n", swaps);
}

int main()
{
	int T;
	scanf(" %d", &T);
	FOR (i, 0, T)
		Run(i+1);

	return 0;
}
