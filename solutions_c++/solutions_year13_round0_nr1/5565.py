#include <iostream>
#include <stdio.h>
using namespace std ;

char s[4][5] ;
int winner = 0 ;
bool not_yet_comp = 0 ;

void scan_x ( int x ){
  bool ff = 1 ;
  for ( int i = 1 ; i < 4 ; ++i ) {
    if ( s[x][i] == '.' ) not_yet_comp = 1 ;
    if ( s[x][i] != 'T' && s[x][i] != s[x][i-1] ) ff = 0 ;
  }
  if ( ff ) {
    if ( s[x][0] != 'T' ) {
      if ( s[x][0] == 'X' ) winner = 1 ;
      else if ( s[x][0] == 'O' ) winner = -1 ;
    }
    else {
      if ( s[x][1] == 'X' ) winner = 1 ;
      else if ( s[x][1] == 'O' ) winner = -1 ;
    }
  } 
}
void scan_y ( int x ){
  bool ff = 1 ;
  for ( int i = 1 ; i < 4 ; ++i ) {
    if ( s[i][x] == '.' ) not_yet_comp = 1 ;
    if ( s[i][x] != 'T' && s[i][x] != s[i-1][x] ) ff = 0 ;
  }
  if ( ff ) {
    if ( s[0][x] != 'T' ) {
      if ( s[0][x] == 'X' ) winner = 1 ;
      else if ( s[0][x] == 'O' ) winner = -1 ;
    }
    else {
      if ( s[1][x] == 'X' ) winner = 1 ;
      else if ( s[0][x] == 'O' ) winner = -1 ;
    }
  }
}
void scan_dig() {
  bool ff = 1 ;
  for ( int i = 1 ; i < 4 ; ++i ){
    if ( s[i][i] != 'T' && s[i][i] != s[i-1][i-1] ) ff = 0 ;
  }
  if ( ff ){
    if ( s[0][0] != 'T' ){
      if ( s[0][0] == 'X' ) winner = 1 ;
      else if ( s[0][0] == 'O' ) winner = -1 ;
    }
    else {
      if ( s[1][1] == 'X' ) winner = 1 ;
      else if ( s[1][1] == 'O' ) winner = -1 ;
    }
  }
  ff = 1 ;
  for ( int i = 1 ; i < 4 ; ++i ){
    if ( s[i][3-i] != 'T' && s[i][3-i] != s[i-1][4-i] ) ff = 0 ;
  }
  if ( ff ){
    if ( s[0][3] != 'T' ){
      if ( s[0][3] == 'X' ) winner = 1 ;
      else if ( s[0][3] == 'O' ) winner = -1 ;
    }
    else {
      if ( s[1][2] == 'X' ) winner = 1 ;
      else if ( s[1][2] == 'O' ) winner = -1 ;
    }
  }
}

int main () {
  freopen( "A-small-attempt0.in", "r", stdin );
  freopen( "A-small-attempt0.out", "w", stdout );
  int n, cas ;
  scanf ( "%d" , &n );
  for ( cas = 1 ; cas <= n ; ++cas ){
    winner = 0 ;
    not_yet_comp = 0 ;
    for ( int i = 0 ; i < 4 ; ++i ){
      getchar() ;
      scanf ( "%s" , &s[i] );
    }
    // -->
    for ( int i = 0 ; i < 4 ; ++i ){
      scan_x ( i ) ;
      scan_y ( i ) ;
    }
    scan_dig() ;
    printf ( "Case #%d: ", cas );
    if ( winner == 1 )  printf ( "X won" );
    else if ( winner == -1 ) printf ( "O won" );
    else if ( winner == 0 ){
      if ( not_yet_comp ) printf ( "Game has not completed" );
      else printf ( "Draw" );
    }
    printf ( "\n" );
  }
}
