#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

#define NN 1100
int v[NN];

int main() {
	int N;
	scanf("%d", &N);
	for (int ct = 1; ct <= N; ct++) {
		int n; scanf("%d", &n);
		int s = 0, soma=0;
		for (int i = 0; i < n; i++)  {
			scanf("%d", &v[i]);
			s = s ^ v[i];
			soma += v[i];
		}

		printf("Case #%d: ", ct);

		if (s != 0) printf("NO\n");
		else {
			sort(v, v+n);
			printf("%d\n", soma-v[0]);
		}
	}
	return 0;
}
