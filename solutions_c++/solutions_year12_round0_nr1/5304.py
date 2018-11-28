#include<stdio.h>
#include<string.h>
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	char mapping[]="yhesocvxduiglbkrztnwjpfmaq";
	int T;
	scanf("%d\n",&T);
	for(int Case = 1 ; Case <= T ; ++Case){
		char temp[105];
		gets(temp);
		int len=strlen(temp);
		printf("Case #%d: ",Case);
		for(int i = 0 ; i < len ; ++i){
			if(temp[i]>='a' && temp[i]<='z')
				printf("%c",mapping[temp[i]-'a']);
			else
				printf("%c",temp[i]);
		}
		printf("\n");
	}
	return 0;
}