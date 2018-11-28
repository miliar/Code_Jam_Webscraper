#include<iostream>
#include<algorithm>
using namespace std;
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define max 2000000000
#define eps 1e-7
#define pi acos(-1.0)

char change(char c)
{
	if(c=='a') return 'y';
	else if(c=='b') return 'h';
	else if(c=='c') return 'e';
	else if(c=='d') return 's';
	else if(c=='e') return 'o';
	else if(c=='f') return 'c';
	else if(c=='g') return 'v';
	else if(c=='h') return 'x';
	else if(c=='i') return 'd';
	else if(c=='j') return 'u';
	else if(c=='k') return 'i';
	else if(c=='l') return 'g';
	else if(c=='m') return 'l';
	else if(c=='n') return 'b';
	else if(c=='o') return 'k';
	else if(c=='p') return 'r';
	else if(c=='q') return 'z';
	else if(c=='r') return 't';
	else if(c=='s') return 'n';
	else if(c=='t') return 'w';
	else if(c=='u') return 'j';
	else if(c=='v') return 'p';
	else if(c=='w') return 'f';
	else if(c=='x') return 'm';
	else if(c=='y') return 'a';
	else if(c=='z') return 'q';
	else return ' ';
}
int main()
{
	char str[105];
	int i,t,k=0;
	freopen("A-small-attempt4.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		k++;
		gets(str);
		printf("Case #%d: ",k);
		for(i=0;i<strlen(str);i++)
		{
			if(str[i]==' ') printf(" ");
			else printf("%c",change(str[i]));
		}
		puts("");
	}
	return 0;
}
