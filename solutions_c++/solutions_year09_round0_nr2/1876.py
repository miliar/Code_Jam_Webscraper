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
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

/////UTILITY FUNCTIONS LISTS///////////////////////////////////////
size_t   getTokens( string s, char itrpt, vector<string>& tokens );
size_t   getTokensPar( string s, vector<string>& vcStr );
bool     isNum( char c );
int      toDec( char c );
int      str2Int( const string& s);
template<class T>
void     vc_out( vector<T>& vc );
///////////////////////////////////////////////////////////////////

/////MAIN FUNCTIONS LISTS///////////////////////////////////////
void nMaps( ifstream& ifs, size_t& n );
void readMaps( ifstream& ifs, ofstream& ofs );
void solve( ofstream& ofs );
void case_out( ofstream& ofs, size_t ith );
///////////////////////////////////////////////////////////////////

size_t n = 0;
vector<size_t *>     mapSize;
vector<vector<size_t> > maps;

int
main( int argc, char* argv[] ){
   ifstream ifs; 
   ofstream ofs("output");
   ifs.open(argv[1]);
   if ( !ifs.is_open() ){
      cerr << "Can't open file " << argv[1] << endl;
      return 0;
   }
   nMaps( ifs, n);
   readMaps( ifs, ofs);
   ifs.close();
   ofs.close();
   return 0;
}

void
nMaps( ifstream& ifs, size_t& n ){
   char c[16];
   ifs.getline(c,16);
   string s = c;
   n = str2Int(s);
}

void
readMaps( ifstream& ifs, ofstream& ofs ){
   for ( size_t i = 0 ; i < n ; ++i ){
      // get map size
      mapSize.clear();
      maps.clear();
      char c[16];
      ifs.getline(c,16);
      string s = c;
      vector<string> vcStr;
      getTokens( s, ' ', vcStr );
      size_t size[2];
      size_t H = (size_t)str2Int(vcStr[0]);
      size_t W = (size_t)str2Int(vcStr[1]);
      size[0] = H; size[1] = W;
      mapSize.push_back( size );
      // get map content
      for ( size_t j = 0 ; j < H ; ++j ){
         char c1[100000];
         ifs.getline(c1,100000);
         string s1 = c1;
         vector<string> vcStr1;
         getTokens( s1, ' ', vcStr1 );
         vector<size_t> mapAlt;
         mapAlt.resize(vcStr1.size());
         for ( size_t k = 0 ; k < vcStr1.size() ; ++k ){
            mapAlt[k] = str2Int(vcStr1[k]);
         }
         maps.push_back(mapAlt);
      }
      // solve
      case_out( ofs, i+1 );
      solve(ofs);
   }
}

bool
isFlow( size_t a, size_t b ){
   return a > b; 
}

void
insertSet( vector<set<size_t> >& sets, size_t t, size_t insert ){
   bool found = 0;
   for( size_t i = 0 ; i < sets.size() ; ++i ){
      if ( sets[i].find(t) != sets[i].end() ){
         sets[i].insert(insert);
         found = 1;
      }
      if ( sets[i].find(insert) != sets[i].end() && found == 0 ){
         sets[i].insert(t);
         found = 1;
      }
      if ( found )
         return;
   }
   if ( found == 0 ){
      set<size_t> s;
      s.insert(t);
      s.insert(insert);
      sets.push_back(s);
   }
}

void
solve( ofstream& ofs ){
   size_t& H = mapSize[0][0];
   size_t& W = mapSize[0][1];

   // encode ith
   vector<vector<size_t> > tmp;
   tmp = maps;
   size_t x = 0;
   for ( size_t i = 0 ; i < tmp.size() ; ++i ){
      for ( size_t j = 0 ; j < tmp[i].size() ; ++j ){
         tmp[i][j] = x++;
      }
   }

   // set
   vector<set<size_t> > sets;
   set<size_t> s;
   s.insert(0);
   sets.push_back(s);
   
   for ( size_t h = 0 ; h < H ; ++h ){
      for ( size_t w = 0 ; w < W ; ++w ){
         size_t minh = 0;
         size_t minw = 0;
         size_t small = 100000;
         size_t ith = 0;
         if( h != 0 ){
            if ( maps[h-1][w] < small ){
               small = maps[h-1][w]; 
               minh = h-1;
               minw = w;
               ++ith;
            }
         }
         if( w != 0 ){
            if ( maps[h][w-1] < small ){
               small = maps[h][w-1]; 
               minh = h;
               minw = w-1;
               ++ith;
            }
         }
         if( w != W-1 ){
            if ( maps[h][w+1] < small ){
               small = maps[h][w+1];
               minh = h;
               minw = w+1;
               ++ith;
            }
         }
         if( h != H-1 ){
            if ( maps[h+1][w] < small ){
               small = maps[h+1][w]; 
               minh = h+1;
               minw = w;
               ++ith;
            }
         }
         if ( maps[h][w] > small )
            insertSet( sets, tmp[h][w], tmp[minh][minw] );
      }
   }
   
   // merge the same set
   map<size_t, size_t> alpha;
   size_t a = 100000;
   set<size_t>::iterator it;
   map<size_t,size_t>::iterator itm;
   for ( size_t i = 0 ; i < sets.size() ; ++i ){
      if ( i == 0 ){
         for ( it=sets[i].begin(); it!=sets[i].end(); it++ ){
            alpha[*it] = 0;
         }
         ++a;
      }else{
         // check
         size_t b;
         for ( it=sets[i].begin(); it!=sets[i].end(); it++ ){
            if ( alpha.find(*it) != alpha.end() ){
               b = alpha[*it];
               break;
            }
         }
         if ( it == sets[i].end() ){
            for ( it=sets[i].begin(); it!=sets[i].end(); it++ ){
               alpha[*it] = a;
            }
            ++a;
         }else{
            for ( it=sets[i].begin(); it!=sets[i].end(); it++ ){
               alpha[*it] = b;
            }
         }
      }
   }
  
   a = 'a';
   map<size_t,char> cmap;
   for ( size_t ith = 0 ; ith < H*W ; ++ith ){
      if ( alpha.find(ith) == alpha.end() ){
         cmap[ith] = a;
         ++a;
      }else{
         if ( cmap.find(alpha[ith]) == cmap.end() ){
            cmap[alpha[ith]] = a;
            ++a;
         }
      }
   }

   for ( size_t ith = 0; ith < H*W ; ++ith ){
      if ( ith % W == 0 && ith != 0 )
         ofs << endl;
      if ( alpha.find(ith) == alpha.end() )
         ofs << (char)cmap[ith] << " ";
      else 
         ofs << (char)cmap[alpha[ith]] << " ";
   }
   ofs << endl;
}

void
case_out( ofstream& ofs, size_t ith ){
   ofs << "Case #" << ith << ":" << endl;
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
