#include <stdio.h>

#include <iostream>
#include <string>
#include <vector>

using namespace std ;

struct node
{
    int ind ;
    char col ;
};

int abs(int a)
{
    return a < 0 ? a*-1 : a ;
}

int main()
{
    int i, j, k, l ;
    int T, N, s, t, p, u ;
    node h ;
    vector <node> seq ;
    vector <int> orange, blue ;

    FILE *in = fopen("file.in", "r") ;
    FILE *out = fopen("file.out", "w") ;

    fscanf(in, "%d\n", &T) ;

    for(l=1;l<=T;l++)
    {
        fscanf(in, "%d", &N) ;
        seq.clear() ;
        orange.clear() ;
        blue.clear() ;

        for(i=0;i<N;i++)
        {
            fscanf(in, " %c %d", &h.col, &h.ind) ;
            seq.push_back(h) ;
            if( h.col == 'O' ) orange.push_back(h.ind) ;
            else blue.push_back(h.ind) ;
        }
        fscanf(in, "\n") ;

        i = 0 ;
        j = 0 ;
        k = 1 ;
        t = 1 ;
        s = 0 ;
        p = 0 ;
        while(1)
        {
            if( p >= seq.size() ) break ;
            s ++ ;
            u = 0 ;

            if( seq[p].col == 'O' && seq[p].ind == k) i ++, u = 1 ;
            else
                if( orange[i] != k && i < orange.size() )
                k += (orange[i] - k) / abs(orange[i] - k) ;

            if( seq[p].col == 'B' && seq[p].ind == t) j ++, u = 1 ;
            else
                if( blue[j] != t && j < blue.size() )
                t += (blue[j] - t) / abs(blue[j] - t) ;

            if( u ) p ++ ;
        }
        fprintf(out, "Case #%d: %d\n", l, s) ;
    }

    return 0 ;
}
