#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> pi;
typedef pair<pi, int> ppi;
typedef unsigned long long ull;

#define x first
#define y second
#define mp make_pair



void solution() {
	int n, s, p;
	scanf("%d%d%d", &n, &s, &p);
	int a[200] = {0};

	int res[2][31];
	for (int i = 0; i < 2; ++i) {
		for (int j = 0; j < 31; ++j) {
			res[i][j] = -1;
		}
	}

	for (int i = 0; i <= 10; ++i) {
		for (int j = i; j <= 10; ++j) {
			for (int k = j; k <= 10; ++k) {
				if (k - i > 2) {
					continue;
				}
				int surp = k - i == 2;
				int sum = i + j + k;
				res[surp][sum] = max(res[surp][sum], k);
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		scanf("%d\n", &a[i]);
	}
	sort(a, a + n, greater<int>());
	int r = 0;
	for (int i = 0; i < n; ++i) {
		int v = res[0][a[i]];
		if (v >= p) {
			++r;
		} else {
			if (s && res[1][a[i]] >= p) {
				--s;
				++r;
			}
		}		
	}
	printf("%d\n", r);
}

int main() {

	//freopen("in.in", "rt", stdin);
	//freopen("out.out", "wt", stdout);

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	/*freopen("B-small.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);*/

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);
	
	int t = 0;
	scanf("%d\n", &t);
	for (int tt = 0; tt < t; tt++) {
		printf("Case #%d: ", tt + 1);
		solution();
	}

	return 0;
}