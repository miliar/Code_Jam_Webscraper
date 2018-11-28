#include <iostream>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <cstdio>
#include <stack>
#include <map>
#include <queue>
#include <string>
#include <string.h>
#include <set>
using namespace std;

int n;
int mx[305][305];


int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
    int tests;
    scanf("%d",&tests);

    for( int t = 1; t <= tests; ++t ){

        memset( mx , 0 , sizeof(mx));

        scanf("%d",&n);
        for( int i = 0; i < n; ++i ){
            int x1,y1,x2,y2;
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);

            for( int x = x1; x <= x2; ++x ){
                for( int y = y1; y <= y2; ++y )
                    mx[y][x] = 1;
            }

        }


        int sec = 0;
        bool ok = true;
        while( ok ){
            ok = false;

            for( int x = 300; x >= 0; --x ){
                for( int y = 300; y >= 0; --y ){
                    if( mx[y][x] == 1 && mx[y-1][x] == 0 && mx[y][x-1] == 0 )
                        mx[y][x] = 0;
                    else if( mx[y][x] == 0 && mx[y-1][x] && mx[y][x-1] )
                        mx[y][x] = 1;

                    if( mx[y][x] == 1 ) ok = true;
                }
            }

            sec ++;
        }

        printf("Case #%d: %d\n",t,sec);

    }


    return 0;
}
