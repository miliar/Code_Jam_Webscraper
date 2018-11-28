#include <stdio.h>
#include <string.h>

#define MAX_LENGTH  510
#define LET 19


int main() {
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	char input[] = "welcome to code jam";
	int n;
	scanf("%d\n", &n);
	for (int cases = 0; cases < n; cases++) {
		printf("Case #%d: ", (cases + 1));
		char str[MAX_LENGTH];
		gets(str);
		int len = strlen(str);
            int ans[len][LET + 1];
            for (int l = 0; l < len; l++) ans[l][0] = 1;
            for (int i = 1; i <= LET; i++) {
            	for (int l = 0; l < len; l++) {
            		//ans[l][i]
            		ans[l][i] = 0;
            		ans[l][i] += (l >= 1 ? ans[l - 1][i] : 0);
            		if ((l + 1 >= i) && (input[i - 1] == str[l])) {
            			if (l == 0) ans[l][i]++; else
            			ans[l][i] += ans[l - 1][i - 1];
            		}
            		
            		ans[l][i] %= 10000;
            		
            	}
            }
            printf("%.4d\n", ans[len - 1][LET]);      
	}

	return 0;
}
