#include <cstdio> 
#include <cstdlib> 
#include <cstring> 

int main() {
	char sub[] = "welcome to code jam";
	char word[501];
	
	int previous[501], now[501];
	int t;
	
	scanf("%d\n", &t);
	for (int c = 1; c <= t; c++) {
		gets(word);
		int n = strlen(word);
		int m = strlen(sub);

		for (int i = 0; i <= n; i++)
			previous[i] = 1;
		
		int result;		
		for (int i = 1; i <= m; i++) {
			if (i & 1) {
				now[0] = 0;
				for (int j = 1; j <= n; j++) {
					int b = (sub[i - 1] == word[j - 1])? previous[j - 1]:0;
					now[j] = (now[j - 1] + b) % 10000;
				}
			} else {
				previous[0] = 0;
				for (int j = 1; j <= n; j++) {
					int b = (sub[i - 1] == word[j - 1])? now[j - 1]:0;
					previous[j] = (previous[j - 1] + b) % 10000;
				}
			}
		}
		result = now[n];
		printf("Case #%d: %d%d%d%d\n", c, (result / 1000), (result % 1000) / 100, (result % 100) / 10, result % 10);
	}
	
	return 0;
}
