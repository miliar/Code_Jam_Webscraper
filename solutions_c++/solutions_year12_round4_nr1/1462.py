#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#pragma comment(linker, "/STACK:16000000")

typedef long long ll;
typedef pair<int, int> pii;

const int INF = 1e9;
const double EPS = 1e-8;
const double PI = 2 * acos(0.);
const int N = 10010;
const int M = (1 << 22) - 1;

int l[N], d[N];
pii Q[M];
int L[N], R[N];

bool solve() {
	int n;
	scanf("%d", &n);
	d[0] = l[0] = 0;
	L[0] = R[0] = 0;
	for (int i = 1; i <= n; ++i) {
		scanf("%d%d", &d[i], &l[i]);
		L[i] = R[i] = i;
	}
	int D;
	scanf("%d", &D);
	Q[0] = pii(0, 1);
	int lft = 0;
	int rght = 1;
	while (lft != rght) {
		
		int x = Q[lft].first;
		int y = Q[lft].second;

//		cerr << x << " " << y << endl;
		lft = (lft + 1) & M;


		if (x < y) {
			if (d[y] + min(l[y], abs(d[y] - d[x])) >= D)
				return 1;
   	
			while (R[y] + 1 <= n && abs(d[R[y] + 1] - d[y]) <= min(abs(d[y] - d[x]), l[y])) {
				Q[rght] = pii(y, R[y] + 1);
				rght = (rght + 1) & M;
				++R[y];
			}
		} else {	
	
			while (L[y] - 1 > 0 && abs(d[x] - d[L[y] - 1]) <= min(l[y], abs(d[y] - d[x]))) {
				Q[rght] = pii(y, L[y] - 1);
				rght = (rght + 1) & M;
				--L[y];
			}
		}
	
	}

	return 0;
}

int main() {
#ifdef _DBG1
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		printf("Case #%d: ", i + 1);
		printf(solve() ? "YES\n" : "NO\n");
	}
	return 0;
}