#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define smallL 10
#define smallD 25
#define smallN 10
#define largeL 15
#define largeD 5000
#define largeN 500

char Dictionary[largeD][largeL+1];
int MaxL = 0;
int MaxD = 0;
int MaxN = 0;  
int L = 0, N = 0, D = 0;

int CheckStr( char *bfr )
{
    int MaxPos = 50;
    int end = 0;
    char posC[L][ MaxPos ];
    char *newBfr = bfr;
    int p = 0;
    for( int l = 0 ; l < L ; l++ )
    {
         int no = 0;
         if( bfr[p] == '(' )
         {
            while( bfr[++p] != ')' )
              posC[l][no++] = bfr[p];
         }
         else
             posC[l][no++] = bfr[p];
         p++;
         newBfr = newBfr + p;
         posC[l][no] = 0;
    }
    int ret = 0;
    for( int d = 0 ; d < D ; d++ )
    {
      int Ok = 1;
      for( int l = 0 ; l < L && Ok ; l++ )
      {
           int OkPos = 0;
           int no = 0;
           while( !OkPos && posC[l][no] != 0 )
           {
              if( posC[l][no++] == Dictionary[d][l] )
                 OkPos = 1;
           }
           if( !OkPos )
               Ok = 0;
      }
      if( Ok )
          ret++;
    }
    return ret;
}

int main(int argc, char *argv[])
{
    FILE *pFile;
    FILE *OutFile;
    pFile = fopen("A-small.in","r");
    int Type = 0;
    if(pFile==NULL)
      pFile = fopen("A-large.in","r");
    else
    {
        Type = 1;
        OutFile = fopen("A-small.out","w");
        if( OutFile == NULL )
            return 0;
    }    
    if(pFile==NULL)
      return 0;
    else if( Type != 1 )
    {
        Type = 2;
        OutFile = fopen("A-large.out","w");
        if( OutFile == NULL )
            return 0;
    }
    MaxL = ( Type == 1 ) ? smallL : largeL;
    MaxD = ( Type == 1 ) ? smallD : largeD;
    MaxN = ( Type == 1 ) ? smallN : largeN;  
    char *bfr;
    bfr = (char*)malloc(sizeof(char)*MaxL*60);
    int Line = 0;
    while( fgets( bfr , MaxL*60 , pFile ) != NULL )
    {
           Line++;
           if( Line == 1 )
           {
                      int p = 0;
                      L = atoi( bfr );
                      while( bfr[p] != ' ' && bfr[p] != 0 )
                             p++;
                      D = atoi( bfr + p );
                      p++;
                      while( bfr[p] != 0 && bfr[p] != ' ' )
                             p++;
                      N = atoi( bfr + p );
           }
           else if( Line <= 1 + D )
           {
                strcpy( Dictionary[Line-2] , bfr );
                Dictionary[Line-2][strlen( Dictionary[Line-2] )-1]=0;
           }
           else
           {
               char resbfr[ 100 ];
               strcpy( resbfr , "Case #" );
               char no[20];
               itoa( Line-D-1 , no , 10 );
               strcpy( resbfr + strlen( resbfr ) , no );
               strcat( resbfr + strlen( resbfr ) , ": " );
               itoa( CheckStr( bfr ) , no , 10 );
               strcat( resbfr + strlen( resbfr ) , no );
               strcat( resbfr + strlen( resbfr ) , "\n" );               
               fputs( resbfr , OutFile  );
           }
    }
    fclose( OutFile );
    fclose(pFile);
    free(bfr);
    return 0;
}
