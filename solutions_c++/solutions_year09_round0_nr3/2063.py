// wtcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string.h>

char strcode[] = "welcome to code jam";

int Evaluate(char *str, int part) 
{
	char *result, chr[2];
	int c=0;

	//if (part==19) return 1;
	chr[1]='\0';
	chr[0]=strcode[part];
	result = strpbrk(str, chr);
	while (result) {
		if(part==18) 
			c++;
		else 
			c+=Evaluate(result+1,part+1);
		result = strpbrk(++result, chr);
	};
	return c;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int n, i;
	char p[1000];
	scanf("%d\n",&n);
	for (i=0;i<n;i++) {
		gets(p);
		printf("Case #%d: %04d\n",i+1,Evaluate(p,0));
	}
	return 0;
}

