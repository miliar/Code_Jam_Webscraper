#include <iostream>
#include <cstring>

#define SIZE 19

void recurrence( char *S, char *T, int j, int i, int size, int &repe );

int main()
{
    freopen("in", "r", stdin );
    freopen("out", "w", stdout );
    int n, t = 0;
    scanf("%d", &n );
    char S[510];
    char T[] = { "welcome to code jam" };
    getchar();
    while( n > t++ )
    {
        char a;
        int i = 0;
        while( (a=getchar()) != '\n' )
            S[i++] = a;
        S[i] = '\0';
        int repes = 0;
        recurrence( S, T, 0, 0, i, repes );
        if( repes < 10 )
            printf("Case #%d: 000%d\n", t, repes );
        else if( repes < 100 )
            printf("Case #%d: 00%d\n", t, repes );
        else if( repes < 1000 )
            printf("Case #%d: 0%d\n", t, repes );
        else
            printf("Case #%d: %d\n", t, repes );
    }
    return 0;
}

/*
    find T in S, a character at a time, current character to search in S is T[i]
    we are at position j in S, size of S is size
    repe is the times it is found modulus 10000
*/
void recurrence( char *S, char *T, int j, int i, int size, int &repe )
{
    if( i == SIZE )
    {
        repe = ( repe + 1 ) % 10000;
        return;
    }
    while( j < size )
    {
        if( S[j] == T[i] )
            recurrence( S, T, j+1, i+1, size, repe );
        ++j;
    }
}
