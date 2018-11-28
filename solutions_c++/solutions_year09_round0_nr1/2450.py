#include <stdio.h>
#include <string.h>

int cur, l, d, n;
char line[30][15], check[2000];
char rules[30][1000];

int scan() {
	int i=0, depth = 0, rx=0, ry=0, ret=0;
	while (check[i]) {
//		printf("%c %s\n", check[i], rules[rx]);
		if (check[i]=='(') {
			depth++;
			ry=0;
		}
		else if (check[i]==')') {
			depth--;
			ry++;
			rules[rx][ry] = 0;
			rx++;
		}
		else {
			if (depth==0) {
				rules[rx][0] = check[i];
				rules[rx][1] = 0;
				rx++;
			}
			else {
				rules[rx][ry] = check[i];
				ry++;
			}
		}
		i++;
	}
	int flag=0;
	for (i=0; i<d; i++) {
		int j=0;
		for (j=0; j<l; j++) {
			int k=0;
			flag=0;
			while (rules[j][k]) {
				if (rules[j][k]==line[i][j]) {
					flag=1;
					break;
				}
				k++;
			}
			if (!flag) break;
		}
		if (flag) {
			ret++;
		}
	}
	return ret;
}

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	scanf("%d %d %d ", &l, &d, &n);
	for (int i=0; i<d; i++) {
		gets(line[i]);
	}
	for (int i=0; i<n; i++) {
		gets(check);
		cur = 0;
		printf("Case #%d: %d\n", i+1, scan());
	}
	return 0;
}
