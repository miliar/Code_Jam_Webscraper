/*************************************************************************
    > File Name: a.cpp
    > Author: mawenxuan
    > Mail: mawenxuan618@gmail.com 
    > Created Time: 六  4/14 22:43:39 2012
 ************************************************************************/

#include<cstdio>
#include<cstring>
#include<cctype>
using namespace std;
int inverse[300];
char exampleinput[][200]={
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char exampleoutput[][200]={
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"};
void init()
{
	for (int i=0;i<3;i++)
	{
		for (int j=0;j<strlen(exampleinput[i]);j++)
		{
			inverse[exampleinput[i][j]-'a']=exampleoutput[i][j]-'a';
		}
	}
	inverse['y'-'a']='a'-'a';
	inverse['e'-'a']='o'-'a';
	inverse['q'-'a']='z'-'a';
	inverse['z'-'a']='q'-'a';
}
int main()
{
	init();
	int t;
	scanf("%d\n",&t);
	char s[200];
	for (int i=0;i<t;i++)
	{
		printf("Case #%d: ",i+1);
		for (int j=0;;j++)	
		{
			char c;
			scanf("%c",&c);
			if (c=='\n')break;
			if (isalpha(c))
			{
				if ('A'<=c&&c<='Z')printf("%c",'A'+inverse[c-'A']);
				else printf("%c",'a'+inverse[c-'a']);
			}
			else printf("%c",c);
		}
		printf("\n");
	}
	return 0;
}
