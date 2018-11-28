#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int t, n , c[1000];
	scanf("%d", &t);
	
	for (int test = 1; test <= t; test++) {
		printf("Case #%d: ", test);
		
		int hasSolution = 0;
		
		scanf("%d", &n);
		
		for (int i = 0; i < n; i++) {
			scanf("%d", &c[i]);
			hasSolution ^= c[i];
		}
		
		if (hasSolution) {
			printf("NO");
		} else {
			sort(c, c + n);
			
			int sol = 0;
			
			for (int i = 1; i < n; i++) {
				sol += c[i];
			}
			
			printf("%d", sol);
		}
		
		printf("\n");
	}
	return 0;
}

