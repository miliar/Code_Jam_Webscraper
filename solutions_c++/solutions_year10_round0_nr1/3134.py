#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int n, k;
		scanf("%d %d", &n, &k);		
		printf("Case #%d: %s\n", t + 1, (( (k | ((1 << n) - 1)) == k ) ? "ON" : "OFF"));
	}
}

