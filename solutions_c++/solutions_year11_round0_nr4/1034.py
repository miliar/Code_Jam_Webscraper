#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	
	int T, N;
	scanf("%d", &T);
	
	for(int ti=0; ti<T; ti++) {
		double res = 0.0;
		scanf("%d", &N);
		for(int i=0; i<N; i++) {
			int tmp;
			scanf("%d", &tmp);			
			if ((tmp-1)!=i)
				res += 1.0;
		}
				
		printf("Case #%d: %f\n", ti+1, res);
	}
	
	return 0;
}

