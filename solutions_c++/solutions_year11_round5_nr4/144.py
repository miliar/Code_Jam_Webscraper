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

string doit( FileReader& fin )
{
   string a = fin.readString();
   int d = (a.length()+3)/4;
   
   __int64 value = 0;
   __int64 mask = 0;
   for ( int i = 0; i < (int)a.length(); i++ )
   {
      value = value*2 + (a[i]=='1');
      mask = mask*2 + (a[i]!='?');
   }

   __int64 ans = 0;
   for ( __int64 i = 0; ; i++ )
   {
      if ( ((i*i) & mask) == value ) { ans = i*i; break; }
   }


   //set<int> st;
   //for ( int i = 1024; i < 2048; i++ )
   //   st.insert( (i*i) & 1023 );

   string s;
   while ( ans ) { s += char('0'+ans%2); ans/=2; }
   reverse( s.begin(), s.end() );
   return s;
}

void main()
{
   FileReader fin( "D-small-attempt0 (1).in" );
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