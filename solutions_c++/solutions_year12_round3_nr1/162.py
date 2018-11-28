#include <stdio.h>
#include <stdlib.h>

#define MAX 1024

int n, m[MAX][MAX], in[MAX], out[MAX], used[MAX];

int check(int index) {
	if(used[index] == 1)return 1;
	used[index] = 1;
	for(int i = 1; i <= n; i++) {
		if(m[index][i]) {
			if(check(i))return 1;
		}
	}
	return 0;
}

void action() {
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) {
		in[i] = 0;
		out[i] = 0;
		for(int j = 1; j <= n; j++)
			m[i][j] = 0;
	}
	for(int i = 1; i <= n; i++) {
		int c, tmp;
		scanf("%d", &c);
		for(int j = 1; j <= c; j++) {
			scanf("%d", &tmp);
			m[i][tmp] = 1;
			in[i]++;
			out[tmp]++;
		}
	}
	for(int i = 1; i <= n; i++) {
		if(out[i] == 0) {
			for(int j = 1; j <= n; j++) {
				used[j] = 0;
			}
			if(check(i)) {
				printf("Yes\n");
				return;
			}
		}
	}
	printf("No\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		action();
	}
return 0;
}
