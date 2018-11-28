#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_N 201
#define MAX_LEN 201

struct T
{
    double v;
    char fe[100];
    int lc;
    int rc;
    int flag;
};
char s[MAX_N][MAX_LEN];
char a[MAX_N*MAX_LEN];
int t;
int n;
int ind;
int ind0;
T tree[100000];
int pos;
double res;
int m;

void Get( int r )
{
    double m = 1;
    double re = 0;
    int p = 0;
    ++pos;
    if( a[pos] == '1' ) re = 1;
    pos += 2;
    while( a[pos] >= '0' && a[pos] <= '9' )
        re = re * 10 + a[pos] - '0', m *= 10, pos++;
    tree[r].v = re / m;
    if( a[pos] != ')' )
    {
        while( a[pos] != '(' ) tree[r].fe[p++] = a[pos++];
        tree[r].fe[p] = 0;
        tree[r].lc = ++ind;
        Get( ind );
        tree[r].rc = ++ind;
        Get( ind );
        ++pos;
    }
    else tree[r].flag = 1, ++pos;
}

void Show( int i )
{
    if( !tree[i].flag )
    {    
         printf( "%lf %s\n", tree[i].v, tree[i].fe );
         Show( tree[i].lc );
         Show( tree[i].rc );
    }
    else
    {
        printf( "%lf\n", tree[i].v );   
    }
}

void Solve( int r )
{
    res *= tree[r].v;
    if( !tree[r].flag )
    {
        for( int i = 0; i < m; ++i )
            if( strcmp( tree[r].fe, s[i] ) == 0 )
            {
                Solve( tree[r].lc );
                return ;
            }
        Solve( tree[r].rc );
    }
}
int main( )
{
    freopen( "in.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d\n", &t );
    for( int i = 1; i <= t; ++i )
    {
         memset( tree, 0, sizeof( tree ) );
         ind = 0;
         ind0 = 0;
         pos = 0;
         scanf( "%d\n", &n );
         for( int i = 0; i < n; ++i )
             gets( s[i] );
         for( int i = 0; i < n; ++i )
             for( int j = 0; s[i][j]; ++j )
                 if( s[i][j] != ' ' && s[i][j] != '\n' ) a[ind0++] = s[i][j];
         a[ind0] = 0;
         Get( 0 );
         scanf( "%d", &n );
         printf( "Case #%d:\n", i );
         for( int j = 0; j < n; ++j )
         {
             scanf( "%s %d", s[0], &m );
             res = 1;
             for( int k = 0; k < m; ++k )
                 scanf( "%s", s[k] );
             Solve( 0 );
             printf( "%lf\n", res );
         }
    }
}
