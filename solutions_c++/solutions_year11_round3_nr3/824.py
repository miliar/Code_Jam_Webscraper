#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <string>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
	int nc, ci;
	static long long a[20000];
	
	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		long long N, L, H, i;
		scanf("%lld %lld %lld", &N, &L, &H);
		for (i = 0; i < N; i++) scanf("%lld", &a[i]);

		long long ans = 0;
		for (ans = L; ans <= H; ans++) {
			bool done = true;
			for (i = 0; i < N; i++)
				if (a[i] % ans != 0 && ans % a[i] != 0) {
					done = false;
					break;
				}
			if (done) break;
		}		
		
		if (ans > H)
			printf("Case #%d: NO\n", ci);
		else
			printf("Case #%d: %lld\n", ci, ans);
	}
	
	return 0;
}
