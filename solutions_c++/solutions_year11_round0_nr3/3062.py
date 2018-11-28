#include <stdio.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std ;


int main()
{
    int i, j, k, l ;
    FILE *in = fopen("file.in", "r") ;
    FILE *out = fopen("file.out", "w") ;
    int T, N, seq[20], a, b, a1, b1 ;

    fscanf(in, "%d", &T) ;
    for(l=1;l<=T;l++)
    {
        fscanf(in, "%d", &N) ;
        for(i=0;i<N;i++)
            fscanf(in, "%d", &seq[i]) ;
        k = 0 ;

        for(i=1;i<=1<<N;i++)
        {
            a = -1 ;
            b = -1 ;
            a1 = 0 ;
            b1 = 0 ;
            for(j=0;j<N;j++)
            {
                if( i & (1<<j) )
                {
                       if( a == -1 ) a = seq[j] ;
                       else a = a^seq[j] ;
                       a1 += seq[j] ;
                }
                else
                {
                    if( b == -1 ) b = seq[j] ;
                    else b = b^seq[j] ;
                    b1 += seq[j] ;
                }
            }

            if( a == b )
            {
                a1 = a1 > b1 ? a1 : b1 ;
                k = k > a1 ? k : a1 ;
            }
        }
        fprintf(out, "Case #%d: ", l) ;
        if( k == 0 ) fprintf(out, "NO\n") ;
        else fprintf(out, "%d\n", k) ;
    }


    return 0 ;
}
