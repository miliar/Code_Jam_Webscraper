#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

using namespace std;

typedef long long lint;

double solve(int wrong)
{
	if (wrong <= 1)
		return 0.0;
	return 1.0*wrong;
}

int main()
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n, diff = 0;

		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			int v;
			scanf("%d", &v);
			if (v != i+1)
				diff ++;
		}

		printf("Case #%d: %.6f\n", t+1, solve(diff));
	}

	return 0;
}
