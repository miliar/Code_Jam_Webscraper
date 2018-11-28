#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = int(1e4 + 5);

int d[N], l[N], n, D, rest[N];

bool dfs(int v) {
	if (d[v] + rest[v] >= D) 
		return true;

	for (int i = v + 1; i < n; i++) {
		if (d[i] > d[v] + rest[v]) break;
		if (rest[i] < min(d[i] - d[v], l[i])) {
			rest[i] = min(d[i] - d[v], l[i]);
			if (dfs(i))
				return true;
		}
	}			

	return false;
}

int main() {
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d", &n);

		for (int j = 0; j < n; j++) 
			scanf("%d%d", d + j, l + j);
		scanf("%d", &D);

		memset(rest, 0, sizeof(rest));
		rest[0] = d[0];

		printf("Case #%d: ", i + 1);

		if (dfs(0))
			puts("YES");			
		else
			puts("NO");
	}

	return 0;
}
