#pragma comment(linker, "/SUBSYSTEM:windows /ENTRY:mainCRTStartup") // suppress console window
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include "bigint-2009.05.03/BigInteger.hh" //http://mattmccutchen.net/bigint/
#include "bigint-2009.05.03/BigIntegerUtils.hh"
#include "Utl.h"

BigInteger gcd( const BigInteger& a, const BigInteger& b ) { return b == 0 ? a : gcd( b, a%b ); }

using namespace std;

class filein : public ifstream
{
public:
   filein( const string& filename ) : ifstream( filename.c_str() ) {}
   string   readStr() { string s; *this >> s; return s; }
   string   readLine() { char c='\n'; while ( isspace( c ) ) if ( eof() ) return string(); else c = get(); char buf[100000]; getline( buf, sizeof(buf) ); return string()+c+buf; }
   int      readInt() { int x; *this >> x; return x; }
   vector<int>    readInts( int num )     { vector<int> v; for ( int i = 0; i < num; i++ ) v.push_back( readInt() ); return v; }
   vector<string> readStrings( int num )  { vector<string> v; for ( int i = 0; i < num; i++ ) v.push_back( readStr() ); return v; }
};
class fileout : public ofstream
{
public:
   fileout( const string& filename ) : ofstream( filename.c_str() ) {}
};

string NUM( int x ) { stringstream ss; ss << x; return ss.str(); }


//
//__int64 doit( filein& fin )
//{
//   int q = fin.readInt();
//
//
//   
//   return 0;
//}
//
//void main()
//{
//   filein fin( "in.txt" );
//   fileout fout( "out.txt" );
//   trace.setFile( fout );
//
//   int numCases = fin.readInt();
//
//   for ( int q = 0; q < numCases; q++ )
//   {      
//      trace << "Case #" << q+1 << ": " << doit( fin ) << endl;
//   }
//}
//
//int m[64][64];
//int N;

//void flipdiag()
//{
//   for ( int y = 0; y <= N-1; y++ )
//   for ( int x = 0; x <= N-1; x++ )
//      swap( m[y][x], m[N-1-x][N-1-y] );
//}
//void fliphorz()
//{
//   for ( int y = 0; y <= N-1; y++ )
//   for ( int x = 0; x < N/2; x++ )
//      swap( m[y][x], m[y][N-1-x] );
//}
//
//bool sym( int S )
//{
//   for ( int y = 0; y <= S; y++ )
//   for ( int x = 0; x <= S; x++ )
//      if ( m[y][x] != m[S-x][S-y] )
//         return false;
//   return true;
//}
//
//int sym()
//{
//   for ( int S = N-1; S >= 0; S-- )
//      if ( sym( S ) )
//         return S;
//   return -1;
//}
//
//int symvert()
//{
//   flipdiag();
//   int s = sym();
//   flipdiag();
//   return max( s, sym() );
//}
//
//int symhorz()
//{
//   fliphorz();
//   int s = symvert();
//   fliphorz();
//   return s;
//}

