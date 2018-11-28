// codejam.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include "iostream"
using namespace std;

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	char aft[]="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char bef[]="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	char map[128]={0};
	map['y']='a';
	map['e']='o';
	map['q']='z';
	int vis[128]={0};
	vis['a']=vis['o']=vis['z']=1;
	for (int i = 0; i < strlen(aft); i++) {
		map[aft[i]]=bef[i];
		vis[bef[i]]=1;
	}
	for(int i=0;i<26;i++)
	{
		if(map[i+'a']==0)
			for(int j=0;j<26;j++)if(vis[j+'a']==0)
			{
				map[i+'a']=j+'a';
			}
	}
	int N; char buf[100+1];//?
	scanf("%d",&N);getchar();
	int cnt=0;
	while(fgets(buf, 100+1, stdin)!=NULL)
	{
		//int len=strlen(buf);
		if(buf[0]=='\n')continue;
		if(buf[strlen(buf)-1]=='\n')//?
			buf[strlen(buf)-1]='\0';
		char origin[100+2];
		for(int i=0;i<strlen(buf);i++)
		{
			origin[i]=map[buf[i]];
		}
		origin[strlen(buf)]='\0';
		printf("%s%d%s%s\n", "Case #",(++cnt) ,": ",origin);//ca
	}
	return 0;
}