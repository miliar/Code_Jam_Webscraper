#include<iostream>
#include<string.h>
#define MAX 5000
using namespace std;

char dir[MAX + 5][20];
bool flag[20][30];
int l, d, n;
char tmp[MAX];

int main( ){
    int i, j, ans, len, k, flag_n;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
    while( scanf( "%d %d %d", &l, &d, &n ) != EOF ){
        for( i = 0; i < d; i++ )
            scanf( "%s", &dir[i] );
        bool f;
        for( i = 1; i <= n; i++ ){
            scanf( "%s", &tmp );
            len = strlen( tmp );
            f = false;
            ans = 0;
            flag_n = 0;
            memset( flag, false, sizeof( flag ) );
            for( j = 0; j < len; j++ ){
                if( tmp[j] == '(' )
                    f = true;
                else if( tmp[j] == ')' ){
                    f = false;
                    flag_n++;
                }else{
                    if( f ) flag[flag_n][tmp[j]-'a'] = true;
                    else{
						flag[flag_n][tmp[j]-'a'] = true;
						flag_n++;	
					}
                }
            }
            for( j = 0; j < d; j++ ){
                len = strlen( dir[j] );
                for( k = 0; k < len; k++ )
                    if( !flag[k][dir[j][k]-'a'] ) break;
                if( k == len ) ans++;
            }
            printf( "Case #%d: %d\n", i, ans );
        }
    }
    return 0;
}
