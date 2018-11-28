#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	char a[4][101], b[4][101] , map[26];
	strcpy(a[0], "ejp mysljylc kd kxveddknmc re jsicpdrysi");
	strcpy(b[0], "our language is impossible to understand");
	strcpy(a[1], "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	strcpy(b[1], "there are twenty six factorial possibilities");
	strcpy(a[2], "de kr kd eoya kw aej tysr re ujdr lkgc jv");
	strcpy(b[2], "so it is okay if you want to just give up");
	strcpy(a[3], "a zq"), strcpy(b[3], "y qz");
	for(int i = 0; i < 4; i++) {
		for(int j = 0; a[i][j] != '\0'; j++) {
			if(a[i][j] != ' ') {
				map[a[i][j] - 'a'] = b[i][j];
			}
		}
	}
	int T, cases;
	scanf("%d%*c", &T);
	cases = T;
	while(T--) {
		char str[101];
		scanf("%[^\n]%*c", str);
		printf("Case #%d: ", cases - T);
		for(int i = 0; str[i] != '\0'; i++) {
			if(str[i] != ' ') {
				printf("%c", map[str[i] - 'a']);
			} else {
				printf(" ");
			}
		}
		if(T) {
			printf("\n");
		}
	}
	return 0;
}