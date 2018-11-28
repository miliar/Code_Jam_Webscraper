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
int      str2Int( const string& s);
int      DecToBase(int base, long iDec, char* szString);
template<class T>
void     vc_out( vector<T>& vc );
///////////////////////////////////////////////////////////////////

/////MAIN FUNCTIONS LISTS///////////////////////////////////////
///////////////////////////////////////////////////////////////////

class Node{
   public:
      Node():num(0){
         //f0 = new Node();
         //f1 = new Node();
      }
      Node(double n ){
         //f0 = new Node();
         //f1 = new Node();
         num = n;
      }
      void setFanin(unsigned ith, Node n, string s){
         if ( ith = 0 ){
            *f0 = n;
            e0 = s;
         }else{
            *f1 = n;
            e1 = s;
         }
      }
      double operator() ( const Node& n ){
         return num;
      }
      ~Node(){}
      void operator = ( Node n ){
         num = n.num;
         e0 = n.e0;
         e1 = n.e1;
         *f0 = *n.f0;
         *f1 = *n.f1;
      }
      double num;
      string e0;
      string e1;
      Node* f0;
      Node* f1;
};

size_t nCases;
Node top;
vector<vector<vector<string> > > qs;
vector<vector<vector<string> > > ani;

void
readIn( ifstream& ifs ){
   char c[256];
   ifs.getline(c,256);   
   string s = c;
   nCases = str2Int(s);
   qs.resize(nCases);
   ani.resize(nCases);
   for ( unsigned i = 0 ; i < nCases ; ++i ){
      char c2[256];
      ifs.getline(c2,256);   
      string s2 = c2;
      int nLines = str2Int(s2);
      qs[i].resize(nLines);
      for ( int j = 0 ; j < nLines ; ++j ){
         char c1[256];
         ifs.getline(c1,256);
         string s1 = c1;
         vector<string> vcS;
         getTokens( s1, ' ', vcS );
         for ( unsigned x = 0 ; x < vcS.size() ; ++x ){
            if ( vcS[x].length()!=0)
               qs[i][j].push_back(vcS[x]);
         }
         vc_out(qs[i][j]);
      }

      char c3[256];
      ifs.getline(c3,256);   
      string s3 = c3;
      nLines = str2Int(s3);
      ani[i].resize(nLines);
      
      for ( int j = 0 ; j < nLines ; ++j ){
         char c1[256];
         ifs.getline(c1,256);
         string s1 = c1;
         vector<string> vcS;
         getTokens( s1, ' ', vcS );
         for ( unsigned x = 0 ; x < vcS.size() ; ++x ){
            if ( vcS[x].length()!=0)
               ani[i][j].push_back(vcS[x]);
         }
         vc_out(ani[i][j]);
      }
   }
}

void
case_out( ofstream& ofs, size_t ith, int num ){
   ofs << "Case #" << ith << ": " << num << endl;
}

void
solve( ofstream& ofs ){
   for ( int i = 0 ; i < nCases; ++i ){
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

int
str2Int( const string& s){
   int ret = 0;
   int tens = 1;
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
         if ( s[i] != ' ')
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
