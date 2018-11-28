#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

char line[1002];
char line2[1002];

int main() {
	freopen("D-small-attempt3.in", "r", stdin);
	freopen("D-small.txt", "w", stdout);
	int ntc, tc = 0, k, i, j;
	scanf("%d", &ntc);
	while(ntc--) {
		printf("Case #%d: ", ++tc);
		scanf("%d %s", &k, line);
		int a[16], len = strlen(line);
		for(i = 0; i < k; ++i)
			a[i] = i;
		int min = 1000000000;
		do {
			strcpy(line2, line);
			for(i = 0; i < len; i+=k) {
				char A[16];
				for(j = 0; j < k; ++j) {
					A[j] = line[i+a[j]];
				}
				for(j = 0; j < k; ++j) {
					line[i+j] = A[j];
				}
			}
			int cnt = 1;
			for(i = 1; i < len; ++i) {
				if(line[i] != line[i-1])
					cnt++;
			}
			if(cnt < min) min = cnt;
			strcpy(line, line2);
		} while(next_permutation(a, a+k));
		printf("%d\n", min);
	}
	return 0;
}