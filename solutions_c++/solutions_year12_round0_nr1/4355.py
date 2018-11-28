#include<iostream>
#include<stdio.h>
using namespace std;
char s[]={"yhesocvxduiglbkrztnwjpfmaq"};
char ss[100];
char f(char c){
	if(c==' ')
		return ' ';
	else
		return s[c-'a'];
}
int main(){
	int t,l;
	char s1[100];
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	gets(s1);
	for(int p=1;p<=t;p++){
		gets(ss);
		l=strlen(ss);
		printf("Case #%d: ",p); 
		for(int i=0;i<l;i++)
			printf("%c",f(ss[i]));
		printf("\n");
		
	}
	
	return 0;
}

		


	

