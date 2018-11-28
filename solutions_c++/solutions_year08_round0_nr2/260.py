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

int departureTimesA[1441];
int arrivalTimesA[1441];

int departureTimesB[1441];
int arrivalTimesB[1441];

int trainsA[1441];
int trainsB[1441];

int __cdecl main (int argc, char **argv)
{

    if( argc == 2 )
    {
        FILE * in = fopen( argv[1], "r" );
        if( ! in ) return 0;

        if( ! getLine( in, line, sizeof(line) )  ) return 0;

        int N = parse(string(line), 0);

        for( int i = 1; i <= N; i++ )
        {
            memset(departureTimesA, 0, sizeof(departureTimesA));
            memset(arrivalTimesA, 0, sizeof(arrivalTimesA));
            memset(departureTimesB, 0, sizeof(departureTimesB));
            memset(arrivalTimesB, 0, sizeof(arrivalTimesB));
            memset(trainsA, 0, sizeof(trainsA));
            memset(trainsB, 0, sizeof(trainsB));

            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            int T = parse(string(line), 0);

            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            vector<string> vstmp = tokenize(string(line), " ");
            if( vstmp.size() != 2 ) return 0;
            int NA = parse(vstmp[0], 0);
            int NB = parse(vstmp[1], 0);

            // fill in some stuff for A-->B
            for( int j = 0; j < NA; j++ )
            {
                if( ! getLine( in, line, sizeof(line) )  ) return 0;
                vector<string> vs = tokenize(string(line), " ");
                if( vs.size() != 2 ) return 0;

                vector<string> vsdepart = tokenize(vs[0], ":");
                if( vsdepart.size() != 2 ) return 0;

                vector<string> vsarrive = tokenize(vs[1], ":");
                if( vsarrive.size() != 2 ) return 0;

                int arriveB = 60 * parse(vsarrive[0],0) + parse(vsarrive[1],0);
                int departA = 60 * parse(vsdepart[0],0) + parse(vsdepart[1],0);

                departureTimesA[departA]++;
                //cout << "depart A: " << departA << " ..ntimes = " << departureTimesA[departA] << endl;
                arrivalTimesB[arriveB]++;
                //cout << "arrive B: " << arriveB << " ..ntimes = " << arrivalTimesB[arriveB] << endl;
            }

            // fill in some stuff for B-->A
            for( int j = 0; j < NB; j++ )
            {
                if( ! getLine( in, line, sizeof(line) )  ) return 0;
                vector<string> vs = tokenize(string(line), " ");
                if( vs.size() != 2 ) return 0;

                vector<string> vsdepart = tokenize(vs[0], ":");
                if( vsdepart.size() != 2 ) return 0;

                vector<string> vsarrive = tokenize(vs[1], ":");
                if( vsarrive.size() != 2 ) return 0;

                int arriveA = 60 * parse(vsarrive[0], 0) + parse(vsarrive[1],0);
                int departB = 60 * parse(vsdepart[0],0) + parse(vsdepart[1],0);

                departureTimesB[departB]++;
                //cout << "depart B: " << departB << " ..ntimes = " << departureTimesB[departB] << endl;
                arrivalTimesA[arriveA]++;
                //cout << "arrive A: " << arriveA << " ..ntimes = " << arrivalTimesA[arriveA] << endl;
            }

            for( int j = 0; j <= 1440; j++ )
            {
                if( j-1 >= 0 )
                {
                    trainsA[j] = trainsA[j-1];
                }
                trainsA[j] -= departureTimesA[j];
                if( j-T >= 0 )
                {
                    trainsA[j] += arrivalTimesA[j-T];
                }

                if( j - 1 >= 0 )
                {
                    trainsB[j] = trainsB[j-1];
                }
                trainsB[j] -= departureTimesB[j];
                if( j-T >= 0 )
                {
                    trainsB[j] += arrivalTimesB[j-T];
                }
            }

            // find the most negative entry for both A and B..
            int lowA = 0, lowB = 0;
            for( int j = 0; j <= 1440; j++ )
            {
                if( trainsA[j] < lowA )
                {
                    lowA = trainsA[j];
                }
                if( trainsB[j] < lowB )
                {
                    lowB = trainsB[j];
                }
            }

            lowA = -lowA;
            lowB = -lowB;

            cout << "Case #" << i << ": " << lowA << " " << lowB << endl;
        }

        fclose(in);  
    }

    return 0;    
}

