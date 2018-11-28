#include <cstdio>

using namespace std;

int T, N;
int A[1001], B[1001];

int main() {
	scanf("%d", &T);
	for(int i=0; i<T; i++) {		
		scanf("%d", &N);		
		for(int j=0; j<N; j++)
			scanf("%d%d", &A[j], &B[j]);
		int y = 0;
		
		for(int j=0; j<(N-1); j++)
			for(int k=j+1; k<N; k++) {
				if ( ((A[j]>A[k]) && (B[j]<B[k])) || 
					((A[j]<A[k]) && (B[j]>B[k]))) {
					y++;											
				}
			}
			
		printf("Case #%d: %d\n", (i+1), y);
	}
	return 0;
}
