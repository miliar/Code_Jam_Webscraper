
#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std ;

FILE *in = fopen("hold.in", "r") ;
FILE *out = fopen("hold.out", "w") ;


int main()
{
    int i, j, k, l ;
    char c ;
    string str ;

    str = "ynficwlbkuomxsevzpdrjgthaq" ;
    fscanf(in, "%d\n", &k) ;
    for(l=1;l<=k;l++)
    {
        fprintf(out, "Case #%d: ", l) ;
        while(1)
        {
            fscanf(in, "%c", &c) ;
            if( c == '\n' ) break ;
            if( c != ' ' )
            {
                j = 0 ;
                while( str[j] != c ) j ++ ;
                c = j+'a' ;
            }
            fprintf(out, "%c", c) ;
        }
        fprintf(out, "\n") ;
    }

    return 0 ;
}
