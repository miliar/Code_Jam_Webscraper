#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

char c[30]="yhesocvxduiglbkrztnwjpfmaq";
char w[200];

int main(){
	int h,i,j,k,t;
	scanf("%d",&t);
	gets(w);
	for(h=1;h<=t;h++){
		gets(w);
		k=strlen(w);
		printf("Case #%d: ",h);
		for(j=0;j<k;j++){
			if(w[j]>='a' && w[j]<='z')
				putchar(c[w[j]-'a']);
			else putchar(w[j]);
		}
		printf("\n");
	}
	return 0;
}
