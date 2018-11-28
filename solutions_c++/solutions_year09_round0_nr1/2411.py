#include <cstdio>

int l, d, n;
char dic[5024][32];

int main(void) {
	int i, j;
	scanf("%d %d %d", &l, &d, &n);

	for(i = 0; i < d; i++) scanf("%s", &dic[i]);
	for(int c = 1; c <= n; c++) {
		int ans = 0;
		char pat[10000], *p;
		int pos[15][26], flag;

		for(i = 0; i < 15; i++) for(j = 0; j < 26; j++) pos[i][j] = 0;

		scanf("%s", &pat);
		i = 0;
		flag = false;
		for(p = pat; *p; p++) {
			if(*p == '(') flag = 1;
			else if(flag) {
				if(*p == ')') {
					flag = 0;
					i++;
				}
				else pos[i][*p - 'a'] = 1;
			} else {
				pos[i++][*p - 'a'] = 1;
			}
		}

/*		for(i = 0; i < 26; i++) {
			printf("%c:", 'a' + i);
			for(j = 0; j < l; j++) {
				printf(" %d", pos[j][i]);
			}
			printf("\n");
		}*/

		for(i = 0; i < d; i++) {
			bool pode = true;
			for(j = 0; j < l && pode; j++)
				if(!pos[j][dic[i][j]-'a']) pode = !pode;
/*			if(pode) printf("%s pode.\n", dic[i]);*/
			if(pode) ans++;
		}

		printf("Case #%d: %d\n", c, ans);
	}

	return 0;
}
