#include<iostream>
#include<cstdlib>

using namespace std;

int g[ 1001 ];

FILE *pp = fopen( "C-small-attempt4.in", "r" );
FILE *fp = fopen( "a.out" , "w" );

int main()
{
    int T,R,K,N;
    fscanf( pp,"%d",&T);
    for ( int i = 1 ; i <= T ; ++ i ){
        fscanf( pp,"%d%d%d",&R,&K,&N);
        for ( int j = 0 ; j < N ; ++ j )
            fscanf( pp,"%d",&g[ j ]);
        int sum = 0,add = 0,move = 0,count = 0;
        for ( int j = 0 ; j < R ; ++ j ) {
            while ( add + g[ move ] <= K && count < N ) {
                  add += g[ move ];
                  move = ( ++ move )%N;
                  ++ count;
            }
            count = 0;
            sum += add;add = 0;
        }
        fprintf( fp,"Case #%d: %d\n",i,sum);
    }
    fclose( fp );
    fclose( pp );
    return 0;
}
