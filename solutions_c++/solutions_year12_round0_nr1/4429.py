#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;

char str[1005];
char change[305];

int main()
{
	FILE *in=fopen("speaking.in","r");
	freopen("out.out","w",stdout);
	FILE *refin=fopen("reference.in","r");
	int c,c2;
	for (c=0;c<300;c++)
		fscanf(refin,"%d",(int*)&change[c]);
	int tests;
	fscanf(in,"%d",&tests);fgets(str,1002,in);
	for (int test=1;test<=tests;test++)
	{
		fgets(str,1002,in);
		int len=strlen(str);
		while (str[len-1]=='\n')
			str[--len]='\0';
		printf("Case #%d: ",test);
		for (c=0;c<len;c++)
			printf("%c",change[(int)str[c]]);
		printf("\n");
	}
	
	
	return 0;
}
