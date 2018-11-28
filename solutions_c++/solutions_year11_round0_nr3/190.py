#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>

using namespace std;

int main() {
	int T, N, X, tmp, m, sum;
	
	scanf("%d", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d ", &N);
		
		X = 0;
		m = 1000000;
		sum = 0;
		
		for(int i = 0; i < N; i++) {
			scanf("%d ", &tmp);
			X ^= tmp;
			sum += tmp;
			m = min(m, tmp);
		}
		
		if(X != 0)
			printf("Case #%d: NO\n", nCase);
		else
			printf("Case #%d: %d\n", nCase, sum-m);
	}
}
