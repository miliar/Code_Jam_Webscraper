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
 for( int i = 0; i < vs.size(); i++ )
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

int best = 200*1000000;

void perm( vector<int> &v, vector<int> &w, size_t idx )
{
	if( idx >= w.size() )
	{
		// compute the score;
		int total = 0;
		for( size_t i = 0; i < w.size(); i++ )
		{
			total += v[i]*w[i];
		}
		if( total < best )
		{
			best = total;
		}
	}
	else
	{
		// for each item remaining in w, swap it with index position and recurse
		for( size_t i = idx; i < w.size(); i++ )
		{
			int orig = w[idx];
			int sw = w[i];
			w[idx] = sw;
			w[i] = orig;
			perm( v, w, idx+1 );
			w[idx] = orig;
			w[i] = sw;			
		}
	}
}

char line[1024];

int __cdecl main (int argc, char **argv)
{

    if( argc == 2 )
    {
        FILE * in = fopen( argv[1], "r" );
        if( ! in ) return 0;

        if( ! getLine( in, line, sizeof(line) )  ) return 0;

        int T = parse(string(line), 0);

        for( int i = 1; i <= T; i++ )
        {

            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            int n = parse(string(line), 0);

			// read in two vectors
            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            vector<string> vstmp = tokenize(string(line), " ");

			vector<int> v = vparse(vstmp, 0);

			if( ! getLine( in, line, sizeof(line) )  ) return 0;
            vstmp = tokenize(string(line), " ");

			vector<int> w = vparse(vstmp, 0);

			//we only need to permute the second vector

			best = 200*1000000;
			perm( v, w, 0 );


            cout << "Case #" << i << ": " << best << endl;
        }

        fclose(in);  
    }

    return 0;    
}

