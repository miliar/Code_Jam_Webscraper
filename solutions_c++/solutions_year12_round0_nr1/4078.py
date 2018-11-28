#include<stdio.h>
#include<string.h>
char s[30]="yhesocvxduiglbkrztnwjpfmaq";
int main(){
	int n,i,j;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	scanf("%d",&n);
	s[29]=getchar();
	for(i=0;i<n;i++){
		char c[120];
		printf("Case #%d: ",i+1);
		fgets(c,105,stdin);
		for(j=0;j<strlen(c);j++){
			if(c[j]<'a'||c[j]>'z')putchar(' ');
			else putchar(s[c[j]-97]);
		}
		if(i!=n-1)puts("");
	}
}