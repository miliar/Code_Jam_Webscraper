#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T;
char N[25], N0[25];

int main() {
	scanf("%d", &T);
	for(int z=0; z<T; ++z) {
		scanf("%s", N);
		int k = strlen(N);
		for(int i=0; i<=k; ++i) N0[i] = N[i];
		next_permutation(N, N + k);
		bool ok = false;
		for(int i=0; i<k; ++ i) {
			if(N0[i] < N[i]) {
				printf("Case #%d: %s\n", z + 1, N);
				ok = true;
				break;
			}
			if(N0[i] > N[i]) {
				for(int j=k; j>=0; --j) N0[j + 1] = N0[j];
				N0[0] = '0';
				next_permutation(N0, N0 + k + 1);
				printf("Case #%d: %s\n", z + 1, N0);
				ok = true;
				break;
			}
		}
		if(!ok) {
			for(int j=k; j>=0; --j) N0[j + 1] = N0[j];
			N0[0] = '0';
			next_permutation(N0, N0 + k + 1);
			printf("Case #%d: %s\n", z + 1, N0);
		}
	}
	return 0;
}
