#include <cstdio>

char combos[50][5];
char oppos[50][5];
char str[105];
char ans[105];
int isin[256];

int main() {
	int ncases;
	scanf("%d",&ncases);
	for(int casenum = 1; casenum <= ncases; casenum++) {
		int nCombos, nOppos;
		scanf("%d", &nCombos);
		for(int i = 0; i < nCombos; i++)
			scanf("%s", combos[i]);
		scanf("%d", &nOppos);
		for(int i = 0; i < nOppos; i++)
			scanf("%s", oppos[i]);
		int strlen;
		scanf("%d", &strlen);
		scanf("%s", str);
		int len = 0;
		for(char c = 'A'; c <= 'Z'; c++)
			isin[c] = 0;
		for(int i = 0; i < strlen; i++) {
			ans[len++] = str[i];
			isin[str[i]]++;
			for(int j = 0; j < nCombos; j++) {
				if((ans[len-1] == combos[j][0] && ans[len-2] == combos[j][1]) || (ans[len-1] == combos[j][1] && ans[len-2] == combos[j][0])) {
					isin[ans[len-1]]--;
					isin[ans[len-2]]--;
					isin[combos[j][2]]++;
					ans[len-2] = combos[j][2];
					len--;
					break;
				}
			}
			for(int j = 0; j < nOppos; j++) {
				if(isin[oppos[j][0]] && isin[oppos[j][1]]) {
					len = 0;
					for(char c = 'A'; c <= 'Z'; c++)
						isin[c] = 0;
				}
			}
		}
		printf("Case #%d: [", casenum);
		for(int i = 0; i < len; i++) {
			printf("%c", ans[i]);
			if(i != len-1)
				printf(", ");
		}
		printf("]\n");
	}
}
