#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>


//char s[100000], s2[100000], map[300];
//q, z.  q, z
char maps[2][300] = 
{ {
' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t',
'u','v','w','x','y', 'z'},
{
' ','y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r', 'z','t','n','w',
'j','p','f','m','a', 'q'}};
char map[300];

char s[300];


int main() {
	for( int i=0; maps[0][i]; i++ )
		map[maps[0][i]] = maps[1][i]; 
	int n, flg;
	scanf("%d", &n);
	gets(s);
	for( int i=0; i<n; i++ ) {
		gets(s);
		printf("Case #%d: ", i+1);
		for( int j=0; s[j]; j++ )
			putchar(map[s[j]]?map[s[j]]:s[j]);
		puts("");
	}
	gets(s);
/*	int n, flg;
	scanf("%d", &n);
	gets(s);
	for( int i=0; i<n; i++ ) {
		gets(s);
		gets(s2);
		for( int j=0; s[j]; j++ )
			map[s[j]] = s2[j];
	}
	printf("{ {\n");
	flg = 0;
	for( int i=0; i<300; i++ )
		if( map[i] ) {
			printf("%s\'%c\'", flg?",":"", i);
			flg = 1;
		}
	printf("},\n{");
	flg = 0;
	for( int i=0; i<300; i++ )
		if( map[i] ) {
			printf("%s\'%c\'", flg?",":"", map[i]);
			flg = 1;
		}
	printf("}};");
	gets(s);
	gets(s);
	gets(s);
*/
}
