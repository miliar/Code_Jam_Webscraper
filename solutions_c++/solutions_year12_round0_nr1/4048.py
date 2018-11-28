#include <stdio.h>
#include <string.h>
/*
int main(){
	char c[26], flg[26] = {0}, str[128];
	while(scanf(" %s", str) != EOF){
		for(int i=0; i<strlen(str); i++)
			flg[str[i]-'a'] = 1;
	}
	for(int i=0; i<26; i++)
		if(flg[i] == 0)
			printf("%c", 'a'+i);
	return 0;
}
*/

int main(){
	char c[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	char str[128];
	int T;
	scanf("%d", &T);
	gets(str);
	for(int t=1; t<=T; t++){
		gets(str);
		printf("Case #%d: ", t);
		for(int i=0; i<strlen(str); i++)
			if(str[i] == ' ')
				printf(" ");
			else
				printf("%c", c[str[i]-'a']);
		printf("\n");
	}
	return 0;
}
