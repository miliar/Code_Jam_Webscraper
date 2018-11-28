#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int N = 1010;
int a[N];

void solve() {
	int n, s, p;
	scanf("%d%d%d", &n, &s, &p);
	for (int i = 0; i < n; ++i) {
		scanf("%d", a + i);
	}
	sort(a, a + n);
	reverse(a, a + n);
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		int t;

		if (a[i] % 3 == 0) t = a[i] / 3;
		else if (a[i] % 3 == 1) t = a[i] / 3 + 1;
		else if (a[i] % 3 == 2) t = a[i] / 3 + 1;
		if (t >= p) {
			ans++;
			continue;
		}

		if (s == 0) continue;

		if (a[i] == 0) t = 0;
		else if (a[i] == 1) t = 1;
		else if (a[i] % 3 == 0) t = a[i] / 3 + 1;
		else if (a[i] % 3 == 1) t = a[i] / 3 + 1;
		else if (a[i] % 3 == 2) t = a[i] / 3 + 2;
		if (t >= p) {
			ans++;
			s--;
		}
	}
	printf("%d\n", ans);
}

int main() {
//	freopen("in","r",stdin);
//	freopen("in.txt","r",stdin);
//	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