//bool cando( int sum, int dif )
//{
//   for ( int y = 0; y < N; y++ )
//   for ( int x = 0; x < N; x++ )
//   {
//      int nx = sum-y;
//      int ny = sum-x;
//      if ( nx < 0 || nx >= N ) continue;
//      if ( ny < 0 || ny >= N ) continue;
//      if ( m[ny][nx] != m[y][x] ) return false;
//   }
//   for ( int y = 0; y < N; y++ )
//   for ( int x = 0; x < N; x++ )
//   {
//      int nx = dif+y;
//      int ny = -dif+x;
//      if ( nx < 0 || nx >= N ) continue;
//      if ( ny < 0 || ny >= N ) continue;
//      if ( m[ny][nx] != m[y][x] ) return false;
//   }
//   return true;
//}
//
//__int64 doit( filein& fin )
//{
//   N = fin.readInt();
//   for ( int r = 0; r < N; r++ )
//      for ( int i = 0; i <= r; i++ )
//         m[r-i][i] = fin.readInt();
//   for ( int r = N-2; r >= 0; r-- )
//      for ( int i = 0; i <= r; i++ )
//         m[N-1-i][N-1-r+i] = fin.readInt();
//
//   int newsize = 2*N-1;
//   for ( int sum = 0; sum <= 2*N-2; sum++ )
//   for ( int dif = -N+1; dif < N; dif++ )
//   {
//      int ns = N + abs(N-1-sum) + abs(dif);
//      if ( ns >= newsize ) continue;
//      if ( cando( sum, dif ) )
//         newsize = ns;
//   }
//         
//   return newsize*newsize-N*N;
//}
//
//void main()
//{
//   filein fin( "A-small-attempt1 (1).in" );
//   fileout fout( "out.txt" );
//   trace.setFile( fout );
//
//   int numCases = fin.readInt();
//
//   for ( int q = 0; q < numCases; q++ )
//   {      
//      trace << "Case #" << q+1 << ": " << doit( fin ) << endl;
//   }
//}

//int P;
//int N;
//vector<int> M;
//vector<vector<int> > prices;
//__int64 cache[1024][11][11];
//__int64 go( int lo, int round, int misses )
//{
//   if ( round < 0 )
//   {
//      return misses <= M[lo] ? 0 : (1LL<<50);
//   }
//   if ( cache[lo][round][misses] != -1 ) return cache[lo][round][misses];
//   int price = prices[round][lo>>(round+1)];
//   
//   __int64 a = go( lo, round-1, misses+1 ) + go( lo+(1<<round), round-1, misses+1 );
//   __int64 b = go( lo, round-1, misses )   + go( lo+(1<<round), round-1, misses ) + price;
//
//   return cache[lo][round][misses] = min( a, b );
//}
//
//__int64 doit( filein& fin )
//{
//   memset( cache, -1, sizeof(cache) );
//   P = fin.readInt();
//   N = 1 << P;
//   M = fin.readInts( N );
//   prices.clear();
//   for ( int i = 0; i < P; i++ )
//   {
//      prices.push_back( fin.readInts( 1 << (P-i-1) ) );
//   }
//      
//   __int64 ret = go( 0, P-1, 0 );
//   return ret;
//}
//
//void main()
//{
//   filein fin( "B-large (2).in" );
//   fileout fout( "out.txt" );
//   trace.setFile( fout );
//
//   int numCases = fin.readInt();
//
//   for ( int q = 0; q < numCases; q++ )
//   {      
//      trace << "Case #" << q+1 << ": " << doit( fin ) << endl;
//   }
//}

//char m[128][128];
//
//bool go()
//{
//   bool empty = true;
//   for ( int y = 100; y > 0; y-- )
//   for ( int x = 100; x > 0; x-- )
//   {
//      if ( m[y-1][x] & m[y][x-1] ) m[y][x] = 1;
//      if ( !(m[y-1][x] | m[y][x-1]) ) m[y][x] = 0;
//      if ( m[y][x] ) empty = false;
//   }
//   return empty;
//}
//
//int len( int x, int y )
//{
//
//}
//
string doit( filein& fin )
{
   int N = fin.readInt();
   vector<int> v = fin.readInts( N );

   int xor = 0;
   int sum = 0;
   int least = 99999999;
   for each ( int x in v )
   {
      xor ^= x;
      sum += x;
      least = min( least, x );
   }

   if ( xor ) return "NO";

   return NUM( sum-least );
}

void main()
{
   filein fin( "C-large.in" );
   fileout fout( "out.txt" );
   trace.setFile( fout );

   int numCases = fin.readInt();

   for ( int q = 0; q < numCases; q++ )
   {      
      trace << "Case #" << q+1 << ": " << doit( fin ) << endl;
   }
}
