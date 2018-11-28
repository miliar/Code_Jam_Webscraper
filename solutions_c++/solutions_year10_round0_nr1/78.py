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

typedef long long lint;

using namespace std;

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n, k;

		scanf("%d %d", &n, &k);
		k %= (1<<n);

		printf("Case #%d: %s\n", t+1, (k == ((1<<n)-1))  ? "ON" : "OFF");
	}

	return 0;
}
