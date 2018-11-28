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

i64 A[500001];
i64 speed[500001];
i64 yar[500001];

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
            vector<string> vt = tokenize(string(line), " " );
            if( vt.size() != 5 ) return 0;

            int n = parse(vt[0], 0);
            int m = parse(vt[1], 0);
            i64 X, Y, Z;
            X = parse(vt[2],X);
            Y = parse(vt[3],Y);
            Z = parse(vt[4],Z);

            // read m lines
            FOR( i, 0, m-1 )
            {
                if( ! getLine( in, line, sizeof(line) )  ) return 0;
                A[i] = parse(line, X);
            }

            // generate speed
            REP(i, n )
            {
                speed[i] = A[i%m];
                A[i%m] = (X * A[i % m] + Y * (i+1)) % Z;
            }

            // compute score
            REP(i,n) yar[i] = 1;

            FOR(i, 0, n-1 )
            {
                FOR(j, 0, i-1 )
                {
                    if( speed[j] < speed[i] )
                    {
                        yar[i] = yar[i] + yar[j];
                        yar[i] = yar[i] % 1000000007;
                    }
                }
            }

            i64 ret = 0;
            REP(i, n)
            {
                ret += yar[i];
                ret = ret % 1000000007;
            }
    

            {
                cout << "Case #" << ii << ": " << ret << endl;
            }
       }

       fclose(in);
   }

   return 0;
}

