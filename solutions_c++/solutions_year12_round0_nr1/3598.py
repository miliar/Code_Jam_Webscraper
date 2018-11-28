#include <stdio.h>
#include <string.h>

int main()
{
	char s1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char s2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char s3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";


	char y1[] = "our language is impossible to understand";
	char y2[] = "there are twenty six factorial possibilities";
	char y3[] = "so it is okay if you want to just give up";

	int map[100] = {0},i;
	map['z' - 'a'] = 'q';
	for(i=0;s1[i];i++)
		map[ s1[i] - 'a' ] = y1[i];

	for(i=0;s2[i];i++)
		map[ s2[i] - 'a' ] = y2[i];

	for(i=0;s3[i];i++)
		map[ s3[i] - 'a' ] = y3[i];

	int flag[30] = {0},t;
	for(i=0;i<26;i++)
	{
		if( map[i] )
			flag[ map[i] - 'a' ] = 1;
		if( map[i] == 0 )
		{
			t = i;
		}
	}

	for(i=0;i<26;i++)
	{
		if( flag[i] == 0 )
		{
			map[t] = 'a' + i;
		}
	}

	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	char g[500]={0},s[500] = {0};
	int T,case_no=0,c;
	scanf("%d%c",&T,&c);
	while( T-- )
	{
		gets(g);
		for(i=0;g[i];i++)
		{
			if( g[i] == ' ' )
				s[i] = g[i];
			else
				s[i] = map[ g[i] - 'a' ];
		}
		printf("Case #%d: %s\n",++case_no,s);
		memset(g,0,sizeof(g));
		memset(s,0,sizeof(s));
	}

	return 0;
}