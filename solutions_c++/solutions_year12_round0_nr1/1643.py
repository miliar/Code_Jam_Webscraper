#include <stdio.h>
#include <string.h>

char str[]="yhesocvxduiglbkrztnwjpfmaq";
char input[1010];
char output[1010];

int main() {
	int t, cases=0;
	
	scanf("%d",&t);
	gets(input);
	while( t-- ) {
		gets(input);
		int len = strlen(input);
		for(int i=0;i<len;++i) {
			if(input[i] == ' ' || input[i] == '\n' || input[i] == '\0')	{
				output[i] = input[i];
				continue;
			}
			output[i] = str[input[i]-'a'];
		}
		
		output[len] = '\0';
		
		printf("Case #%d: ", ++cases);
		puts(output);
	}
	

	return 0;
}
