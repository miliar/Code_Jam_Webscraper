#pragma comment(linker, "/STACK:20000000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

int64 l;
int n;
int arr[128];
int mx;

int res[110000];

vector<int> curr, next;

void DFS(int u) {
	for (int i = 0; i<n; i++) {
		int nu = u + arr[i];
		if (nu < mx) continue;
		nu -= mx;

		if (res[nu] < 1000000000) continue;
		res[nu] = res[u];
		curr.push_back(nu);
		DFS(nu);
	}
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%I64d", &l);
		scanf("%d", &n);
		for (int i = 0; i<n; i++) scanf("%d", arr+i);
		std::sort(arr, arr+n);
		std::reverse(arr, arr+n);

		mx = arr[0];
		int64 x0 = int64(l) / int64(mx);
		int mod = int64(l) - int64(x0) * int64(mx);

		curr.clear();
		memset(res, 63, sizeof(res));

		res[0] = 0;
		curr.push_back(0);
		DFS(0);
		while (!curr.empty()) {
			for (int j = 0; j<curr.size(); j++) DFS(curr[j]);

			next.clear();
			for (int j = 0; j<curr.size(); j++) {
				int u = curr[j];
//				printf("%d ", u);
				for (int i = 0; i<n; i++) {
					int nu = u + arr[i];
					if (nu >= mx) continue;
		
			        if (res[nu] < 1000000000) continue;
			        res[nu] = res[u] + 1;
			        next.push_back(nu);
				}
			}
//			printf("\n");
			std::swap(curr, next);
		}

		printf("Case #%d: ", tt);
		if (res[mod] > 1000000000) printf("IMPOSSIBLE\n");
		else printf("%I64d\n", x0 + res[mod]);
		fflush(stdout);
	}
	return 0;
}
 