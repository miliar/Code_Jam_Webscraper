#include <stdio.h>
#include <string.h>
#include <ctype.h>

char a[]= "yhesocvxduiglbkrztnwjpfmaq";


int main() {
    int n , i , j;
    char s[100000];
    while( scanf("%d\n",&n) != EOF ) {
        for( i = 0 ; i < n;i++ ) {
            gets( s );
            printf("Case #%d: ",i+1);
            for( j = 0 ; j < strlen(s);j++ ){
                if( islower( s[j] ) ) putchar(a[s[j]-'a']);
                else putchar( s[j] );
            }
            puts("");
        }
    }
    return 0;
}
