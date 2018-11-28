#include <stdio.h>

#define MAXN 36
#define MAXS 102400

int n, s[MAXN], mic[MAXN * MAXS];

void print(int index, int count) {
	if(index == 0) {
		printf("\n");
		return;
	}
	if(count > 0)printf(" ");
	printf("%d", s[mic[index]]);
	print(index - s[mic[index]], count + 1);
}

void action() {
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		scanf("%d", &s[i]);

	for(int i = 0; i < MAXN * MAXS; i++)mic[i] = 0;
	for(int i = 1; i <= n; i++) {
		for(int j = MAXN * MAXS - 1; j >= s[i]; j--) {
			if(j == s[i] || mic[j - s[i]] != 0) {
				if(mic[j] != 0) {
					print(j, 0);
					printf("%d ", s[i]);
					print(j - s[i], 0);
					return;
				}
				mic[j] = i;
			}
		}
	}
	printf("Impossible\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d:\n", i);
		action();
	}
return 0;
}
