#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void process()
{
	int i;
	char table[28] = {"yhesocvxduiglbkrztnwjpfmaq"};
	char data[1000];
	gets(data);
	for(i=0; i<strlen(data); i++) {
		if( data[i] == ' ' ) {
			printf(" ");
		} else {
			printf("%c", table[data[i]-'a']);
		}
	}
	printf("\n");
}
int main()
{
	int n;
	int i;
	char data[100];
	
	freopen("input.txt","r", stdin);
	freopen("output.txt","w", stdout);
	scanf("%d", &n);
	gets(data);
	for(i=0; i<n; i++) {
		printf("Case #%d: ", i+1);
		process();
	}
	return 0;
}