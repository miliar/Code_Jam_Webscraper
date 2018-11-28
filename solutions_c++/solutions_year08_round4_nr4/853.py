#include <cstdio>
#include <algorithm>

using namespace std;

char buf[1010];
int perm[5];

int main() {
	int N;
	scanf("%d\n", &N);

	for(int C = 1; C <= N; ++C) {
		int k;
		scanf("%d\n%s\n", &k, buf);
		for(int i = 0; i < k; ++i) {
			perm[i] = i;
		}
		int mingroups = -1;
		do {
			int groups = 1;
			char prev = buf[perm[0]];
			for(int i = 1; buf[i] != 0; ++i) {
				char next = buf[(i/k)*k + perm[i%k]];
				if(next != prev) {
					groups += 1;
					prev = next;
				}
			}
			if(mingroups == -1 || groups < mingroups) {
				mingroups = groups;
			}
		} while(next_permutation(perm, perm+k));
		printf("Case #%d: %d\n", C, mingroups);
	}
}
