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
   vector<int> readInts( int n ) { vector<int> v(n); for ( int i = 0; i < n; i++ ) v[i] = readInt(); return v; }
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

int doit( FileReader& fin )
{
   int N = fin.readInt();
   vector<int> v = fin.readInts( N );
   vector<int> w( 11000 );
   vector<int> a;
   for ( int i = 0; i < N; i++ )
      w[v[i]]++;
   
   int LEN = 999999;
   for ( int i = 0; i < 10001; i++ )
   {
      for ( int k = w[i]; k < w[i+1]; k++ )
         a.push_back( i+1 );
      for ( int k = w[i+1]; k < w[i]; k++ )
      {
         LEN = min( LEN, i-a[0]+1 );
         a.erase( a.begin() );
      }
   }

   return LEN == 999999 ? 0 : LEN;
}

void main()
{
   FileReader fin( "B-large (1).in" );
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