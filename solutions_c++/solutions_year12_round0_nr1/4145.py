#include<stdio.h>
#include<string.h>
char tran[100] = "yhesocvxduiglbkrztnwjpfmaq";
char s[200];
int main(){
	int t;
	scanf("%d",&t);
	gets(s);
	for(int p = 0 ; p < t ; p++ ){
		gets(s);
		int n = strlen(s);
		printf("Case #%d: ",p+1);
		for(int i = 0 ; i < n; i++){
			if( s[i] == ' ' ) printf(" ");
			else printf("%c",tran[s[i]-'a']);
		}
		printf("\n");
	}
}
