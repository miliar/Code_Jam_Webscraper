#include <stdio.h>
#include <bitset>
#include <algorithm>
using namespace std;

bitset<516> table[516];
bitset<516> cut[516];

int dbn, db[516], sum;

int main(void)
{
	int t, ti;
	char sz[512];
	scanf("%d", &t);
	for (ti = 1; ti <= t; ti++) {
		int m, n, i, j, k, l, s;
		scanf("%d %d\n", &m, &n);
		for (i = 0; i < m; i++) {
			fgets(sz, 512, stdin);
			cut[i].reset();
			db[i] = 0;
			for (j = 0; j < n/4; j++) {
				int l = sz[j] < 'A' ? sz[j]-'0' : sz[j]-'A'+10;
				table[i][4*j+0] = ((l&8) != 0);
				table[i][4*j+1] = ((l&4) != 0);
				table[i][4*j+2] = ((l&2) != 0);
				table[i][4*j+3] = ((l&1) != 0);
			}
		}
		db[m] = 0;
		dbn = sum = 0;
		s = m < n ? m : n;
		while (s > 1) {
			for (; s > 1; s--) {
				for (i = 0; i <= m-s; i++) {
					for (j = 0; j <= n-s; j++) {
						bool b = table[i][j];
						for (k = 0; k < s; k++) {
							for (l = 0; l < s; l++) {
								if (table[i+k][j+l] != b^((k+l)&1) || cut[i+k][j+l]) goto bad;
							}
						}
						sum += s*s;
						if (db[s]++ == 0) dbn++;
						for (k = 0; k < s; k++) {
							for (l = 0; l < s; l++) {
								cut[i+k][j+l] = 1;
							}
						}
						goto next;
bad:;
					}
				}
			}	
next:;
		}
		if (sum < m*n) {
			dbn++;
			db[1] = m*n-sum;
		}
		printf("Case #%d: %d\n", ti, dbn);
		for (i = (m < n ? m : n); i > 0; i--) {
			if (db[i] > 0) printf("%d %d\n", i, db[i]);
		}
	}
	return 0;
}