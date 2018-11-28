#include <stdio.h>

char *c1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz";
char *c2 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq";

int main(){
	char map[256]={0};
	for(int i=0;c1[i];i++){
		map[c1[i]] = c2[i];
	}
	int T;
	scanf("%d\n", &T);
	for(int TT = 1; TT<=T;TT++){
		printf("Case #%d: ", TT);
		char ch[200];
		gets(ch);
		for(int i=0;ch[i];i++){
			printf("%c", map[ch[i]]);
		}
		printf("\n");
	}
	return 0;
}