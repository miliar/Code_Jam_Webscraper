#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <math.h>

using namespace std;


int main(){

    freopen("A-large.IN", "r", stdin );
    freopen("sol.txt", "w", stdout );

    int t;
    scanf("%d", &t );

    for(int test = 1; test <= t; ++test ){

        int n;
        scanf("%d", &n );

        int diff, move_o = 0, move_p = 0;
        int pos_o = 1, pos_p = 1, sol = 0, x;

        for(int i = 0; i < n; ++i ){
            char c;
            while(  !isalpha(c = getchar() ) );

            scanf("%d", &x );
            if( c == 'O' ){
                diff = abs( pos_o - x );
                diff = max( diff - move_o, 0 ) + 1;
                move_p += diff, move_o = 0;
                pos_o = x;
                sol    += diff;
            }else{
                diff = abs( pos_p - x );
                diff = max( diff - move_p, 0 ) + 1;
                move_o += diff, move_p = 0;
                pos_p = x;
                sol    += diff;
            }
        }

        printf("Case #%d: %d\n",test, sol );
    }

    return 0;
}
