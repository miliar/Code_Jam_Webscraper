/* Copyright NTUEE 2009. All Rights Reserved. */
/* =====================================================================================
 *       Filename:  main.cpp
 *    Description:  Watersheds
 *        Created:  09/03/09 14:34:27 CST
 *         Author:  Gary Wu (NTUEE), researchgary@gmail.com
 * ===================================================================================== */

#include <set>
#include <map>
#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

/////UTILITY FUNCTIONS LISTS///////////////////////////////////////
size_t   getTokens( string s, char itrpt, vector<string>& tokens );
size_t   getTokensPar( string s, vector<string>& vcStr );
bool     isNum( char c );
int      toDec( char c );
double      str2Int( const string& s);
int      DecToBase(int base, long iDec, char* szString);
template<class T>
void     vc_out( vector<T>& vc );
///////////////////////////////////////////////////////////////////

/////MAIN FUNCTIONS LISTS///////////////////////////////////////
///////////////////////////////////////////////////////////////////

size_t nCases;
vector<string> qs;

void
readIn( ifstream& ifs ){
   char c[256];
   ifs.getline(c,256);   
   string s = c;
   nCases = str2Int(s);
   for ( unsigned i = 0 ; i < nCases ; ++i ){
      char c1[256];
      ifs.getline(c1,256);
      string s1 = c1;
      vector<string> vcS;
      qs.resize(nCases);
      getTokens( s1, ' ', vcS );
      qs[i]= vcS[0];
   }
}

void
case_out( ofstream& ofs, size_t ith, string s ){
   ofs << "Case #" << ith << ": " << s << endl;
}

void
solve( ofstream& ofs ){
   for ( int i = 0 ; i < nCases; ++i ){
      ostringstream sout;
      sout << qs[i];
      char *c = (char*)sout.str().c_str();
      if ( next_permutation(c,c+qs[i].length()) ){
         string s = c;
         case_out(ofs,i+1,s);
      }else{
         ostringstream sout;
         sout << "0" << qs[i];
         string tmp = sout.str();
         char* c1 = (char*)tmp.c_str();
         next_permutation(c1,c1+qs[i].length()+1);
         string s1 = c1;
         case_out(ofs,i+1,s1);
      }
   }
}

int
main( int argc, char* argv[] ){
   ifstream ifs; 
   ofstream ofs("output");
   ifs.open(argv[1]);
   if ( !ifs.is_open() ){
      cerr << "Can't open file " << argv[1] << endl;
      return 0;
   }
   readIn(ifs);
   solve(ofs);
   ifs.close();
   ofs.close();
   return 0;
}


//utility functions
bool
   isNum( char c ){
      if ( c >= 48 && c<=57 )
         return true;
      return false;
   }

int
   toDec( char c ){
      if ( isNum(c) )
         return ((int)c-48);
      return -1;
   }

double
str2Int( const string& s){
   double ret = 0;
   double tens = 1;
   bool isMinus = (s[0]=='-');

   for ( int i = s.size()-1 ; i >= 0 ; --i ){
      if ( i == 0 && isMinus )
         continue;
      int x = toDec(s[i]);
      if ( x < 0 )
         return 0;
      ret = ret + x*tens;
      tens = tens * 10;
   }
   ret = isMinus ? -ret : ret;
   return ret;
}

size_t
getTokens( string s, char itrpt, vector<string>& tokens ){
   int prePos = 0, nxtPos = 0;
   do{
      ostringstream sout;
      nxtPos = s.find_first_of( itrpt, prePos+1 );
      if ( nxtPos == string::npos )
         nxtPos = s.size();
      for ( int i = prePos; i < nxtPos ; ++i ){
         sout << s[i];
      }
      prePos = nxtPos+1;
      tokens.push_back(sout.str());
      //cout << sout.str() << " ";

   } while(nxtPos!=s.size());
   //cout << endl;
   return tokens.size();
}

template<class T> void
vc_out( vector<T>& vc ){
   for ( size_t i = 0 ; i < vc.size() ; ++i )
      cout << vc[i] << " ";
   cout << endl;
}

size_t
getTokensPar( string s, vector<string>& vcStr ){
   bool start = 0;
   ostringstream sout;
   for ( size_t i = 0 ; i < s.size() ; ++i ){
      if ( s[i] == '(' ){
         start = 1;
         continue;
      }
      if ( s[i] == ')' ){
         string ps = sout.str();
         sort(ps.begin(),ps.end());
         vcStr.push_back(ps);
         sout.str("");
         start = 0;
         continue;
      }
      if ( start == 0 ){
         vcStr.push_back(string(1,s[i]));
      }
      if ( start == 1 )
         sout << s[i];
   }
   return vcStr.size();
}
