#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <map>
#include <algorithm>
#define fore(I,D) for(unsigned int(I)=0;(I)<(D).size();++(I))
#define forn(I,S) for(unsigned int(I)=0;(I)<(S);++(I))
#define ALL(C) (C).begin(),(C).end()
#define COUNT(C,N) count(ALL(C),(N))
#define SORT(C) sort(ALL(C))
#define REV(C) reverse(ALL(C))
#define UNIQ(C) (C).erase( unique(ALL(C)), (C).end());
#define FIND(C,N) find(ALL(C),N)
#define FILL(C,N) fill(ALL(C),N)
#define REPLACE(C,N1,N2) replace(ALL(C),N1,N2)
#define COMMA <<","<<
#define ENDL <<endl
//#include <iomanip>
using namespace std;
// time g++ -Wall -O0 -mtune=pentium-m qual.cpp ; time cat sample.in | ./a.exe | tee out

bool isdraw( vector<string> bd ){
  fore( i, bd )
    fore( j, bd[0] )
    if( bd[i][j]=='.' )
      return false;
  return true;
}
bool isxwin_sub2( vector<string> bd, char x ){
  fore( i, bd[0] )
    if( bd[i][i]!=x )
      return false;
  return true;
}
bool isxwin_sub3( vector<string> bd, char x ){
  fore( i, bd[0] )
    if( bd[bd[0].size()-1-i][i]!=x )
      return false;  
  return true;
}
bool isxwin_sub1( vector<string> bd, char x ){
  string str="xxxx";
  REPLACE( str, 'x', x );
  
  fore( i, bd )
    if( bd[i]==str )
      return true;
 
  return false;
}

bool isxwin( vector<string> bd, char x ){
  fore( i, bd )
    REPLACE( bd[i], 'T', x );
  
  vector<string> bd2=bd;
  fore( i, bd )
    fore( j, bd[0] )
    bd2[i][j]= bd[j][i];
  
  return isxwin_sub1( bd, x ) || isxwin_sub1( bd2, x )
    ||isxwin_sub2( bd, x ) || isxwin_sub3( bd2, x );   
}

string sub1(){
  string s="init";
  vector<string> bd;
  forn( i, 4 ){
    cin >> s;
    bd.push_back(s);
  }
  //fore( i, bd )
  //  cout << bd[i] ENDL;
  
  if( isxwin( bd, 'O' ) )
    return " O won";
  if( isxwin( bd, 'X' ) )
    return " X won";
  if( isdraw( bd ) )
    return " Draw";
  return " Game has not completed";
}


int main (int argc, char*argv[]){
  int T;
  cin >> T;
  
  //cout << T ENDL;
  for ( int i=0 ; i<T ; i++ ){
    cout << "Case #" << i+1 << ":" ;

    cout << sub1();
    //cout.precision(6);
    //cout << sub1();
    //printf("%6f",sub1());
    cout << endl;
  }
  
  return 1;
};
