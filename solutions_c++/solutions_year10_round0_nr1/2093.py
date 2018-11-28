#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tc, it = 0;
	cin >> tc;
	while(tc --> 0) {
		int n, k;
		cin >> n >> k;
		k = k % (1 << n);
		printf("Case #%d: %s\n", ++it, (k == (1 << n) - 1) ? "ON" : "OFF");
	}
	return 0;
}