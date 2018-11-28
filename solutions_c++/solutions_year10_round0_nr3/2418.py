#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <sstream>
using namespace std;

#define fo(i,n) for(int i=0; i<n; i++)
#define foo(i,j,n) for(int i=j; i<n; i++)

int g[1010];
int main() {
#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int T, n, k, r;
	scanf("%d", &T);

	foo(t,1,T+1) {
		printf("Case #%d: ", t);
		scanf("%d%d%d", &r, &k, &n);
		fo(i,n)
			scanf("%d", g + i);

		long long res = 0;
		int start = 0, rr = r, i = 0;
		while (rr--) {
			long long cursum=0;
			for(int i=0; i<n && cursum<k; i++) {
				res += g[start % n];
				cursum +=g[start % n];

				if(cursum>k){
					res -= g[start %n];
					cursum -= g[start %n];
					break;
				}
				start++;
			}
		}
		printf("%lld\n", res);
	}
	return 0;
}
