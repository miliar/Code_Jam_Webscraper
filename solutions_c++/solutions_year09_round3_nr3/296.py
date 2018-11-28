#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int v[200];
int N, Q, P;
bool marca[200];

int simula() {
	memset(marca, 0, sizeof(marca));
	int ans = 0;
	for (int i=0;i<Q;i++) {
		marca[v[i]] = true;
		for (int j=v[i]-1;j>=1;j--) {
			if (marca[j]) break;
			ans++;
		}
		for (int j=v[i]+1;j<=P;j++) {
			if (marca[j]) break;
			ans++;
		}
	}
	return ans;
}

int main() {
	int _42=1;
	scanf(" %d", &N);
	while (N--) {
		scanf(" %d %d", &P, &Q);
		for (int i=0;i<Q;i++) {
			scanf(" %d", &v[i]);
		}
		sort(v, v+Q);
		//for (int i=0;i<Q;i++) printf("%d ", v[i]);
		int ans = simula();
		while (next_permutation(v, v+Q)) {
			//for (int i=0;i<Q;i++) printf("%d ", v[i]);
			//printf("\n");
			ans = min(ans, simula());
		}
		printf("Case #%d: %d\n", _42++, ans);
	}

	return 0;
}
