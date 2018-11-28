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

int n;
vector<int> arr;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d", &n);
		arr.resize(n);
		for (int i = 0; i<n; i++) scanf("%d", &arr[i]);

		sort(arr.begin(), arr.end());

		int xor = 0;
		for (int i = 0; i<n; i++) xor ^= arr[i];
		int res = 0;
		for (int i = 1; i<n; i++) res += arr[i];

		printf("Case #%d: ", tt);
		if (xor == 0) printf("%d\n", res);
		else printf("NO\n");
		fflush(stdout);
	}
	return 0;
}
