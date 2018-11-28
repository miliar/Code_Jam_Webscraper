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

char line[1024];


double CalcSliver( double x1, double y1, double x2, double y2, double rad )
{

    //printf("called calcsliver with %f %f %f %f %f\n", x1, y1, x2, y2, rad );
    // to calc triangle area, we can bisect it, make 2 right triangles..
    double aLen = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
    //printf("aLen = %f... rad is %f\n", aLen, rad );
    double triangleArea = (aLen * sqrt( 4*rad*rad - aLen*aLen )) / 4.0;

    //printf("triangle area = %f\n", triangleArea );

    // find the angle
    double angle = asin( (aLen/2.0) / rad ) * 2;

    //printf( "angle = %f\n", angle );

    // find area of the wedge:
    double wedgeArea = (angle * (PI * rad * rad )) / (2.0*PI);

    //printf("wedge area = %f\n", wedgeArea);

    double ret = wedgeArea - triangleArea;

    //printf("slice had area %f\n", ret);
    
    return ret;
}

double EscapeArea( double rad, double lowx, double lowy, double highx, double highy )
{
    //printf("called escapearea with rad = %f, lowx = %f, lowy = %f, highx = %f, highy = %f\n", rad, lowx, lowy, highx, highy );

    if( highx <= lowx || highy <= lowy )
    {
        //printf("returned_flytoobig %f\n", 0);
        return 0;
    }

    double furthest = sqrt( highx*highx + highy*highy );
    double closest = sqrt(lowx*lowx + lowy*lowy );

    

    if( furthest <= rad ) // the box is not affected by the edge
    {
        double ret = (highx-lowx) * (highy - lowy );
        //printf("returned_simple %f\n", ret);
        return ret;
    }
    if( closest >= rad ) // the box is outside of the range we care about
    {
        //printf("returned_out %f\n", 0);
        return 0;
    }

    // otherwise our box is impacted by the rim..
    //check where it intersects the top of our box..
   
    double topIntersect = 0;
    double bottomIntersect = 0;
    double rightIntersect = 0;
    double leftIntersect = 0;

    // see if top is intersected
    double tmp = (rad * rad) - (highy*highy);
    if( tmp > 0 )
    {
        double xIntercept = sqrt(tmp);
        if( xIntercept >= lowx && xIntercept <= highx )
        {
            // the top is intersected
            topIntersect = xIntercept;
        }
    }

    // see if bottom is intersected
    tmp = (rad * rad) - (lowy*lowy);
    if( tmp > 0 )
    {
        double xIntercept = sqrt(tmp);
        if( xIntercept >= lowx && xIntercept <= highx )
        {
            // the top is intersected
            bottomIntersect = xIntercept;
        }
    }

    // see if right is intersected
    tmp = (rad * rad) - (highx*highx);
    if( tmp > 0 )
    {
        double yIntercept = sqrt(tmp);
        if( yIntercept >= lowy && yIntercept <= highy )
        {
            // the top is intersected
            rightIntersect = yIntercept;
        }
    }

    // see if left is intersected
    tmp = (rad * rad) - (lowx*lowx);
    if( tmp > 0 )
    {
        double yIntercept = sqrt(tmp);
        if( yIntercept >= lowy && yIntercept <= highy )
        {
            // the top is intersected
            leftIntersect = yIntercept;
        }
    }

    if( topIntersect > 0 && rightIntersect > 0 )
    {
        double ret = 0;
        // add left block
        ret += (topIntersect - lowx) * (highy - lowy );
        // add remaining lower block
        ret += (highx - topIntersect) * (rightIntersect - lowy);
        // add remaining triagle
        ret += (highx - topIntersect) * (highy - rightIntersect) * 0.5;
        // need to add the remaining sliver..
        ret += CalcSliver( topIntersect, highy, highx, rightIntersect, rad );
        //printf("topintersect is %f .. rightintersect is %f\n", topIntersect, rightIntersect);
        //printf("returned_a %f\n", ret);
        return ret;
    }
    else if( leftIntersect > 0 && rightIntersect > 0 )
    {
        double ret = 0;
        double lowi = min(leftIntersect, rightIntersect);
        double highi = max(leftIntersect, rightIntersect);
        // add bottom part
        ret += (lowi-lowy) * (highx - lowx);
        // add triangle
        ret += (highi-lowi) * (highx - lowx) * 0.5;
        // need to add remaining sliver..
        ret += CalcSliver( lowx, leftIntersect, highx, rightIntersect, rad );
        //printf("returned_b %f\n", ret);
        return ret;
    }
    else if( topIntersect > 0 && bottomIntersect > 0 )
    {
        double ret = 0;
        double lowi = min(topIntersect, bottomIntersect);
        double highi = max(topIntersect, bottomIntersect);
        // add left part
        ret += (lowi-lowx) * (highy - lowy);
        // add triangle
        ret += (highi-lowi) * (highy - lowy) * 0.5;
        // need to add remaining sliver..
        ret += CalcSliver( topIntersect, highy, bottomIntersect, lowy, rad );
        //printf("returned_c %f\n", ret);
        return ret;
    }
    else if( leftIntersect >= 0 && bottomIntersect >= 0 )
    {
        double ret = 0;
        //add triangle
        ret += (leftIntersect - lowy ) * (bottomIntersect - lowx ) * 0.5;
        //printf("small triangle area = %f\n", ret);
        // need to add remaining sliver
        ret += CalcSliver( lowx, leftIntersect, bottomIntersect, lowy, rad );
        //printf("returned_d %f\n", ret);
        return ret;
    }
    else
    {
        ;//printf("baaaaaaaaad\n");
    }

    //printf("returned_end %f\n", 0);
    return 0;
}

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
            if( ! getLine( in, line, sizeof(line) )  ) return 0;
            vector<string> vs = tokenize(string(line), " ");
            if( vs.size() != 5 )
            {
                return 0;
            }
            double f = parse(vs[0], (double)0 );
            double R = parse(vs[1], (double)0 );
            double t = parse(vs[2], (double)0 );
            double r = parse(vs[3], (double)0 );
            double g = parse(vs[4], (double)0 );


            double quadrantArea = (PI * R * R) / 4.0;
            double escapetotal = 0.0;

            double escapeR = R - t - f;
            double escape_r = r + f;

            for( double lowx = escape_r; lowx <= escapeR; lowx += (g + r + r) )
            {
                double highx = lowx + g - f - f;
                for( double lowy = escape_r; lowy <= escapeR; lowy += (g + r + r) )
                {
                    double highy = lowy + g - f - f;
                    escapetotal += EscapeArea( escapeR, lowx, lowy, highx, highy );
                }
            }

            double ret = 1.0 - (escapetotal/quadrantArea);

            cout << "Case #" << setprecision(8) << fixed << i << ": " << ret << endl;
        }

        fclose(in);  
    }

    return 0;    
}

