#include <iostream>
using namespace std;

const int MaxN = 1010;

int TCase, N, G[MaxN], Round, Limit, Next[MaxN];
long long Sum[MaxN], Ans;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt ", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; ++Case) {
		//init
		scanf("%d%d%d", &Round, &Limit, &N);
		for (int i = 1; i <= N; ++i)
			scanf("%d", G+i);
		//get Next
		for (int i = 1; i <= N; ++i) {
			Sum[i] = 0;
			for (int j = i; ; ) {
				if (Sum[i] + G[j] > Limit) {
					Next[i] = j;
					break;
				}
				Sum[i] += G[j];
				if (j == N) j = 1;
				else ++j;
				if (j == i) {
					Next[i] = j;
					break;
				}
			}
		}
		//get Answer
		Ans = 0;
		for (int i = 0, cur = 1; i < Round; ++i) {
			Ans += (long long)Sum[cur];
			cur = Next[cur];
		}
		printf("Case #%d: %lld\n", Case, Ans);
	}
	return 0;
}
