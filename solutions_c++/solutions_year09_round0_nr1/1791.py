#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char dict[5006][17];

int main(void) {
	int l, d, n, m, start;
	char s[500];
	freopen("D:/C_Prog/Contest/alien1.in", "r", stdin);
	freopen("D:/C_Prog/Contest/alien1.out", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);
	for (int i=0; i<d; i++) 
		scanf("%s", dict[i]);
	for (int j=0; j<n; j++) {
		int count = 0;
		scanf("%s", s);
		m = strlen(s);
		for (int i=0; i<d; i++) {
			int isOK = 1;
			start = 0;
			for (int x=0; x<l && isOK; x++) {
				if (s[start] == '(') {
					int partialOK = 0;
					int k;
					for (k=start+1; k<m && s[k]!=')'; k++) {
						if (s[k] == dict[i][x]) {
							partialOK = 1;
						}
					}
					start = k+1;
					if (partialOK == 0) {
						isOK = 0;
						//printf("1. Error checking position x=%d[%c]\n", x, dict[i][x]);
						break;
					}
				} else {
					if (s[start] != dict[i][x]) {
						isOK = 0;
						//printf("2. Error checking position start=%d[%c] x=%d[%c]\n", start, s[start], x, dict[i][x]);
						break;
					}
					start++;
				}
			}
			if (isOK) {
				//printf("Found %s\n", dict[i]);
				count++;
			}
		}
		printf("Case #%d: %d\n", j+1, count);
	}
	return 0;
}
