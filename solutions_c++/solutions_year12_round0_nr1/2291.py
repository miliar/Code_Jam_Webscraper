#include<stdio.h>
#include<string.h>

int map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd',
			   'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't',
			   'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(){
	int T, cnt;
	cnt = 0;
	scanf("%d\n", &T);
	while(T--){
		char s[1001];
		gets(s);
		printf("Case #%d: ", ++cnt);
		int len = strlen(s);
		for(int i = 0; i < len; i++){
			if(s[i] == ' ') printf("%c", s[i]);
			else printf("%c", map[s[i]-'a']);
		}
		puts("");
	}

	return 0;
}
