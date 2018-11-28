#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char s[105];

main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,t,i,j;
	scanf(" %d",&T);
	gets(s);
	for(t=0;t<T;t++){
		gets(s);
		printf("Case #%d: ",t+1);
		for(i=0;s[i];i++){
			if(s[i]=='a')	printf("y");
			else if(s[i]=='b')	printf("h");
			else if(s[i]=='c')	printf("e");
			else if(s[i]=='d')	printf("s");
			else if(s[i]=='e')	printf("o");
			else if(s[i]=='f')	printf("c");
			else if(s[i]=='g')	printf("v");
			else if(s[i]=='h')	printf("x");
			else if(s[i]=='i')	printf("d");
			else if(s[i]=='j')	printf("u");
			else if(s[i]=='k')	printf("i");
			else if(s[i]=='l')	printf("g");
			else if(s[i]=='m')	printf("l");
			else if(s[i]=='n')	printf("b");
			else if(s[i]=='o')	printf("k");
			else if(s[i]=='p')	printf("r");
			else if(s[i]=='q')	printf("z");
			else if(s[i]=='r')	printf("t");
			else if(s[i]=='s')	printf("n");
			else if(s[i]=='t')	printf("w");
			else if(s[i]=='u')	printf("j");
			else if(s[i]=='v')	printf("p");
			else if(s[i]=='w')	printf("f");
			else if(s[i]=='x')	printf("m");
			else if(s[i]=='y')	printf("a");
			else if(s[i]=='z')	printf("q");
			else if(s[i]==' ')	printf(" ");
		}
		printf("\n");
	}
}