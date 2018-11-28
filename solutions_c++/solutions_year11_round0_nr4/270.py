#include<stdio.h>

int nCase, N;

int main() {
	int a[1024];
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d", &N);
		for(int i = 1; i <= N; ++i)
			scanf("%d", &a[i]);
		int sum = 0;
		for(int i = 1; i <= N; ++i) {
			if(a[i] == i || a[i] == 0) continue;
			int l = 1, s;
			for(s = i; a[s] != i; ++l) {
				int t = a[s];
				a[s] = 0;
				s = t;
			}
			a[s] = 0;
			sum += l;
		}
		printf("Case #%d: %d.000000\n", cs, sum);
	}
}
