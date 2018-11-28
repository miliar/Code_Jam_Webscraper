#include <iostream>
#include <algorithm>
#include<functional>
#include <string>
#include <stdio.h>
using namespace std;
char ch[30];
string s1[100]={"ejp","mysljylc", "kd", "kxveddknmc", "re", "jsicpdrysi",
"rbcpc","ypc", "rtcsra", "dkh", "wyfrepkym", "veddknkmkrkcd",
"de", "kr","kd", "eoya", "kw", "aej", "tysr", "re", "ujdr", "lkgc", "jv"},
s2[100]={"our", "language", "is", "impossible", "to", "understand",
"there" ,"are", "twenty", "six", "factorial", "possibilities",
"so" ,"it", "is", "okay", "if", "you", "want", "to", "just" ,"give", "up"};
char s[200];
int arr[30];
int main()
{
	freopen("D:\\Visual Studio 2008\\google code jam\\A-small-attempt3.in", "r", stdin ) ;

	freopen("D:\\Visual Studio 2008\\google code jam\\A-small-attempt3.out", "w", stdout ) ;
	for(int i=0;i<23;++i)
	{
		for(int j=0;j<s1[i].length();++j)
		{
			ch[s1[i][j]-'a']=s2[i][j];
		}
	}
	ch[16]='z';ch[25]='q';
	//for(int i=0;i<26;++i)
	//{	cout<<i<<" "<<ch[i]<<endl;
	//	arr[ch[i]-'a']=1;
	//}
	//cout<<endl<<endl;
	//for(int i=0;i<26;++i)
	//	if(arr[i]==0)
	//		cout<<i<<" "<<char(i+'a')<<endl;
	//cout<<endl<<endl;
	//int arr[30];
	//
	//for(int i=0;i<26;++i)
	//{
	//	arr[i]=0;
	//}
	//for(int i=0;i<26;++i)
	//	if(ch[i]!=' ')
	//		arr[i]=1;
	//for(int i=0;i<)
	int t;
	scanf("%d ",&t);
	for(int k=1;k<=t;++k)
	{
		gets(s);
		printf("Case #%d: ",k);
		for(int i=0;i<strlen(s);++i)
		{
			if(s[i]==' ')
				printf(" ");
			else
				printf("%c",ch[s[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}