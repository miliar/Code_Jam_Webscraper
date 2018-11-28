#include<iostream>
#include<string>

using namespace std;

char a[256];

void init( void ){
    a[ 'a' ] = 'y';
    a[ 'b' ] = 'h';
    a[ 'c' ] = 'e';
    a[ 'd' ] = 's';
    a[ 'e' ] = 'o';
    a[ 'f' ] = 'c';
    a[ 'g' ] = 'v';
    a[ 'h' ] = 'x';
    a[ 'i' ] = 'd';
    a[ 'j' ] = 'u';
    a[ 'k' ] = 'i';
    a[ 'l' ] = 'g';
    a[ 'm' ] = 'l';
    a[ 'n' ] = 'b';
    a[ 'o' ] = 'k';
    a[ 'p' ] = 'r';
    a[ 'q' ] = 'z';
    a[ 'r' ] = 't';
    a[ 's' ] = 'n';
    a[ 't' ] = 'w';
    a[ 'u' ] = 'j';
    a[ 'v' ] = 'p';
    a[ 'w' ] = 'f';
    a[ 'x' ] = 'm';
    a[ 'y' ] = 'a';
    a[ 'z' ] = 'q';
    a[ ' ' ] = ' ';
}

int main(void){
    freopen("in","r",stdin);
    freopen("out.txt","w",stdout);
    char s[1000];
    int T;
    init();
    scanf("%d",&T);
    getchar();
    for( int c = 1; c <= T; c++ ){
        gets(s);
        printf("Case #%d: ", c );
        for( int j = 0; s[j]; j++ )
            putchar( a[ s[j] ] );
        puts("");
    }
    //system("pause");
    return 0;
}
