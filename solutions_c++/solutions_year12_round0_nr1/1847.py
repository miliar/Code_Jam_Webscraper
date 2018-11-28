#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int main(){
	char str[28]={"yhesocvxduiglbkrztnwjpfmaq"};
	char ch[200];
	int n,m,i,j,k;
	scanf("%d",&n);
	getchar();
	for(i=1;i<=n;i++){
		gets(ch);
		printf("Case #%d: ",i);
		for(j=0;j<strlen(ch);j++)
			if(ch[j]>='a'&&ch[j]<='z') printf("%c",str[ch[j]-'a']);
			else printf("%c",ch[j]);
			printf("\n");
	}
}