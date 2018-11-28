#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <Windows.h>

using namespace std;

class FileReader : public ifstream
{
public:
   FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
   int readInt() { int x; *this >> x; return x; }
   //string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
   //vector<string> readLines( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readLine() ); return v; }
   string readString() { string x; *this >> x; return x; }
   vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
   __int64 readInt64() { __int64 x; *this >> x; return x; }
};


//class XYf
//{
//public:
//	XYf() { x = y = 0; }
//	XYf( const double& xx, const double& yy ) { x = xx; y = yy; }
//
//	XYf operator+( const XYf& p ) const { return XYf(x + p.x, y + p.y); }
//	XYf operator-( const XYf& p ) const { return XYf(x - p.x, y - p.y); }
//	XYf operator-() const { return XYf() - *this; }
//	XYf operator*(double m) const { return XYf(x * m, y * m); }
//	XYf operator/(double m) const { return XYf(x / m, y / m); }	
//
//	double operator*( const XYf& p ) { return x * p.x + y * p.y; }	
//	double operator^( const XYf& p ) { return x * p.y - y * p.x; }
//
//   double len2() const { return x*x + y*y; }
//	double len() const;
//   double dist2( const XYf& p ) const { return (*this-p).len2(); }
//   double dist( const XYf& p ) const { return ::sqrt( dist2( p ) ); }
//
//public:
//	double x, y;
//};

class FileWriter : public ofstream
{
public:
   FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
   //int writeInt() { int x; *this << x; return x; }
   //int writeString( const string& str ) { *this << str; }
};

string doit( FileReader& fin )
{
   int W = fin.readInt();
   int L = fin.readInt();
   int U = fin.readInt();
   int G = fin.readInt();
   
   vector<double> hi( W + 1 );
   vector<double> lo( W + 1 );
   int x0 = 0;
   int y0 = 0;
   for ( int i = 0; i < L; i++ )
   {
      int x1 = fin.readInt();
      int y1 = fin.readInt();
      for ( int x = x0; x <= x1; x++ )
         lo[x] = y0 + double(x-x0)*(y1-y0)/(x1-x0);
      x0 = x1;
      y0 = y1;
   }
   x0 = 0;
   y0 = 0;
   for ( int i = 0; i < U; i++ )
   {
      int x1 = fin.readInt();
      int y1 = fin.readInt();
      for ( int x = x0; x <= x1; x++ )
         hi[x] = y0 + double(x-x0)*(y1-y0)/(x1-x0);
      x0 = x1;
      y0 = y1;
   }

   double totalArea = 0;
   for ( int x = 0; x < W; x++ )
      totalArea += ( hi[x]-lo[x] + hi[x+1]-lo[x+1] ) / 2.0;
   
   stringstream ss;
   ss.precision( 12 );
   for ( int i = 1; i < G; i++ )
   {
      double area = totalArea * i / G;      
      double tot = 0;
      for ( int x = 0; x < W; x++ )
      {
         double slice = ( hi[x]-lo[x] + hi[x+1]-lo[x+1] ) / 2.0;
         if ( slice >= area )
         {
            double a = hi[x]-lo[x];
            double b = hi[x+1]-lo[x+1];
            double A = (b-a)/2;
            double B = a;
            double C = -area;
            double xx;
            if ( fabs(A) > 1e-10 )
            {
               double root0 = ( -B + sqrt( B*B - 4*A*C ) ) / (2*A);
               double root1 = ( -B - sqrt( B*B - 4*A*C ) ) / (2*A);
               xx = root0 > 0 && root0 <= 1 ? root0 : root1;
            }
            else
            {
               xx = -C/B;
            }
            ss << endl << x + xx;
            break;
         }
         area -= slice;
      }
   }
   

   return ss.str();
}

void main()
{
   FileReader fin( "A-large (1).in" );
   FileWriter fout( "out.txt" );
   int T = fin.readInt();
   for ( int i = 0; i < T; i++ )
   {
      stringstream ss;
      ss << "Case #" << i+1 << ": " << doit( fin ) << endl;
      fout << ss.str().c_str();
      OutputDebugStringA( ss.str().c_str() );
   }
}