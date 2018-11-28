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

class FileWriter : public ofstream
{
public:
   FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
   //int writeInt() { int x; *this << x; return x; }
   //int writeString( const string& str ) { *this << str; }
};

class PrimeBitSieve
{
public:
   PrimeBitSieve( int n ) { init( n ); }
   ~PrimeBitSieve() {}
protected:
   void init( int n )
   {
      N = n;
      sieve.resize( 0 );
      sieve.resize( n );
      sieve[0] = true;
      sieve[1] = true;
      for ( int i = 2; i*i < N; i++ ) if ( isPrime( i ) )
         for ( int k = i*i; k < N; k += i )
            if ( !sieve[k] )
               sieve[k] = true;
   }
public:
   bool isPrime( int x ) const
   {
      return !sieve[x];
   }
protected:
   int            N;
   vector<bool>   sieve;
};

PrimeBitSieve sieve( 1100000 );

__int64 doit( FileReader& fin )
{
   __int64 N = fin.readInt64();
   if ( N == 1 ) return 0;
   __int64 ret = 1;
   for ( __int64 i = 2; i*i <= N; i++ ) if ( sieve.isPrime( (int)i ) )
   {
      __int64 x = i;
      while ( x*i <= N ) { x *= i; ret++; }
   }
   return ret;
}

void main()
{
   FileReader fin( "C-large.in" );
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