#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define PI 2*acos(0)
#define EPS 1e-7
#define LL long long
#define INF 1000000000
#define PQ priority_queue

typedef pair<int, int> i2;
typedef pair<int, i2> i3;
typedef pair<i2, i2> i4;

set<i2> st;
int tc, A, B, ans, numdig;

int shift(int x, int _t) {
	int dig[100], sz = 0;
	
	while (x > 0) {
		dig[sz++] = x % 10;
		x /= 10;
	}
	
	reverse(dig, dig + _t);
	reverse(dig + _t, dig + sz);
	
	int res = 0;
	for (int i = 0; i < sz; i++) res = 10 * res + dig[i];
	
	return res;
}

int main() {

	//freopen("file.in", "r", stdin);

	scanf("%d", &tc);
	int t = 0;
	while (tc--) {
		scanf("%d %d", &A, &B);
		ans = 0;
		st.clear();
		for (int n = A; n < B; n++) {
			numdig = (int) floor(log10(n)) + 1;
			for (int j = 1; j < numdig; j++) {
				int tmp = shift(n, j);
				if (n < tmp && tmp <= B && !st.count(i2(n, tmp))) ans++, st.insert(i2(n, tmp));
			}
		}
		printf("Case #%d: %d\n", ++t, ans);
	}

	return 0;
}
