#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int main() {

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T, n, S, p;
	int t[109];
	scanf("%d", &T);
	for( int cas = 1;cas <= T; ++cas) {
		scanf("%d%d%d", &n, &S, &p);
		int ret = 0;
		int tmp;
		for( int i = 0; i < n; ++ i) {
			scanf("%d", &tmp);
			if(tmp < p) continue;
			
			tmp -= p;
			int R = tmp & 1;
			tmp >>= 1;
			if(tmp >= p - 1) ++ ret;
			else {
				if((tmp == p - 2)&& S) {
					++ ret;
					-- S;
				}
			}
		}
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}
