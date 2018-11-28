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
#include "g_bignum.h"
#include <cassert>

using namespace std;

/////UTILITY FUNCTIONS LISTS///////////////////////////////////////
size_t   getTokens( string s, char itrpt, vector<string>& tokens );
size_t   getTokensPar( string s, vector<string>& vcStr );
bool     isNum( char c );
int      toDec( char c );
unsigned long long      str2Int( const string& s);
int      DecToBase(int base, long iDec, char* szString);
bool     analyze(const string&, vector<double>&, double&);
template<class T> void vc_out( vector<T>& vc );
///////////////////////////////////////////////////////////////////

/////MAIN FUNCTIONS LISTS///////////////////////////////////////
///////////////////////////////////////////////////////////////////

size_t nCases;
vector<unsigned long long> N;
vector<vector<GBigNum> > qs;

void
readIn( ifstream& ifs ){
   char c[1048576];
   ifs.getline(c,1048576);   
   string s = c;
   nCases = str2Int(s);
   qs.resize(nCases);
   for ( unsigned i = 0 ; i < nCases ; ++i ){
      char c1[1<<15];
      ifs.getline(c1,1<<15);
      string s1 = c1;
      vector<string> firstline;
      getTokens(s1,' ',firstline);
      N.push_back(str2Int(firstline[0]));

      for ( unsigned j = 1 ; j < firstline.size() ; ++j )
         qs[i].push_back(GBigNum(firstline[j]));
   }
}

void
case_out( ofstream& ofs, size_t ith, string num ){
   ofs << "Case #" << ith << ": " << num << endl;
   cout << "Case #" << ith << ": " << num << endl;
}

char symbols[37] = "0123456789ABCDEFGHIJKLMNoPQRSTUVWXYZ";

struct Par {
   unsigned long long pos;
   unsigned long long cost;
};

typedef unsigned long long ul;


// a>b
GBigNum check( const GBigNum& a, const GBigNum& b ){
   if ( a==b )
      return a;
   GBigNum r = a%b;
   if ( r==GBigNum("0") )
      return b;
   return check(b,r);
}

void
solve( ofstream& ofs ){
   vector<string> rst;
   for ( int i = 0 ; i < nCases; ++i ){
      //sort
      sort(qs[i].begin(),qs[i].end());
      vector<GBigNum> diffSet;
      for ( unsigned j = 0 ; j < N[i]-1 ; ++j ){
         GBigNum diff = qs[i][j+1]-qs[i][j];
         if ( diff!=GBigNum("0") )
            diffSet.push_back( qs[i][j+1]-qs[i][j] );
      }
      sort(diffSet.begin(),diffSet.end());
      GBigNum fac("1");
      for ( unsigned j = 0 ; j < diffSet.size()-1 ; ++j ){
         fac = check(diffSet[j+1],diffSet[j]);
         if ( fac == GBigNum("1") )
            break;
         diffSet[j+1] = fac;
      }
      if ( diffSet.size()==1 )
         fac = diffSet[0];
      GBigNum rst("0");
      if ( fac!=GBigNum("1") ){
         rst = fac - qs[i][0]%fac;
      }
      /*
      for ( unsigned j = 0 ; j < N[i] ; ++j ){
         qs[i][j] = qs[i][j]+rst;
         assert( qs[i][j] % fac==GBigNum("0")  );
      }
      if ( N[i] == 2 )
         assert(fac==(qs[i][1]-qs[i][0]));
      else{
         if ( qs[i][1]-qs[i][0] != GBigNum("0") && qs[i][2]-qs[i][1] != GBigNum("0") )
            assert(fac==check(qs[i][1]-qs[i][0],qs[i][2]-qs[i][1]));
      }
      */
      case_out(ofs,i+1,rst.ToString());
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



/* ====================== utility functions =============================== */
// ________________________________________________________________________

int DecToBase(int base, long iDec, char* szString)
{
   //Check base is between 2 and 36
   if(base<2)
      return 0; //Failed
   //If input is 0, output is 0
   if(iDec==0){
      strcpy(szString,"0");
      return 1;
   }

   int count = 0;
   char chResult[256] = "";
   char* pChResult = chResult;
   while(iDec > 0 && count++<256)
   {
      *pChResult = symbols[iDec % base];
      pChResult++;
      iDec = iDec/base; //iDec = itself divided by base
   }
   ostringstream sout;
   string s = chResult;
   for( int i = s.size()-1 ; i >=0 ; --i ){
      sout << s[i];
   }
   s = sout.str();
   strcpy(chResult,s.c_str()); 
   strcpy(szString,chResult);

   return 1;
}

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

unsigned long long
str2Int( const string& s){
   unsigned long long ret = 0;
   long tens = 1;
   bool isMinus = (s[0]=='-');

   for ( int i = s.size()-1 ; i >= 0 ; --i ){
      if ( i == 0 && isMinus )
         continue;
      int x = toDec(s[i]);
      if ( x < 0 )
         return 0;
      ret = ret + (long long)x*tens;
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

bool analyze(const string& fileName, vector<double>& out, double& opt){
   ifstream infile(fileName.c_str(), ios::in);
   string a;
   infile >> a;
   if (a == "Infeasible") {
      return false;
   }
   infile >> a;
   infile >> a;
   infile >> a;
   infile >> opt;
   while (infile >> a) {
      infile >> a;
      double t;
      infile >> t;
      out.push_back(t);
      infile >> t;
   }
   return true;
}
