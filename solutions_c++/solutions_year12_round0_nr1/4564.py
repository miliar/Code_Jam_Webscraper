#include<stdio.h>

int main()
{
int t,i,n,x;
char str[101],a,lang[28];


lang[11]='i';
lang[12]='g';
lang[13]='l';
lang[14]='b';
lang[15]='k';
lang[16]='r';
lang[17]='z';
lang[18]='t';
lang[19]='n';
lang[20]='w';
lang[21]='j';
lang[22]='p';
lang[23]='f';
lang[24]='m';
lang[25]='a';
lang[26]='q';
lang[1]='y';
lang[2]='h';
lang[3]='e';
lang[4]='s';
lang[5]='o';
lang[6]='c';
lang[7]='v';
lang[8]='x';
lang[9]='d';
lang[10]='u';

scanf("%d",&t);
n=t+1;
scanf("%c",&a);		// trash -- enter
while(t>0)
{
	
	gets(str);
	printf("Case #%d: ",n-t);
	for(i=0;str[i]!='\0';i++)
	{
		if(str[i]!=' '){
		x=str[i]-96;
		printf("%c",lang[x]);}
		else
		printf("%c",str[i]);
	}
	printf("\n");
	t--;
}
return 0;
}

