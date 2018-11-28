#include <stdio.h>
#include <string.h>


int main() {
	int n, i;
	char str[102];
	char format[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	scanf("%d\n", &n);

	for(i = 0; i < n; i++) {
		gets(str);
		int len = strlen(str);
		int j;
		printf("Case #%d: ", i+1);
		for(j = 0; j < len; j++) {
			if(str[j] == ' ') {
				printf(" ");
			}
			else {
				printf("%c", format[str[j] - 'a']);
			}
		}
		printf("\n");
	}
	return 0;
}