#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int n;
string x;

int main (){
    
    scanf( "%d", &n );
    
    for( int j = 1; j <= n+1; ++j ){
      getline( cin, x );
      string ret;
      
      for( int i = 0; i < x.size(); ++i ){
        if( x[i] == ' ' ) ret += ' ';
        if( x[i] == 'y' ) ret += 'a';
        if( x[i] == 'n' ) ret += 'b';
        if( x[i] == 'f' ) ret += 'c';
        if( x[i] == 'i' ) ret += 'd';
        if( x[i] == 'c' ) ret += 'e';  // a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
        if( x[i] == 'w' ) ret += 'f';
        if( x[i] == 'l' ) ret += 'g';
        if( x[i] == 'b' ) ret += 'h';
        if( x[i] == 'k' ) ret += 'i';
        if( x[i] == 'u' ) ret += 'j';
        if( x[i] == 'o' ) ret += 'k';
        if( x[i] == 'm' ) ret += 'l';
        if( x[i] == 'x' ) ret += 'm';
        if( x[i] == 's' ) ret += 'n';
        if( x[i] == 'e' ) ret += 'o';
        if( x[i] == 'v' ) ret += 'p';
        if( x[i] == 'z' ) ret += 'q';
        if( x[i] == 'p' ) ret += 'r';
        if( x[i] == 'd' ) ret += 's';
        if( x[i] == 'r' ) ret += 't';
        if( x[i] == 'j' ) ret += 'u';
        if( x[i] == 't' ) ret += 'w';
        if( x[i] == 'h' ) ret += 'x';
        if( x[i] == 'a' ) ret += 'y';
        if( x[i] == 'q' ) ret += 'z';
        if( x[i] == 'g' ) ret += 'v';
      }
      if( j == 1 ) continue;
      printf( "Case #%d: ", j-1 ); cout << ret << endl; 
    }
    
    return 0;   
}
