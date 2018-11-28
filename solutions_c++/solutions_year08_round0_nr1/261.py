#include "stdafx.h"

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

char line[1024];

int __cdecl main (int argc, char **argv)
{
    if( argc == 2 )
    {
        FILE * in = fopen( argv[1], "r" );
        if( ! in )
        {
            printf("FAIL\n");
            return 0;
        }

        if( ! getLine( in, line, sizeof(line) )  )
        {
            printf("FAIL\n");
            return 0;
        }

        int N = parse(string(line), 0);

        for( int i = 1; i <= N; i++ )
        {
            // read # of search engines
            if( ! getLine( in, line, sizeof(line) )  )
            {
                printf("FAIL 1\n");
                return 0;
            }
            int S = parse(string(line), 0);

            for( int j = 0; j < S; j++ )
            {
                // read in the S engines.. the names don't matter
                if( ! getLine( in, line, sizeof(line) )  )
                {
                    printf("FAIL 2\n");
                    return 0;
                }
            }

            if( ! getLine( in, line, sizeof(line) )  )
            {
                printf("FAIL 3\n");
                return 0;
            }
            int Q = parse(string(line), 0);

            set<string> ss;

            int ret = 0;
            for( int j = 0; j < Q; j++ )
            {
                if( ! getLine( in, line, sizeof(line) )  )
                {
                    printf("FAIL 3\n");
                    return 0;
                }
                string s(line);
                ss.insert(s);
                if( ss.size() == S )
                {
                    ret++;
                    ss.clear();
                    ss.insert(s);
                }                
            }

            cout << "Case #" << i << ": " << ret << endl;
        }

        fclose(in);  
    }

    return 0;    
}

