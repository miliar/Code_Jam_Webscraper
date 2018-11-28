#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

const int MAXN = 1000 + 10;
int step[MAXN];
int a[MAXN];

int main()
{
	int T, N;	double res;
	scanf("%d", &T);
	for (int ncas = 1; ncas <= T; ncas++) {
		scanf("%d", &N);
		for (int i = 1; i <= N; i++) {
			scanf("%d", &a[i]);
		}
		int nstep = 1;
		memset(step, 0, sizeof(step));
		res = 0;	int num;
		for (int i = 1; i <= N; i++) {
			if (step[i] != 0) {
				continue;
			}
			num = 0;
			int j;
			for (j = i; a[j] != i; j = a[j]) {
				step[j] = nstep;
				num++;
			}
			step[j] = nstep++;
			if (num != 0) {
				res += num + 1;
			}
		}
		printf("Case #%d: %.6f\n", ncas, res);
	}
	return 0;
}
