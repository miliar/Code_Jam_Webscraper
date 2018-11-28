/*
TASK: Fair Warning
LANG: C++
AUTHOR: Yordan Chaparov
*/

#include <iostream>
#include <cstring>
using namespace std;

int C, n;
int t[1024];
int d;
int raz[1000020];
int len[1024];

bool sravn( char a[], char b[] ) // 1 -> a < b; 0 -> a > b
{
    if ( strlen( a ) == strlen( b ) )
    {
        int i = 0;
        while ( i < strlen( a ) )
        {
            if ( a[i] != b[i] )
                return a[i] < b[i];
            i++;
        }
    }
    return strlen( a ) < strlen( b );
}

void izv( char a[], char b[], char c[] ) //a-b = c;
{
    int i, j, k;
    char pr = 0;
    int la = strlen( a ), lb = strlen( b );
    char x[64];

    i = la-1;
    j = lb-1;
    x[la] = '\0';
    while ( j >= 0 )
    {
        x[i] = a[i] - b[j] - pr + '0';
        if ( x[i] < '0' )
        {
            x[i] = x[i] + 10;
            pr = 1;
        }
        else pr = 0;
//        cout << "XX " << i << " " << x[i] << endl;
        i--;
        j--;
    }
    while ( i >= 0 )
    {
        x[i] = a[i] - pr;
        if ( x[i] < '0' )
        {
            x[i] = x[i] + 10;
            pr = 1;
        }
        else pr = 1;
//        cout << "XX " << i << " " << x[i] << endl;
        i--;
    }
//    cout << x << endl;

    k = 0;
    i = 0;
    while ( x[k] == '0' )
        k++;
    if ( x[k] == '\0' )
    {
        c[i] = '0';
        i++;
    }
    while ( x[k] != '\0' )
    {
        c[i] = x[k];
        i++;
        k++;
    }
    c[i] = '\0';
//    cout << "RAZ " << i << " " << c[0] << " " << c[1] << " " << c[2] << " " << c << endl;
}

int nod( int a, int b )
{
    if ( b == 0 )
        return a;
    return nod( b, a%b );
}

int main()
{
    int i, j, k;
    int x;

    scanf( "%d", &C );
    for ( int ii = 1; ii <= C; ii++ )
    {
        scanf( "%d", &n );
        for ( i = 1; i <= n; i++ )
        {
            scanf( "%d", &t[i] );
//            cout << t[i] << endl;
        }

        k = 0;
        for ( i = 1; i <= n; i++ )
        {
            for ( j = i+1; j <= n; j++ )
            {
                k++;
                if ( t[i] < t[j] )
                    raz[k] = t[j] - t[i];
                else
                    raz[k] = t[i] - t[j];
            }
        }
        d = raz[1];
        for ( i = 2; i <= k; i++ )
        {
            x = nod( d, raz[i] );
            d = x;
        }
        t[2] = t[1];
        while ( d < t[1] )
        {
            x = t[1] - d;
            t[1] = x;
        }
        t[2] = d - t[1];
        printf( "Case #%d: %d\n", ii, t[2] );
    }
    return 0;
}
