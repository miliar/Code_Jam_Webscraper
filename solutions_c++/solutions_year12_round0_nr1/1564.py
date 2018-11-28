#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char a[28];
char s[300];
void init()
{
    strcpy( a, "yhesocvxduiglbkrztnwjpfmaq\0");
}
int main()
{
	init();
	int n;
	scanf( "%d", &n );
	gets(s);
	for ( int i = 1; i <= n; i++ )
	{
		gets(s);
		printf( "Case #%d: ",i );
		int l = strlen( s );
		for ( int j = 0; j < l; j++ )
		if ( s[j] != ' ' )
		{
			printf( "%c", a[s[j]-'a'] );
		}
		else printf( " " );
		printf("\n");
	}
	return 0;
}