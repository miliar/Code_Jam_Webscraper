#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int t, n, k;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>t;
	for(int i=1; i<=t; ++i) {
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", i, (k % (1<<n) == ((1<<n)-1) ? "ON" : "OFF"));
	}
	return 0;
}