#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <cstring>
using namespace std;

string to[ 4 ] = { "ejp mysljylc kd kxveddknmc re jsicpdrysi" , "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" , "de kr kd eoya kw aej tysr re ujdr lkgc jv" , "y qee" };
string from[ 4 ] = { "our language is impossible to understand" , "there are twenty six factorial possibilities" , "so it is okay if you want to just give up" , "a zoo" };

map< char , char > sub;
int main(){
  
  for( int q = 0 ; q < 4 ; q++ ){
    for( int w = 0 ; w < (int)from[ q ].size() ; w++ ){
      sub[ to[ q ][ w ] ] = from[ q ][ w ];
    }
  }
  
  for( int q = 'a' ; q <= 'z' ; q++ ){
    bool ok = 0;
    for( int w = 'a' ; w <= 'z' ; w++ ){
      if( sub[ w ] == q ){
	ok = 1;
      }
    }
    if( !ok ) sub[ 'z' ] = q;
  }
  
  FILE *in = fopen( "f.in" , "r" );
  freopen( "f.out" , "w" , stdout );
  int ntest;
  fscanf( in , "%d\n" ,&ntest );
  
  for( int t = 1 ; t <= ntest ; t++ ){
    printf( "Case #%d: " ,t );
    char x; 
    fscanf( in , "%c" ,&x );
    while( x != '\n' ){
      printf( "%c" ,sub[ x ] );
      fscanf( in , "%c" ,&x );
    }
    printf( "\n" );
  }
  
  return 0;
}
