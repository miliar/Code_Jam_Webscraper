#include<stdio.h>
#include<stdlib.h>
#include<string>
int main()
{
	char string[200];
	int n,i,j;

	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&n);
	for(i=0;i<n;i++)
	{
		gets(string);
		for(j=0;j<strlen(string);j++)
		switch(string[j])
		{
			case 'a': string[j]='y';
				break;
		case 'b': string[j]='h';
				break;
		case 'c': string[j]='e';
				break;
		case 'd': string[j]='s';
				break;
		case 'e': string[j]='o';
				break;
		case 'f': string[j]='c';
				break;
		case 'g': string[j]='v';
				break;
		case 'h': string[j]='x';
				break;
		case 'i': string[j]='d';
				break;
		case 'j': string[j]='u';
				break;
		case 'k': string[j]='i';
				break;
		case 'l': string[j]='g';
				break;
		case 'm': string[j]='l';
				break;
		case 'n': string[j]='b';
				break;
		case 'o': string[j]='k';
				break;
		case 'p': string[j]='r';
				break;
		case 'q': string[j]='z';
				break;
		case 'r': string[j]='t';
				break;
		case 's': string[j]='n';
				break;
		case 't': string[j]='w';
				break;
		case 'u': string[j]='j';
				break;
		case 'v': string[j]='p';
				break;
		case 'w': string[j]='f';
				break;
		case 'x': string[j]='m';
				break;
		case 'y': string[j]='a';
				break;
		case 'z': string[j]='q';
				break;
		}
		printf("Case #%d: %s\n",i+1,string);
	}
	return 0;
}