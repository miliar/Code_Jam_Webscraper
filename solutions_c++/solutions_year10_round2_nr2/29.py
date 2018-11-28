#include <cstdio>
#include <string>
#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

const int N = 64;

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		int b, tm, x[N], v[N], n, K;
		scanf("%d %d %d %d", &n, &K, &b, &tm);
		for(int i = 0; i < n; i++) scanf("%d", &x[i]);
		for(int i = 0; i < n; i++) scanf("%d", &v[i]);
		int cnt = 0, useless = 0;
		int res = 0;
		for(int i = n-1; i >= 0; i--) {
			int useful = (x[i]+tm*v[i] >= b ? 1 : 0);
			if(useful && cnt < K) { res += useless; cnt++; }
			else useless++;
		}
		printf("Case #%d: ", t+1);
		if(cnt < K) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}

