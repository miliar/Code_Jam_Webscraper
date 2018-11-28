#include <iostream>

enum { MAXSIZE=500, PATTERNSIZE=19 };


long match( char* input, char* pattern ){
    int isize = strlen(input)-1; //ignore \n
    int psize = PATTERNSIZE;

    long map[PATTERNSIZE+1][MAXSIZE+1];
    for(int i=0;i<=psize;++i) map[i][0] = 0;
    for(int i=0;i<=isize;++i) map[0][i] = 1;

    //printf("p=%d i=%d\n", psize, isize);

    //dp
    for(int i=1;i<=psize; ++i){
        for(int j=1;j<=isize; ++j){
            if( pattern[i]==input[j] )
                map[i][j] = map[i-1][j-1] + map[i][j-1];
            else
                map[i][j] = map[i][j-1];
        }
    }
    /*
    for(int y=0;y<=psize;++y){
        for(int x=0;x<=isize;++x){
            printf("%ld ", map[y][x] );
        }
        printf("\n");
    }*/
    return map[psize][isize];
}

int main(){

    freopen("C-small-attempt0.in", "r", stdin );
    freopen("C-small.out", "w", stdout );

    char pattern[] = " welcome to code jam";

    int numCase;
    scanf("%d ", &numCase);

    for(int k=1; k<=numCase; ++k ){

        char input[MAXSIZE+5];
        input[0] = ' ';
        fgets( input+1, sizeof(input), stdin); //第一格留白

        long result = match( input, pattern );

        printf("Case #%d: %04d\n", k, result%10000);
    }
    return 0;
}
