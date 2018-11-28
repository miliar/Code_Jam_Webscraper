#include <iostream>
using namespace std;
const int maxl = 60;
int a[1010][maxl];
int gcd[maxl];
int ci, cn, i, j, k, n;
char s[maxl];
int ls;

void sub( int a[maxl], int b[maxl] )
{
    int i;
    for ( i = 0; i < maxl; i++ )
    {
        a[i] = a[i]-b[i];
        while ( a[i] < 0 )
        {
            a[i+1]--;
            a[i] += 10;
        }
    }
}

bool zero( int a[maxl] )
{
    int i;
    for ( i = 0; i < maxl; i++ )
    if ( a[i] != 0 ) return 0;
    return 1;
}

void mod( int a[maxl], int b[maxl] )
{
    int la, lb, i, j, flag;
    la = maxl-1;
    while ( a[la] == 0 ) la--;
    lb = maxl-1;
    while ( b[lb] == 0 ) lb--;
    for ( i = la; i >= lb; i-- )
    {
        while (1)
        {
            flag = 1;
            for ( j = 0; j <= lb; j++ )
            if ( a[i-j] > b[lb-j] ) break;
            else if ( a[i-j] < b[lb-j] )
            {
                flag = 0;
                break;
            }
            if ( flag == 0 ) break;
            for ( j = lb; j >= 0; j-- )
            {
                a[i-j] = a[i-j]-b[lb-j];
                while ( a[i-j] < 0 )
                {
                    a[i-j+1]--;
                    a[i-j] += 10;
                }
            }
        }
        if ( i > lb )
        {
            a[i-1] += a[i]*10;
            a[i] = 0;
        }
    }
}

void work( int a[maxl], int b[maxl] )
{
    int c[maxl];
    int j;
    while ( !zero(b) )
    {
        mod( a, b );
        memcpy( c, a, sizeof(c) );
        memcpy( a, b, sizeof(c) );
        memcpy( b, c, sizeof(c) );
    }
}

bool small( int a[maxl], int b[maxl] )
{
    int la, lb;
    la = maxl-1;
    while ( a[la] == 0 ) la--;
    lb = maxl-1;
    while ( b[lb] == 0 ) lb--;
    if ( la < lb ) return 1;
    if ( la > lb ) return 0;
    while ( la > 0 )
    {
        if ( a[la] != b[la] ) break;
        la--;
    }
    if ( a[la] < b[la] ) return 1;
    return 0;
}

int main()
{
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    scanf( "%d", &cn );
    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d", &n );
        memset( a, 0, sizeof(a) );
        for ( i = 0; i < n; i++ )
        {
            scanf( "%s", &s );
            ls = strlen(s);
            for ( j = 0; j < ls; j++ ) a[i][j] = s[ls-j-1]-'0';
        }
        k = 0;
        for ( i = 1; i < n; i++ )
        if ( small( a[i], a[k] ) ) k = i;
        for ( i = 0; i < n; i++ )
        if ( i != k ) sub( a[i], a[k] );
        if ( k == 0 ) i = 1;
        else i = 0;
        memcpy( gcd, a[i], sizeof(gcd) );
        for ( i++; i < n; i++ )
        if ( i != k )
        {
            work( gcd, a[i] );
        }
        mod( a[k], gcd );
        printf( "Case #%d: ", ci );
        if ( zero(a[k]) ) printf( "0\n" );
        else
        {
            sub( gcd, a[k] );
            i = maxl-1;
            while ( gcd[i] == 0 ) i--;
            for ( ; i >= 0; i-- ) printf( "%d", gcd[i] );
            printf( "\n" );
        }
    }
    return 0;
}
