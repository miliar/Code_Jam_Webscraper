#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <string.h>
using namespace std;

int C[1005];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int testCase;
	scanf("%d", &testCase);
	for(int tc = 1; tc <= testCase; ++tc){
		int n, xorSum = 0, sum = 0, minC = 0x7fffffff;
		cin >> n;
		for(int i = 0; i < n; ++i){
			scanf("%d", &C[i]);
			xorSum ^= C[i];
			sum += C[i];
			if(minC > C[i]){
				minC = C[i];
			}
		}
		if(xorSum){
			printf("Case #%d: NO\n", tc);
			continue;
		}
		printf("Case #%d: %d\n", tc, sum - minC);
	}
	return 0;
}
