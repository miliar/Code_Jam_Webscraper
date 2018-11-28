#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <climits>
#include <sstream>
#include <cstring>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <cmath>
#include <map>
#include <set>

#define INF (INT_MAX/3)
#define MAXS 1000010

typedef long long lint;

using namespace std;

int leftof[MAXS+16];

int canwin(int a, int b)
{
	if (a == 0 || b == 0)
		return 1;
	if (a < b)
		swap(a, b);
	return b < leftof[a];
}

int calc_it(int a, int b)
{
	int result = 0;

	if (b == 0)
		return 1;

	int mid = (a-b)/b;
			
	for (int k = mid-1; k <= mid+1; k++) {
		if (k <= 0)
			continue;

		if (b-a*k > 0) {
			int v1 = a, v2 = b-a*k;
			if (v1 < v2)
				swap(v1, v2);
			if (v1 < a && !canwin(v1, v2))
				result = 1;
		}
		if (a-b*k > 0) {
			int v1 = b, v2 = a-b*k;
			if (v1 < v2)
				swap(v1, v2);
			if (v1 < a && !canwin(v1, v2))
				result = 1;
		}
	}

	return result;
}

int main(int argc, char ** argv)
{
	leftof[0] = 0;

	for (int a = 1; a <= MAXS; a++) {
		int left = 0, right = a;

		while (left < right) {
			int m = (left+right)/2;

			if (calc_it(a, m))
				left = m+1;
			else
				right = m;
		}

		leftof[a] = left;
	}

	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int a1, a2, b1, b2;

		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
		
		lint ret = 0;

		for (int a = a1; a <= a2; a++) {
			int left = b1;
			int right = min(a-1, min(b2, leftof[a]-1));
			int len = (right-left+1);
			lint len2 = max((lint)len, 0LL);
			ret += len2;
		}
		swap(a1, b1);
		swap(a2, b2);
		for (int a = a1; a <= a2; a++) {
			int left = b1;
			int right = min(a-1, min(b2, leftof[a]-1));
			int len = (right-left+1);
			lint len2 = max((lint)len, 0LL);
			ret += len2;
		}

		for (int i = 1; i <= MAXS; i++)
			if (a1 <= i && i <= a2 && b1 <= i && i <= b2 && canwin(i, i))
				ret ++;

		printf("Case #%d: %lld\n", t+1, ret);
	}

	return 0;
}
