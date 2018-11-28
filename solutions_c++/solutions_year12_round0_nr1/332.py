#include<iostream>
#include<map>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std;
string ss[2][3];
int t;
char s[222];
char mp[333];
int main()
{
	ss[0][0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	ss[0][1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	ss[0][2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	ss[1][0]="our language is impossible to understand";
	ss[1][1]="there are twenty six factorial possibilities";
	ss[1][2]="so it is okay if you want to just give up";
	mp['z']='q';
	mp['q']='z';
	for (int i=0;i<3;i++)
	{
		for (int j=0;j<ss[0][i].size();j++)
			mp[ss[0][i][j]]=ss[1][i][j];
	}
	scanf("%d",&t);
	gets(s);
	int gg=0;
	while (t--)
	{
		gets(s);
		printf("Case #%d: ",++gg);
		for (int i=0;i<strlen(s);i++)
			printf("%c",mp[s[i]]);
		printf("\n");
	}
	return 0;
}
