#include<iostream>
#include<stdio.h>
#include<cstring>
int main() {
    char G[110], c , X[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'} ;
    int i, n, T, j, ch ;
    FILE *fin , *fout ;
    fin = fopen("A-small-attempt0.in","r") ;
    fout = fopen("op1.txt","w") ;
    fscanf(fin,"%d",&T);
    fscanf(fin,"%c",&c);
    for ( i = 1 ; i <= T ; ++i ) {
        fscanf(fin,"%[^\n]s",G);
        fscanf(fin,"%c",&c);
        printf("%s\n",G);
        n = strlen(G) ;
        fprintf(fout,"Case #%d: ",i) ;
        for ( j = 0 ; j < n ; ++j ) {
            ch = G[j] - 97 ;
            if ( 0 <= ch )
                fprintf(fout,"%c",X[ch]) ;
            else
                fprintf(fout,"%c",G[j]) ;
        }
        fprintf(fout,"\n") ;
    }
    fclose(fin);
    fclose(fout);
    return 0;
}

