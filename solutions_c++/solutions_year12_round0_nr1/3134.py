#include <stdio.h>
#include <string.h>

int gmap[26];
char input[1024];
char src[][256]={"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char dest[][256] ={"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
void decode()
{
	int i;
	gmap['z'-'a']='q';
	gmap['q'-'a']='z';
	for(  i = 0 ; i < 3 ; i ++ )
	{
		int len = strlen(dest[i]);
		for(int j = 0 ; j < len ;j ++ )
		{
			if( dest[i][j] == ' ')
				continue;
			gmap[src[i][j]-'a']=dest[i][j];
		}
	}
	for(  i = 0 ; i < 26 ; i ++ )
	{
		//printf("%c -> %c\n",'a'+i,gmap[i]);
	}
}
void translate( char * str)
{
	int len = strlen(str);
	for( int i = 0 ; i < len; ++ i )
	{
		if( ' ' == str[i])
			continue;
        str[i] = gmap[ str[i]-'a'];
	}
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);
	decode();
	int T;
	scanf("%d",&T);
	gets(input);
	for( int i = 1 ; i <= T ; ++ i )
	{
		gets(input);
		translate(input);
		printf("Case #%d: %s\n",i,input);
	}
	return 0;
}