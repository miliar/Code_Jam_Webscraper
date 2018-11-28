#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

int main() {
	int T; 
	scanf("%d", &T);
	for (int i = 0; i < T; i ++) {
		int N, K, ans = 0;
		char hoge[256];
		scanf("%d %d", &N, &K);
		itoa(K, hoge, 2);
		int len = strlen(hoge);
		if (len >= N) {	
			int f = 1;
			for (int j = 0; j < N; j ++) {
				if (hoge[(len-1) - j] == '0') {
					f = 0; break;
				}
			}
			if (f) ans = 1;
		};

		printf("Case #%d: %s\n", i+1, ans?"ON":"OFF");
//		printf("[%s]", hoge);
	}

	return 0;
}