#include<iostream>
#include<cstring>
#include<cstdio>
	char s[1100000];
using namespace std;
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int t;
	scanf("%d",&t);
	getchar();
	char tran[27] = "yhesocvxduiglbkrztnwjpfmaq";
	for(int casenum = 1;casenum<=t;casenum++){
		gets(s);
		printf("Case #%d: ",casenum);
		for(int i = 0;i<strlen(s);i++){
			if(s[i]==' ')printf(" ");
			else printf("%c",tran[s[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}