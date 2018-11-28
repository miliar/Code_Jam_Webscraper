#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	int T, N, C;
	
	scanf("%d", &T);
				
	for(int ti=0; ti<T; ti++) {
		scanf("%d", &N);
		
		int totxor = 0;
		int minval = 1000000000;
		int sumval = 0;
		for(int i=0; i<N; i++) {
			scanf("%d", &C);
			totxor ^= C;
			if (C < minval)
				minval = C;
			sumval += C;
		}
															
		printf("Case #%d: ", ti+1);
		
		if (totxor == 0)
			printf("%d\n", sumval - minval);
		else
			printf("NO\n");
		
	}
	
	return 0;
}

