#include <iostream>
#include <cstring>
#include <stdio.h>
using namespace std;

int T;
char s[200];
char c[26];

void set( char ch, char s )
{
    c[ ch-'a' ] = s;
}

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);

    set( 'e', 'o' );
    set( 'j', 'u' );
    set( 'p', 'r' );
    set( 'm', 'l' );
    set( 'y', 'a' );
    set( 's', 'n' );
    set( 'l', 'g' );
    set( 'c', 'e' );
    set( 'k', 'i' );
    set( 'd', 's' );
    set( 'x', 'm' );
    set( 'v', 'p' );
    set( 'n', 'b' );
    set( 'r', 't' );
    set( 'i', 'd' );
    set( 'b', 'h' );
    set( 't', 'w' );
    set( 'h', 'x' );
    set( 'w', 'f' );
    set( 'f', 'c' );
    set( 'a', 'y' );
    set( 'o', 'k' );
    set( 'z', 'q' );
    set( 'g', 'v' );
    set( 'q', 'z' );
    set( 'u', 'j' );

    scanf("%d\n",&T);
    for (int t = 1; t <= T; ++t) {
        gets(s);
        int len = strlen(s);

        printf("Case #%d: ",t);
        for (int i = 0; i < len; ++i) {
            if ( s[i] == ' ' ) printf(" ");
            else               printf("%c",c[ s[i]-'a' ]);
        }
        printf("\n");
    }

    return 0;
}
