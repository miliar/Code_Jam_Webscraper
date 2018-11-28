#include <stdio.h>

#define MAX 1100

int M[MAX];
int buyed[MAX];

int pow2(int n) {
	int num = 1;
	for (int i=0; i<n; i++)
		num *= 2;
	return num;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++) {
		int P;
		scanf("%d", &P);
		int max = pow2(P);
		for (int i = 0; i<max; i++) {
			scanf("%d", &M[i]);
			buyed[i] = 0;
		}
		char line[10000];
		gets(line);
		for (int i = 0; i<P; i++)
			gets(line);

		int ans = 0;
		for (int i = 0; i<max; i++) {
			int num = i+max;
			for (int j = 1; j<P-M[i]+1; j++) {
				int tmp = num >> (P-j+1);
				if (buyed[tmp] == 0) {
					ans++;
					buyed[tmp] = 1;
				}
			}
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
