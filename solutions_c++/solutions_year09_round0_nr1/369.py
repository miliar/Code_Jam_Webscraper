#include <stdio.h>

#define MAXL 16
#define MAXW 51200

int l, d, n;
int pattern[MAXL][26], ans;
char word[MAXW][MAXL], str[MAXL * MAXL * MAXL];

int main(int argc, char *argv[])
{
	int i, j, k;

	scanf("%d %d %d", &l, &d, &n);
	for(i = 0; i < d; i++)
		scanf("%s", word[i]);

	for(i = 1; i <= n; i++) {
		scanf("%s", str);
		for(j = 0; j < l; j++)
			for(k = 0; k < 26; k++)
				pattern[j][k] = 0;
		for(j = 0, k = 0; j < l; j++, k++) {
			if(str[k] == '(') {
				for(++k; str[k] != ')'; k++)
					pattern[j][str[k] - 'a'] = 1;
			} else {
				pattern[j][str[k] - 'a'] = 1;
			}
		}

		ans = 0;
		for(j = 0; j < d; j++) {
			for(k = 0; k < l; k++)
				if(!pattern[k][word[j][k] - 'a'])break;
			if(k == l)
				ans++;
		}
		printf("Case #%d: %d\n", i, ans);
	}

	return 0;
}
