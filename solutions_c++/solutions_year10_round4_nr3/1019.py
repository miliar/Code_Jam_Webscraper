#include <cstdio>
#include <cstring>

using namespace std;

int polje[110][110], temp[110][110];

void solve(){
    int r;
    scanf( "%d", &r );
    memset( polje, 0, sizeof(polje) );

    for( int i = 0; i < r; i++ ){
        int r1, r2, s1, s2;
        scanf( "%d %d %d %d", &s1, &r1, &s2, &r2 );
        for( int r = r1; r <= r2; r++ )
            for( int s = s1; s <= s2; s++ )
                polje[r][s] = 1;
    }

    int ret = 0;
    while(1){

        bool ima = 0;
        for( int i = 1; i <= 100; i++ )
            for( int j = 1; j <= 100; j++ )
                if( polje[i][j] ) ima = 1;
        if( !ima ) break;

        ret++;
        for( int i = 1; i <= 100; i++ ){
            for( int j = 1; j <= 100; j++ ){
                if( polje[i][j] && !polje[i-1][j] && !polje[i][j-1] ) temp[i][j] = 0;
                else if( !polje[i][j] && polje[i-1][j] && polje[i][j-1] ) temp[i][j] = 1;
                else temp[i][j] = polje[i][j];
            }
        }
        memcpy( polje, temp, sizeof(temp) );
    }

    printf( "%d", ret );

}

int main(){
    int t;
    scanf( "%d", &t );

    for( int T = 1; T <= t; T++ ){
        printf( "Case #%d: ", T);
        solve();
        printf( "\n");
    }
    return 0;
}
