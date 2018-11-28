#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>

using namespace std;

map<char, char> mp;
bool x[ 30 ];

int main()
{
   freopen( "asmall.in", "r", stdin );
   freopen( "asmall.out", "w", stdout );
   mp[ 'a' ] = 'y';
   mp[ 'b' ] = 'h';
   mp[ 'c' ] = 'e';
   mp[ 'd' ] = 's';
   mp[ 'e' ] = 'o';
   mp[ 'f' ] = 'c';
   mp[ 'g' ] = 'v';
   mp[ 'h' ] = 'x';
   mp[ 'i' ] = 'd';
   mp[ 'j' ] = 'u';
   mp[ 'k' ] = 'i';
   mp[ 'l' ] = 'g';
   mp[ 'm' ] = 'l';
   mp[ 'n' ] = 'b';
   mp[ 'o' ] = 'k';
   mp[ 'p' ] = 'r';
   mp[ 'q' ] = 'z';
   mp[ 'r' ] = 't';
   mp[ 's' ] = 'n';
   mp[ 't' ] = 'w';
   mp[ 'u' ] = 'j';
   mp[ 'v' ] = 'p';
   mp[ 'w' ] = 'f';
   mp[ 'x' ] = 'm';
   mp[ 'y' ] = 'a';
   mp[ 'z' ] = 'q';
   char c;
   char d;
   for( c = 'a'; c <= 'z'; ++c )
      for( d = c + 1; d <= 'z'; ++d )
         if( mp[ c ] == mp[ d ] )
         {
            cout << c << ' ' <<  d << endl;
         }

   int n;
   scanf( "%d", &n );
   int i = 0;
   while( scanf("%c", &c ) == 1 )
   {
      if( isalpha( c ))
         printf( "%c", mp[ c ] );
      else
      {
         if( c == '\n' && i < n )
         {
            ++i;
            if( i > 1 )
               printf( "\n" );
            printf( "Case #%d: ", i );
         }
         else
         {
            printf( "%c", c );
            if( c == '\n' )
               break;
         }
           

      }
   }
   return 0;
}
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
*/