#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define maxT 110
#define maxH 110
#define maxW 110
#define MAXALT 999999999;

int T = 0;
int H = 0;
int W = 0;
char CurrB = 'a';

int Map[maxH][maxW];
char Res[maxH][maxW];

char GetWater( int h , int w )
{
     if( Res[h][w] != 0 )
         return Res[h][w];
     int MyAlt = Map[h][w];
     int MAX = MAXALT;
     int NAlt = ( h > 0 ) ? Map[h-1][w] : MAX;
     int WAlt = ( w > 0 ) ? Map[h][w-1] : MAX;
     int EAlt = ( w < W - 1 ) ? Map[h][w+1] : MAX;
     int SAlt = ( h < H - 1 ) ? Map[h+1][w] : MAX;
     int MinAlt = MyAlt;
     char dir = 'I';
     if( MinAlt > NAlt )
     {
         dir = 'N';
         MinAlt = NAlt;
     }
     if( MinAlt > WAlt )
     {
         dir = 'W';
         MinAlt = WAlt;
     }
     if( MinAlt > EAlt )
     {
         dir = 'E';
         MinAlt = EAlt;
     }
     if( MinAlt > SAlt )
     {
         dir = 'S';
         MinAlt = SAlt;
     }
     if( dir == 'I' )
     {
         Res[h][w] = CurrB;
         CurrB++;
     }
     else if( dir == 'N' )
         Res[h][w] = GetWater(h-1,w);
     else if( dir == 'W' )
         Res[h][w] = GetWater(h,w-1);
     else if( dir == 'E' )
         Res[h][w] = GetWater(h,w+1);
     else if( dir == 'S' )
         Res[h][w] = GetWater(h+1,w);
     return Res[h][w];
}

int main(int argc, char *argv[])
{
    FILE *pFile;
    FILE *OutFile;
    pFile = fopen("B-small.in","r");
    int Type = 0;
    if(pFile==NULL)
      pFile = fopen("B-large.in","r");
    else
    {
        Type = 1;
        OutFile = fopen("B-small.out","w");
        if( OutFile == NULL )
            return 0;
    }    
    if(pFile==NULL)
      return 0;
    else if( Type != 1 )
    {
        Type = 2;
        OutFile = fopen("B-large.out","w");
        if( OutFile == NULL )
            return 0;
    }
    char *bfr;
    size_t size = sizeof(char)*maxW*900;
    bfr = (char*)malloc(size);
    int WasT = 0;
    int WasHead = 0;
    int CurrH = 0, CurrW = 0, CurrT = 0;
    while( fgets( bfr , size , pFile ) != NULL )
    {
           if( !WasT )
           {
               WasHead = 0;
               WasT = 1;
               T = atoi( bfr );
           }
           else if( !WasHead )
           {
                CurrT++;
                WasHead = 1;
                CurrB = 'a';
                int p = 0;
                H = atoi( bfr );
                while( bfr[p] != ' ' && bfr[p] != 0 )
                   p++;
                W = atoi( bfr + p );
                CurrH = 0;
                CurrW = 0;
           }
           else
           {
               Map[ CurrH ][ 0 ] = atoi( bfr );
               for( int i = 1 ; i < W ; i++ )
               {
                    while( *bfr != ' ' )
                    {
                           bfr++;
                    }
                    Map[ CurrH ][ i ] = atoi( ++bfr );
               }
               CurrH++;
               if( CurrH == H )
               {
                   WasHead = 0;
                   for( int i = 0 ; i < H ; i++ )
                   {
                        for( int j = 0 ; j < W ; j++ )
                           Res[i][j] = 0;
                   }
                   for( int i = 0 ; i < H ; i++ )
                   {
                        for( int j = 0 ; j < W ; j++ )
                             if( Res[i][j] == 0 )
                                 Res[i][j] = GetWater( i , j );
                   }
                   char res[size];
                   res[0]=0;
                   strcpy( res , "Case #" );
                   char no[20];
                   itoa( CurrT , no , 10 );
                   strcpy( res + strlen( res ) , no );
                   strcpy( res + strlen( res ) , ":\n" );
                   for( int i = 0 ; i < H ; i++ )
                   {
                        for( int j = 0 ; j < W ; j++ )
                        {
                             int pos = strlen( res );
                             if( j > 0 )
                                 strcpy( res + pos++ , " " );
                             res[ pos ] = Res[i][j];
                             res[ pos+1 ] = 0;
                        }
                        strcpy( res + strlen( res ) , "\n" );
                   }
                   fputs( res , OutFile );
               }
           }
    }
    fclose( OutFile );
    fclose(pFile);
    free(bfr);
    return 0;
}
