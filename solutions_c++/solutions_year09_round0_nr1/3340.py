#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct elem {
        char c;
        struct elem *jos,*urm;
}nod;

char a[5002][20];
int l,d,n;
nod *q, *q1, *root;

int verif ( char s[] )
{
 int p = 0, k = 0;


 root = NULL;
 q = NULL; q1 = NULL;
 for ( int i = 0; i < strlen( s ); i ++ )
    {
            if ( s[i] == '(' )
             {
                 p ++;
                 if( root == NULL )
                  {
                   q = (nod *) malloc (sizeof(nod));
                   root = q;
                   q1 = q;
                   q1->urm = NULL;
                   q1->jos = NULL;
                  }
                  else
                  {
                    q->urm = (nod *) malloc (sizeof(nod));
                    q = q->urm;
                    q->jos = NULL;
                    q->urm = NULL;
                    q1=q;
                  }
             }
            else
            if ( s[i] == ')' ) p --;
            else
            if ( p == 0 )
             {
                    if( root == NULL )
                  {
                   q = (nod *) malloc (sizeof(nod));
                   root = q;
                   q1 = q;
                   q1->c = s[i];
                   q1->urm = NULL;
                   q1->jos = NULL;
                  }
                   else
                   {
                    q->urm = (nod *) malloc (sizeof(nod));
                    q = q->urm;
                    q->c = s[i];
                    q->jos = NULL;
                    q->urm = NULL;
                    q1= q;
                   }
             }
            else
            if ( p == 1 )
                {
                    q1->jos =(nod *) malloc (sizeof(nod));
                    q1->c = s[i];
                    q1 = q1->jos;
                    q1->jos = NULL;
                    q1->urm = NULL;
                }
    }
   /*for ( q = root; q ; q = q->urm )
    {
       for ( q1 = q; q1-> jos; q1 = q1->jos )
        {
            printf ( "%c", q1->c );
        }
    printf ( "*\n" );
    }*/
   int nr = 0,ok;

   for ( int i = 0; i < d; i ++ )
    {
        q = root;
        for( int j = 0; j < strlen(a[i]); j ++)
         {
            if( j > 0 ) q = q->urm;
            ok = 0;
            for ( q1 = q; q1; q1 = q1->jos )
                if ( q1->c == a[i][j] )
                    ok = 1;
            if ( ok == 0 ) break;
         }
        if ( ok ) nr ++ ;
    }
   return nr;
}

void cit ()
{
 char s[256];
 int nr = 0;
        freopen ( "a.in", "r", stdin );
        freopen ( "a.out", "w", stdout );
        scanf ("%d %d %d", &l, &d, &n );
        for ( int i = 0; i < d; i ++ )
            scanf ( "%s", a[i] );
        fgets ( s, 256, stdin );
        for ( int i = 0; i < n; i ++ )
         {
            fgets ( s, 256, stdin );
            printf ( "Case #%d: %d\n", i+1, verif ( s ) );
         }
        fclose( stdin );
        fclose( stdout );
}

void afis ()
{
        for ( int i = 0; i < d; i ++ )
         printf( "%s\n", a[i] );
}

int main()
{
    cit ();

    return 0;
}
