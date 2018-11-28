#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#define MAX 110

int n, end;

bool solve(){
	bool res;
	return (end & ((1 << n) - 1) % (1 << n)) == ((1 << n) - 1);
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, cases;
	scanf("%d", &cases);
	for (t = 1; t <= cases; t++){
		bool res;
		scanf("%d %d", &n, &end);
		res = solve();
		printf("Case #%d: ", t);
		if (res) printf("ON\n");
		else printf("OFF\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}