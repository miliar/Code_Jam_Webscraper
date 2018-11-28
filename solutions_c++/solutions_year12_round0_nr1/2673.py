#include<stdio.h>
#include<string.h>

char code[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main()
{
	//freopen("E:\\TDDOWNLOAD\\A-small-attempt0.in","r",stdin);
	//freopen("E:\\TDDOWNLOAD\\A-small.out","w",stdout);
	
	int T;
	scanf("%d\n",&T);
	for(int cse=1;cse<=T;cse++)
	{
		char text[110];
		gets(text);
		int L=strlen(text);
		
		printf("Case #%d: ",cse);
		for(int i=0;i<L;i++)
			if(text[i]>='a'&&text[i]<='z') printf("%c",code[text[i]-'a']);
			else printf("%c",text[i]);	
		printf("\n");
	}
	return 0;
}
