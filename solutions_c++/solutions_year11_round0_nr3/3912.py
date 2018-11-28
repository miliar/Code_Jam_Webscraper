#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	
	int t, n, mini, x, sum, a;
	
	scanf("%d", &t);
	
	for (int j = 1; j <= t; j++) {
		
		mini = 9999999;
		x = sum = 0;
		
		scanf("%d", &n);
		
		for (int i = 0; i < n; i++) {
			
			scanf("%d", &a);
			x ^= a;
			sum += a;
			mini = min(a, mini);
		}
		
		printf("Case #%d: ", j);
		
		if (x)
			printf("NO\n");
		else
			printf("%d\n", sum - mini);
	}
	
	return 0;
	
}
