#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x));
#define COPY(x, y) memcpy(x, y, sizeof(y));
#define SIZE(x) (int)x.size()
#define LEN(x) (int)x.length()

typedef long long int64;

int test, testq;

map <int, int> q;

set <int> q2;

int n;

void Solve() {
	int x;
	int a, b;
	int i;
	int ans;
	q.clear();
	q2.clear();
	scanf("%d", &n);
	fi(1, n) {
		scanf("%d %d", &a, &b);
		q[a] = b;
		if (b >= 2) {
			q2.insert(a);
		}
	}
	ans = 0;
	while (!q2.empty()) {
		ans++;
		x = *q2.begin();
		if (q[x] <= 3) {
			q2.erase(x);
		}
		if (q.find(x - 1) != q.end() && q[x - 1] == 1) {
			q2.insert(x - 1);
		}
		if (q.find(x + 1) != q.end() && q[x + 1] == 1) {
			q2.insert(x + 1);
		}
		q[x] -= 2;
		q[x - 1]++;
		q[x + 1]++;
	}
	printf("%d\n", ans);
	fflush(stdout);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%d: ", test);
		Solve();
	}
	return 0;
}
