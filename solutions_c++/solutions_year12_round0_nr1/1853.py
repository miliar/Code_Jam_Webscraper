#include<cstdio>

int main(){
	int t;
	char key[] = "yhesocvxduiglbkrztnwjpfmaq";
	char s[256];
	scanf("%d ",&t);
	for(int c=1; c<=t; c++){
		fgets(s,256,stdin);
		printf("Case #%d: ",c);
		for(int i=0;s[i] && s[i]!='\n';i++)
			if(s[i]>='a' && s[i]<='z')
				printf("%c",key[s[i]-'a']);
			else printf("%c",s[i]);
		printf("\n");
	}
	return 0;
}
