#include<stdio.h>
#include<string.h>
char str[128]="yhesocvxduiglbkrztnwjpfmaq";
int main(){
	freopen("A-small-attempt5.in","r",stdin);
	freopen("oo.out","w",stdout);
	int t,ca=1;
	scanf("%d",&t);
	getchar();
	while(t--){
		char s[1010];
		gets(s);
		printf("Case #%d: ",ca++);
		for(int i=0;s[i];i++){
			if(s[i]==' ')
			printf(" ");
			else printf("%c",str[s[i]-'a']);
		}
		puts("");
	}
	return 0;
}
