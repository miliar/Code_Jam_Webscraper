#include <stdio.h>
#include <string.h>

int main()
{
	int t,T,i;
	char code[27] = "yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d",&T);
	gets(new char[1]);
	for(t=1;t<=T;t++){
		char txt[105]="";
		gets(txt);
		int L = strlen(txt);
		for(i=0;i<L;i++){
			if(txt[i]==' ')continue;
			txt[i] = code[txt[i]-'a'];
		}
		printf("Case #%d: %s\n",t,txt);		
	}
}
