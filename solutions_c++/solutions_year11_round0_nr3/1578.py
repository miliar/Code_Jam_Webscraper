#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int T, N;
int arr[1111];

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.txt", "w", stdout);
	scanf("%d", &T);
	for(int s = 1; s <= T; ++s) {
		int ss = 0;
		long long ans = 0;
		scanf("%d", &N);
		for(int i = 0; i < N; ++i) {
			scanf("%d", &arr[i]);
			ss ^= arr[i];
			ans += arr[i];
		}
		if(ss != 0) ans = -1;
		else {
			sort(arr, arr + N);
			ans -= arr[0];
		}

		/*int ans = -1;
		for(int i = 0; i < (1<<N); ++i) {
			int s1 = 0, s2 = 0, s22 = 0;
			int add1 = 0, add2 = 0;
			for(int j = 0; j < N; ++j) {
				if(i & (1<<j)) {
					s1 += arr[j];
					++add1;
				} else {
					s2 ^= arr[j];
					s22 += arr[j];
					++add2;
				}
			}
			if(s1 == s2 && add1 > 0 && add2 > 0) {
				ans = max(ans, max(s1, s22));
			}
		}
		*/
		printf("Case #%d: ", s);
		if(ans == -1) puts("NO");
		else printf("%lld\n", ans);
	}
	return 0;
}