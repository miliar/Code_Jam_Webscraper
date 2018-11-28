#include<iostream>

using namespace std;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t, cas = 0, n, k;
	cin >> t;
	while(t --) {
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", ++ cas);
		if(k % (1 << n) == (1 << n) - 1) puts("ON");
		else puts("OFF");
	}
	return 0;
}
