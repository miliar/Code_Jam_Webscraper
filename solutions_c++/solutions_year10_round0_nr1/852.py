#include <cstdio>

int main(){
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++){
		int n, k;
		scanf("%d %d", &n, &k);
		int light = 1;
		for (int i = 0; i < n; i++)
			light <<= 1;
		light--;
		bool first = true;
		while (k > 0){
			if (!first) k--;
			else first = false;
			k -= light;
		}
		if (k == 0 && !first) printf("Case #%d: ON\n", test);
		else printf("Case #%d: OFF\n", test);
	}

	return 0;
}
