#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

bool check(char ch, vector< string > &table ){
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      if( !(table[i][j] == ch || table[i][j] == 'T') )break;
      if( j == 3 ) return true;
    }
  }
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      if( !(table[j][i] == ch || table[j][i] == 'T') )break;
      if( j == 3 ) return true;
    }
  }
  for(int i=0; i<4; i++){
    if( !(table[i][i] == ch || table[i][i] == 'T') )break;
    if( i == 3 ) return true;
  }
  for(int i=0; i<4; i++){
    if( !(table[3-i][i] == ch || table[3-i][i] == 'T') )break;
    if( i == 3 ) return true;
  }

  return false;
}

bool check2(vector< string > &table) {
  for(int i=0; i<4; i++){
    for(int j=0; j<4; j++){
      if(table[i][j] == '.' )return false;
    }
  }
  return true;
}

int main(){
  int T;
  cin >> T;
  for( int t_case = 1; t_case <= T; t_case++ ){
    vector< string > table(4);
    for(int i=0; i<4; i++ ){ cin >> table[i]; }
    printf("Case #%d: ",t_case);
    if( check('X',table) ){
      printf("X won");
    } else if ( check('O',table) ){
      printf("O won");
    } else if ( check2( table) ){
      printf("Draw");
    } else {
      printf("Game has not completed");
    }
    printf("\n");
  }
  return 0;
}
