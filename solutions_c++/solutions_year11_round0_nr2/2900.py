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

    int T, C, D, N ;
    char com[30][30], opp[30][30], x, y, z ;
    string list ;

    fscanf(in, "%d\n", &T) ;
    for(l=1;l<=T;l++)
    {
        for(i=0;i<30;i++) for(j=0;j<30;j++) com[i][j] = 0 , opp[i][j] = 0 ;
        list.clear() ;

        fscanf(in, "%d", &C) ;
        for(i=0;i<C;i++)
        {
            fscanf(in, " %c%c%c", &x, &y, &z) ;
            com[x-'A'][y-'A'] = z ; // combine
            com[y-'A'][x-'A'] = z ;
        }

        fscanf(in, " %d", &D) ;
        for(i=0;i<D;i++)
        {
            fscanf(in, " %c%c", &x, &y) ;
            opp[x-'A'][y-'A'] = 1 ; // opposite
            opp[y-'A'][x-'A'] = 1 ;
        }

        fscanf(in, " %d ", &N) ;
        for(i=0;i<N;i++)
        {
            fscanf(in, "%c", &x) ;

            if( list.size() )
            {
                y = list[list.size()-1] ;
                if( com[x-'A'][y-'A'] )
                {
                    list.resize(list.size()-1) ;
                    x = com[x-'A'][y-'A'] ;
                }
            }
            list += x ;

            for(j=0;j<list.size();j++)
            {
                if( opp[x-'A'][list[j]-'A'] ) list.clear() ;
            }
        }

        fscanf(in, "\n") ;
        fprintf(out, "Case #%d: [", l) ;
        if( list.size() ) fprintf(out, "%c", list[0]) ;
        for(i=1;i<list.size();i++) fprintf(out, ", %c", list[i]) ;
        fprintf(out, "]\n") ;
    }

    return 0 ;
}
