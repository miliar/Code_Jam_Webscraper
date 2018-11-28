#include<stdio.h>
#include<string.h>
char map[30]={};
char tra[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
main()
{
	int i,T,j;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	char s[1000],s1[1000],junk[1000];
	scanf("%d",&T);
	gets(junk);
	for(j=0;j<T;j++)
	{
		gets(s);
		printf("Case #%d: ",j+1);
		for(i=0;i<strlen(s);i++)
		{
			if(s[i]>='a' && s[i]<='z')
				printf("%c",tra[s[i]-'a']);
			else printf("%c",s[i]);
		}
		puts("");
	}
	/*
	while(gets(s)!=NULL)
	{
		gets(s1);
		for(i=0;i<strlen(s);i++)
		{
			if(s[i]>='a' && s[i]<='z')map[s[i]-'a']=s1[i];
		}
	}
	for(i=0;i<='z'-'a';i++)
	{
		printf(",'%c'",map[i]);
	}*/
	scanf(" ");
}
