#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "A"

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	int64 two[3] = {1, 2, 4};
	int64 five[3] = {1, 5, 25};

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);

		int64 n, pd, pg;
		scanf("%I64d %I64d %I64d", &n, &pd, &pg);

		int64 pd2 = (pd % 2 == 0) + (pd % 4 == 0);
		int64 pd5 = (pd % 5 == 0) + (pd % 25 == 0);

		int64 pg2 = (pg % 2 == 0) + (pg % 4 == 0);
		int64 pg5 = (pg % 5 == 0) + (pg % 25 == 0);

        int64 minD = two[2 - pd2] * five[2 - pd5];
        int64 minG = two[2 - pg2] * five[2 - pg5];

        if (minD > n || pd != 0 && pg == 0 || pd != 100 && pg == 100) {
        	printf("Broken");
        }
        else {
        	printf("Possible");
        }

		printf("\n");
	}

	return 0;
}
