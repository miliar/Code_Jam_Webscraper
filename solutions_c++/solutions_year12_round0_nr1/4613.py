#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std ;

string instr[3] = {
  "ejp mysljylc kd kxveddknmc re jsicpdrysi" ,
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" ,
  "de kr kd eoya kw aej tysr re ujdr lkgc jv" };
string outstr[3] = {
  "our language is impossible to understand" ,
  "there are twenty six factorial possibilities" ,
  "so it is okay if you want to just give up" };

int map[26] ; 

void init()
{
  int flag[26] ; 
  memset(flag,0,sizeof(flag)) ;
  map['e'-'a'] = 'o' ;
  map['q'-'a'] = 'z' ;
  map['y'-'a'] = 'a' ;
  for( int i = 0 ; i < 3 ; ++ i )
    {
      for( int j = 0 ; j < instr[i].size() ; ++ j )
        {
          map[instr[i][j]-'a'] = outstr[i][j];
          flag[outstr[i][j]-'a'] = 1 ;
        }
    }
  int anno = -1 ;
  for( int i = 0 ; i < 26 ; ++ i )
    if(flag[i] == 0 ) { anno = i ; break ; }
  for( int i = 0 ; i < 26 ; ++ i )
    if( !map[i] ) map[i] = anno + 'a' ;
  //  for( int i = 0 ; i < 26 ; ++ i )
  //  {
  //    cout << char(i+'a') << "->" << char(map[i]) << endl ;
  //}
}

int main()
{
  int case_count ;
  int case_order ;
  init() ;
  cin >> case_count ;
  getchar() ;
  case_order = 1 ;
  string line ;
  while(case_count--)
    {
      getline(cin,line) ;
      string result ;
      for( int i = 0 ; i < line.size() ; ++ i )
        {
          if( line[i] == ' ' ) result+=line[i] ; 
          else result += char(map[line[i]-'a']) ;
        }
      cout << "Case #" << case_order ++ << ": " << result << endl ;
    }
  return 0 ;
}
