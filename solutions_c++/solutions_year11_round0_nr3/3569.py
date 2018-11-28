#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
 
using namespace std;

__int64 inf = 1LL << 30;
int used[1005];
vector<int> vi;
int n;



int main() {
	int T;
	freopen("c:\\C-large.in", "r", stdin);
	freopen("c:\\C-large.out", "w", stdout);
	scanf("%d", &T);

	for (int testCase = 1; testCase <= T; ++testCase) {
		
		scanf("%d", &n);

		vi = vector<int>();

		int xor = 0;
		__int64 sum= 0;
		for (int i = 0; i < n; ++i) {
			int d;
			scanf("%d", &d);
			vi.push_back(d);
			xor ^= d;
			sum += d;
		}

		if (xor != 0) {
			printf("Case #%d: NO\n", testCase); 
		} else {
			int res = -1;
			sort(vi.begin(), vi.end());


			printf("Case #%d: %lld\n", testCase, sum - vi[0]); 
		}

	}

	return 0;
}