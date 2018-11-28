#include <stdio.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std ;


int main()
{
    int i, j, k, l ;

    FILE *in = fopen("file.in", "r")  ;
    FILE *out = fopen("file.out", "w")  ;
    int T, N ;
    char c ;
    int board[105][105] ;
    double wp[105], owp[105], h, oowp ;
    int p, w ;

    fscanf(in, "%d\n", &T) ;

    for(l=1;l<=T;l++)
    {
        fscanf(in, "%d\n", &N) ;
        for(i=0;i<N;i++) for(j=0;j<N;j++) board[i][j] = -1 ;

        for(i=0;i<N;i++)
        {
            for(j=0;j<N;j++)
            {
                fscanf(in, "%c", &c) ;
                if( c == '1' ) board[i][j] = 1 ;
                if( c == '0' ) board[i][j] = 0 ;
            }
            fscanf(in, "\n") ;
        }

        for(i=0;i<N;i++)
        {
            p = 0 ;
            w = 0 ;
            for(j=0;j<N;j++)
            {
                if( board[i][j] == 1 ) p ++, w ++ ;
                if( board[i][j] == 0 ) p ++ ;
            }
            wp[i] = (double)w / (double) p ;
        }

        for(k=0;k<N;k++)
        {
            owp[k] = 0 ;
            h = 0 ;
            for(i=0;i<N;i++)
            {
                if( board[k][i] != -1 )
                {
                    h ++ ;
                    p = 0 ;
                    w = 0 ;
                    for(j=0;j<N;j++)
                    {
                        if( j == k ) continue ;
                        if( board[i][j] == 1 ) p ++, w ++ ;
                        if( board[i][j] == 0 ) p ++ ;
                    }
                    owp[k] += (double) w / (double) p ;
                }
            }
            owp[k] /= h ;
        }

        fprintf(out, "Case #%d:\n", l) ;
        for(i=0;i<N;i++)
        {
            k = 0 ;
            oowp = 0 ;
            for(j=0;j<N;j++)
                if( board[i][j] != -1 ) oowp += owp[j], k ++ ;
            oowp /= k ;
            h = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp ;
            fprintf(out, "%lf\n", h) ;
        }

    }

    return 0 ;
}
