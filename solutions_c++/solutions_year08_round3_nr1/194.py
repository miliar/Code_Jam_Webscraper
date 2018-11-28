#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <iomanip>

using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef vector<vector<string> > VVS;
typedef signed long long i64;
typedef unsigned long long u64;

const double PI = 2*acos(0.0);

#define REP(i,n) for( int i = 0; i < (n); i++)
#define FOR(i,a,b) for( int i = (a); i <= (b); i++ )
#define FORD(i,a,b) for( int i = (a); i >= (b); i-- )
#define VAR(a,b) __typeof(b) a = b
#define FOREACH(it,c) for( VAR( it, (c).begin() ); it != (c).end(); ++it )

#define PRN(X) cout << #X << " = " << X << endl

template<class T>
string str( T x ){
 ostringstream oss;
 oss << x;
 return oss.str();
}

template<class T>
T parse( const string &s , T type){
 istringstream iss(s);
 iss >> type;
 return type;
}

vector<string> tokenize( string s, string delims, bool giveDelims = false){
 vector<string> ret;
 string::size_type d=0, g=s.find_first_not_of(delims,0);
 if( giveDelims )
  for( string::size_type i = d; i < min(s.size(),g); i++)
    ret.push_back(str(s[i]));
 d = s.find_first_of(delims, g);
 while( g != string::npos){
  ret.push_back( s.substr( g, d-g));
  g = s.find_first_not_of(delims,d);
  if(giveDelims)
    for( string::size_type i = d; i < min(s.size(),g); i++)
      ret.push_back(str(s[i]));
  d = s.find_first_of(delims, g);
 }
 return ret;
}


template<class T>
vector<T> vparse( const vector<string> &vs, T ident ){
 vector<T> vt;
 for( size_t i = 0; i < vs.size(); i++ )
  vt.push_back( parse(vs[i], ident));
 return vt;
}


// get rid of trailing end of line markers
void trim( char * s ){
       while( *s != 0 ){
               if( *s == '\n' || *s == '\r' ){
                       *s = 0;
                       return;
               }
               s++;
       }
}

// gets a line from f, removing trailing end of line markers
bool getLine( FILE * f, char * line, int maxlen ){
       if( ! fgets( line, maxlen, f ) ){
               return false;
       }
       trim(line);
       return true;
}

//////////////////////////////////////////////////////////////////////////////

//////////////////////////////////////////////////////////////////////////////

char line[1024000];

vector<int> freqs;

int __cdecl main (int argc, char **argv)
{

   if( argc == 2 )
   {
       FILE * in = fopen( argv[1], "r" );
       if( ! in ) return 0;

       if( ! getLine( in, line, sizeof(line) )  ) return 0;

       int N = parse(string(line), 0);

       FOR(ii, 1, N )
       {
            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            vector<string> vt = tokenize( string(line), " " );
            if( vt.size() != 3 ) return 0;

            int maxLetters = parse(vt[0],0);
            int nKeys = parse(vt[1], 0);
            int alphSize = parse(vt[2], 0);

            freqs.clear();

            if( ! getLine( in, line, sizeof(line) )  ) return 0;

            freqs = vparse( tokenize( string(line), " " ), 0 );

            if( freqs.size() != alphSize )
            {
                return 0;
            }

            sort(freqs.begin(), freqs.end());

            u64 ret = 0;

            int idx = freqs.size()-1;
            FOR(i, 1, maxLetters ) // max letters per key
            {
                FOR(j, 1, nKeys )
                {
                    if( idx < 0 ) break;
                    ret += i * freqs[idx];
                    idx--;
                }
                if( idx < 0 ) break;
            }

            // if there's any frequency location at the idx location, this is impossible
            bool bad = false;
            FOR( i, 0, idx )
            {
                if( freqs[i] > 0 )
                {
                    bad = true;
                }
            }

            if( bad )
            {
                cout << "Case #" << ii << ": " << "Impossible" << endl;
            }
            else
            {
                cout << "Case #" << ii << ": " << ret << endl;
            }
       }

       fclose(in);
   }

   return 0;
}

