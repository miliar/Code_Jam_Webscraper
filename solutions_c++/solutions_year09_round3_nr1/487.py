#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
int change[128];
int num[10000];
int n;

int main() {
	char str[10000];
	long long a;
	int T, t = 1;
	int i,j ;
	int count;
	bool zero;
	scanf("%d", &T);
	while (T--) {
		scanf("%s", str);
		memset(change, -1, sizeof(change));
		count = 1;
		zero = false;
		n = strlen(str);
		for (i = 0; str[i]; i++) {
			if (change[str[i]] == -1) {
				if (count == 2 && zero == false) {
					zero = true;
					change[str[i]] = 0;
				}
				else {
					change[str[i]] = count;
					count++;
				}
			}
			num[i] = change[str[i]];
		}
		//printf("%d\n", count);
		a = 0;
		for (i = 0; i < n; i++) {
			a *= count;
			a += num[i];
		}
		printf("Case #%d: %lld\n",t++, a);
	}
	return 0;
}
