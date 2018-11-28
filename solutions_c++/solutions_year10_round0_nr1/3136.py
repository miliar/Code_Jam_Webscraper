#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
    FILE * pp = fopen( "A-large.in" , "r" );
    FILE * fp = fopen( "a.out", "w" );
    int t,N,K;fscanf( pp, "%d",&t);
    for ( int i = 1 ; i <= t ; ++ i ) {
        fscanf( pp, "%d%d",&N,&K);
        if ( K == 0 ) {
             fprintf( fp, "Case #%d: OFF\n",i);
        }else {
            long long value = 1;
            for ( int j = 0 ; j < N ; ++ j )
                value = value<<1;
            if ( (K+1)%value == 0 )
               fprintf( fp, "Case #%d: ON\n",i);
            else
                fprintf( fp ,"Case #%d: OFF\n",i);
        }
    }
    system("pause");
    return 0;
}
