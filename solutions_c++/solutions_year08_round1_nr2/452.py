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

int NO = 0;
int LIKES = 1;
int MALT = 2;

const int MAX_FLAVS = 10;
const int MAX_PPL = 100;

int adj[MAX_PPL+1][MAX_FLAVS+1];

bool canEat[MAX_PPL+1];

int bitcount(int x)
{
    int ret = 0;
    while( x != 0 )
    {
        if( x % 2 == 1 ) ret ++;
        x = x / 2;
    }
    return ret;
}

int __cdecl main (int argc, char **argv)
{

    if( argc == 2 )
    {
        FILE * in = fopen( argv[1], "r" );
        if( ! in ) return 0;

        if( ! getLine( in, line, sizeof(line) )  ) return 0;

        int C = parse(string(line), 0);

        for( int i = 1; i <= C; i++ )
        {
            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            int N = parse(string(line), 0);

            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            int M = parse(string(line), 0);

            //clear matrix
            for( int k = 0; k <= MAX_PPL; k++ )
            {
                for( int h = 0; h <= MAX_FLAVS; h++ )
                {
                    adj[k][h] = 0;
                }
            }

            for( int j = 0; j < M; j++ )
            {
                if( ! getLine( in, line, sizeof(line) )  ) return 0;
                vector<string> vs = tokenize(string(line), " ");
                vector<int> vi = vparse( vs, 0 );

                for( size_t w = 1; w + 1 <= vi.size(); w += 2 )
                {
                    int p = j+1; // person
                    int f = vi[w]; // flav
                    int m = vi[w+1]; //malted?

                    if( m > 0 )
                    {
                        adj[p][f] = adj[p][f] | MALT;
                    }
                    else adj[p][f] = adj[p][f] | LIKES;
                }
            }

            // everything is read in.. now just do our calculations..

            //loop through all subsets?
            int best = -1;
            for( int j = 0; j <= 1024; j++ )
            {
                // if j has fewer bits than best
                if( best == -1 || bitcount(j) < bitcount(best) )
                {
                    // if everyone can eat given items in j..

                    for( int k = 1; k <= M; k++ )
                    {
                        canEat[k] = false;
                        for( int h = 1; h <= N; h++ )
                        {
                            // is bit h set in t? if so this flavor is malted
                            bool malted = (j >> (h-1)) & 1;

                            if( (malted && (adj[k][h] & MALT) > 0) || (!malted && (adj[k][h] & LIKES) > 0 ) )
                            {
                                canEat[k] = true;
                            }
                        }
                    }

                    bool ret = true;
                    for( int k = 1; k <= M; k++ ) 
                        ret = ret && canEat[k];
                    if( ret )
                    {
                        best = j;
                    }
                }
                
            }
            

            cout << "Case #" << i << ": ";
            if( best >= 0 )
            {
                for( int j = 0; j < N; j++ )
                {
                    if( (best >> j) & 1 == 1 ) cout << "1";
                    else cout << "0";

                    if( j+1 < N )
                    {
                        cout << " ";
                    }
                }
            }
            else
            {
                cout << "IMPOSSIBLE";
            }
            cout << endl;
        }

        fclose(in);  
    }

    return 0;    
}

