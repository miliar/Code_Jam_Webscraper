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
void setupParam( ifstream& fs, size_t& L, size_t& D, size_t& N );
void readExistWords( ifstream& fs, size_t L, size_t D, vector<string>& words );
void readPatterms( ifstream& fs, size_t& N, vector<vector<string> >& patterm );
void case_out( ofstream& ofs, size_t ith ,size_t num );
void solve( ofstream& fs, vector<string>& words, vector<vector<string> >& patterm );
///////////////////////////////////////////////////////////////////////////////////////



int 
main( int argc, char* argv[] ){
   ifstream input(argv[1]);
   if ( !input.is_open() ){
      cerr << "Can't open file " << argv[1] << endl;
      return 0;
   }
   // setup
   size_t L, D, N;
   vector<string> words;
   vector<vector<string> > patterm;
   setupParam( input, L, D, N );
   readExistWords( input, L, D, words );
   readPatterms( input, N, patterm );
   ofstream ofs;
   ofs.open("output");
   solve( ofs, words, patterm );
   input.close();
   ofs.close();
   return 0;
}

void
setupParam( ifstream& fs, size_t& L, size_t& D, size_t& N ){
   char c[32];
   fs.getline(c,32);
   string s = c;
   vector<string> vcStr;
   getTokens( s, ' ', vcStr ); 
   L = (size_t)str2Int(vcStr[0]);
   D = (size_t)str2Int(vcStr[1]);
   N = (size_t)str2Int(vcStr[2]);
   assert(vcStr.size()==3);
}

void 
readExistWords( ifstream& fs, size_t L, size_t D, vector<string>& words ){
   for ( size_t i = 0 ; i < D ; ++i ){
      char c[L+1];
      fs.getline(c,L+1);
      string s = c;
      words.push_back(s);
   }
}

void
readPatterms( ifstream& fs, size_t& N, vector<vector<string> >& patterm ){
   for ( size_t i = 0 ; i < N ; ++i ){
      char c[140001];
      fs.getline(c,140001);
      string s = c;
      vector<string> vcStr;
      getTokensPar( s, vcStr );
      vc_out(vcStr);
      patterm.push_back(vcStr);
   }
}

void
case_out( ofstream& ofs, size_t ith ,size_t num ){
   ofs << "Case #" << ith << ": " << num << endl;
}

void
solve( ofstream& fs, vector<string>& words, vector<vector<string> >& patterm ){
   vector<size_t> num( patterm.size(), 0 );
   size_t wdSize = words[0].size();
   for ( size_t i = 0 ; i < words.size() ; ++i ){
      for( size_t pj = 0 ; pj < patterm.size() ; ++pj ){
         // filtering impossible cases
         bool p = 1;
         for ( size_t wk = 0 ; wk < wdSize ; ++wk ){
            char c1 = (const char)patterm[pj][wk][0];
            char c2 = (const char)patterm[pj][wk][patterm[pj][wk].size()-1];
            if ( words[i][wk] < c1 || words[i][wk] > c2 )
            {
               p = 0;
               break;
            }
         }
         if ( p == 0 )
            continue;
         // counts
         bool found = 1;
         for ( size_t wk = 0 ; wk < wdSize ; ++wk ){
            if ( patterm[pj][wk].find(words[i][wk]) == string::npos )
            {
               found = 0;
               break;
            }
         }
         if ( found == 1 )
            ++num[pj];
      }
   }
   for ( size_t i = 0 ; i < num.size() ; ++i ){
      case_out(fs,i,num[i]);
   }
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
