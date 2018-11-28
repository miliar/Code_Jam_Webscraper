//#include <cstdlib>
#include <iostream>
//#include <stdio.h>
//#include <stdlib.h>

using namespace std;

#define BUFOR_LIMIT 2000

char *PATTERN = "welcome to code jam\0";
int PatLen = 0;
int bfrlen = 0;
int No = 0;
int Ilosc[ 20 ][ BUFOR_LIMIT ];

inline int SubWelcome( int row , int pos )
{
       if( bfrlen - PatLen + row < pos )
           return 0;
       int ret = 0;
       int Next = Ilosc[ row ][ pos ];
       if( Next > -1 )
           ret += SubWelcome( row , Next );
       if( row + 1 == PatLen )
           return ++ret;
       int NextRow = Ilosc[ row + 1 ][ pos ];
       if( NextRow > -1 )
           ret += SubWelcome( row + 1 , NextRow );
       ret = ret % 10000;
       return ret;
}

inline int WelcomeF( char *bfr )
{
       bfrlen = strlen( bfr );
       for( int i = 0 ; i < PatLen ; i++ )
            for( int j = 0 ; j < bfrlen ; j++ )
                 Ilosc[ i ][ j ] = ( PATTERN[ i ] == bfr[ j ] );
       for( int i = 0 ; i < PatLen ; i++ )
       {
            int last = -1;
            for( int j = bfrlen - 1 ; j > -1 ; j-- )
            {
                 int tmp = Ilosc[ i ][ j ];
                 Ilosc[ i ][ j ] = last;
                 if( tmp )
                     last = j;
            }
       }
       if( Ilosc[0][0] < 0 )
           return 0;
       return SubWelcome( 0 , Ilosc[0][0] );
}

inline int Welcome( char *str , int pos )
{
    if( ( str = strchr( str , PATTERN[ pos ] ) ) == NULL )
        return 0;
    int res = 0;
    while( str != NULL )
    {
           if( pos + 1 < PatLen )
               res += Welcome( str + 1 , pos + 1 );
           else
               res += 1;
           str = strchr( str + 1 , PATTERN[ pos ] );
    }
    res = res % 10000;
    return res;
}

int main(int argc, char *argv[])
{
    PatLen = strlen( PATTERN );
    FILE *pFile;
    FILE *OutFile;
    pFile = fopen("C-small.in","r");
    int Type = 0;
    if(pFile==NULL)
      pFile = fopen("C-large.in","r");
    else
    {
        Type = 1;
        OutFile = fopen("C-small.out","w");
        if( OutFile == NULL )
            return 0;
    }    
    if(pFile==NULL)
      return 0;
    else if( Type != 1 )
    {
        Type = 2;
        OutFile = fopen("C-large.out","w");
        if( OutFile == NULL )
            return 0;
    }
    char *bfr;
    size_t size = sizeof(char)*BUFOR_LIMIT;
    bfr = (char*)malloc(size);
    int WasT = 0;
    int l = 0;
    while( fgets( bfr , BUFOR_LIMIT , pFile ) != NULL )
    {
           if( !WasT )
           {
               WasT = 1;
               No = atoi( bfr );
           }
           else
           {
               char tmpBfr[BUFOR_LIMIT+1];
               tmpBfr[0]='X';
               strcpy( tmpBfr + 1 , bfr );
               int ans = WelcomeF(tmpBfr);
               l++;
               fprintf( OutFile , "Case #%d: %.4d\n" , l , ans );
               cout<<"\n"<<l;
           }
    }
    fclose( OutFile );
    fclose(pFile);
    free(bfr);
    return 0;
}
