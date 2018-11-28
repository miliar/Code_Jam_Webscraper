#include<iostream>
#include<cstdio>
using namespace std;
char str1[1000];
char mark[27] = "yhesocvxduiglbkrztnwjpfmaq";
/*
int main()
{
	mark['z'-'a'] = 'q';
	mark['q'-'a'] = 'z';
	int i;
	int t=3;
	while(t--){
		gets(str1);
		gets(str2);
		for(i=0;str1[i];i++)
		{
			if(str1[i]>='a'&&str1[i]<='z')
			mark[str1[i]-'a'] = str2[i];
		}
	}
	for(i=0;i<26;i++)
		printf("%c",'a'+i);
	printf("\n");
	for(i=0;i<26;i++)
	{
		printf("%c",mark[i]);
	}
	return 0;
}
*/
/*
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities
de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
*/
/*
yhesocvxduiglbkrztnwjpfmaq
*/
int main()
{
//   	freopen("A-small-attempt2.in","r",stdin);
//   	freopen("A-small-attempt2.out","w",stdout);
// 
	int t;
	int cases = 0;
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		cases++;
		gets(str1);
		printf("Case #%d: ",cases);
		for(int i=0;str1[i];i++)
		{
			if(str1[i]>='a'&&str1[i]<='z')
				printf("%c",mark[str1[i]-'a']);
			else
				printf("%c",str1[i]);
		}
		printf("\n");
	}

return 0;
}