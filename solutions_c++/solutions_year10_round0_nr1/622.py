#include <stdio.h>

bool calc(int n, int k){
	int m = (1 << n);
	k %= m;
	return(k == m - 1);
}


int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	int n, k;

	scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		scanf("%d%d", &n, &k);

		bool res = calc(n, k);
		printf("Case #%d: %s\n", i, res ? "ON" : "OFF");
	}

	return 0;
}