#include<stdio.h>
#include<ctype.h>
#include<string.h>

char decode[] = "yhesocvxduiglbkrztnwjpfmaq";
int tests;

int main() {
	scanf("%d\n",&tests);
	for(int t = 1; t <= tests; t++) {
		char buffer[110];
		gets(buffer);
		for(int i = 0;i < strlen(buffer); i++) {
			if (isalpha(buffer[i])) {
				buffer[i] = decode[buffer[i]-'a'];
			}
		}
		printf("Case #%d: %s\n",t,buffer);
	}		
	return 0;
}