/* Copyright NTUEE 2009. All Rights Reserved. */
/* =====================================================================================
 *       Filename:  main.cpp
 *    Description:  Answer alien language problem
 *        Created:  09/03/09 10:57:57 CST
 *         Author:  Gary Wu (NTUEE), researchgary@gmail.com
 * ===================================================================================== */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

//////////UTILITY FUNCTIONS LIST///////////////////////////////////////////////////////
size_t   getTokens( string s, char itrpt, vector<string>& tokens );
size_t   getTokensPar( string s, vector<string>& vcStr );
bool     isNum( char c );
int      toDec( char c );
int      str2Int( const string& s);
template<class T>
void     vc_out( vector<T>& vc );
///////////////////////////////////////////////////////////////////////////////////////

//////////MAIN FUNCTIONS LIST//////////////////////////////////////////////////////////
void setupParam( ifstream& ifs );
void setupStr( ifstream& ifs );
void solve( ofstream& ofs );
///////////////////////////////////////////////////////////////////////////////////////

size_t N = 0;
vector<string> str;
string STR = "welcome to code jam";
size_t length;
string strSet = " acdejlmotw";
vector<int> ans;

int 
main( int argc, char* argv[] ){
   ifstream input(argv[1]);
   ofstream ofs;
   ofs.open("output");
   if ( !input.is_open() ){
      cerr << "Can't open file " << argv[1] << endl;
      return 0;
   }
   // setup
   length = STR.size();
   setupParam( input );
   setupStr( input ); 
   solve(ofs);
   input.close();
   ofs.close();
   return 0;
}

void
setupParam( ifstream& fs ){
   char c[32];
   fs.getline(c,32);
   string s = c;
   N = (size_t)str2Int(s);
}

void
case_out( ofstream& ofs, size_t ith ,int num ){
   ofs << "Case #" << ith << ": ";
   if ( num < 10 )
      ofs << "000";
   else if ( num < 100 ) 
      ofs << "00";
   else if ( num < 1000 )
      ofs << "0";
   ofs << num << endl;
}

void
setupStr( ifstream& ifs ){
   for ( size_t i = 0 ; i < N ; ++i ){
      char c[1000];
      ifs.getline(c,1000);
      string s = c;
      str.push_back(s);
   }
}

void
deleteLit( string& s ){
   ostringstream sout;
   for (size_t i = 0 ; i < s.size() ; ++i ){
      if ( strSet.find(s[i]) != string::npos )
         sout << s[i];
   }
   s = sout.str();
}

void
solve( ofstream& ofs ){
   // filter out redundant literals
   for ( size_t ith = 0 ; ith < N ; ++ith ){
      int num = 0;
      string s = str[ith];
      deleteLit(s); 
      if ( s.size() < length ){
         ans.push_back(0);
         continue;  
      }
      vector<vector<unsigned> > dp;
      dp.resize(s.size()+ 1);
      for (unsigned i = 0; i < dp.size(); ++i) {
         dp[i].resize(length+1, 0);
      }
      dp[0][0] = 1;
      for (unsigned pos = 0; pos < s.length(); ++pos) {
         for (unsigned i = 1; i <= length; ++i) {
            if ( s[pos] != STR[i-1] )
               continue;
            for (unsigned j = 0; j <= pos; ++j){
               dp[pos+1][i] += dp[j][i-1];
            }
            dp[pos+1][i] %= 10000;
         }
         num += dp[pos+1][19];
         num %= 10000;
      }
      ans.push_back(num);
   }
   for( size_t ith = 0 ; ith < N ; ++ith )
      case_out( ofs, ith+1, ans[ith] );
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
      if ( i == s.size()-1 && isMinus )
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
