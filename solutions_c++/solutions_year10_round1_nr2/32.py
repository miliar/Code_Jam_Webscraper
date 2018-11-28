#pragma comment(linker, "/SUBSYSTEM:windows /ENTRY:mainCRTStartup") // suppress console window
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include "bigint-2009.05.03/BigInteger.hh"
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

//void main()
//{
//   filein fin( "A-large-practice.in" );
//   fileout fout( "out.txt" );
//   int L, D, N;
//   fin >> L >> D >> N;
//   vector<string> dic;
//   for ( int i = 0; i < D; i++ )
//      dic.push_back( fin.getStr() );
//   for ( int q = 0; q < N; q++ )
//   {
//      string word = fin.getStr();
//      int ct = 0;
//      for ( int k = 0; k < (int) dic.size(); k++ )
//      {
//         bool isMatch = true;
//         int p = 0;
//         for ( int i = 0; i < L; i++ )
//         {
//            if ( word[p] == '(' ) 
//            {
//               bool ok = false;
//               while ( word[p] != ')' )
//               {
//                  if ( word[p] == dic[k][i] ) ok = true;
//                  p++;
//               }
//               p++;
//               if ( !ok ) { isMatch = false; break; }
//               continue;
//            }
//            if ( word[p] == dic[k][i] ) { p++; continue; } 
//            
//            isMatch = false; break;
//         }
//         if ( isMatch ) ct++;
//      }
//      fout << "Case #" << q+1 << ": " << ct << endl;
//   }
//}


//void main()
//{
//   filein fin( "C-large-practice.in" );
//   fileout fout( "out.txt" );
//   int N = fin.readInt();
//
//   int ways[20][1000] = { 0 };
//   const string M = "welcome to code jam";
//   for ( int q = 0; q < N; q++ )
//   {
//      string s = fin.readLine();
//      memset( ways, 0, sizeof(ways) );
//      ways[0][0] = 1; // [M len][s len]
//      for ( int i = 0; i <= (int)M.length(); i++ )
//      {
//         for ( int k = 0; k < (int)s.length(); k++ )
//         {
//            ways[i][k+1] += ways[i][k]; ways[i][k+1] %= 10000;
//            if ( i < M.length() && M[i] == s[k] )
//            { ways[i+1][k+1] = (ways[i+1][k+1]+ways[i][k])%10000; }
//         }
//      }
//      string z = ("0000"+NUM(ways[M.length()][s.length()]));
//      fout << "Case #" << q+1 << ": " << z.substr( z.length()-4 ) << endl;
//   }
//
//}
//void main()
//{
//   filein fin( "A-large.in" );
//   fileout fout( "out.txt" );
//   int T = fin.readInt();
//
//   for ( int q = 0; q < T; q++ )
//   {
//      int N = fin.readInt();
//      int K = fin.readInt();
//      fout << "Case #" << q+1 << ": " << ((K+1)%(1<<N) ? "OFF" : "ON") << endl;
//   }
//
//}

//void main()
//{
//   filein fin( "B-large.in" );
//   fileout fout( "out.txt" );
//   int T = fin.readInt();
//
//   for ( int q = 0; q < T; q++ )
//   {
//      int N = fin.readInt();
//      vector<int> v;
//      BigInteger x, y;
//      for ( int i = 0; i < N; i++ ) 
//      {
//         BigInteger b = stringToBigInteger( fin.readStr() );
//         if ( i == 0 ) { x = b; continue; }
//         if ( i == 1 ) { y = b-x > 0 ? b-x : x-b; continue; }
//         if ( y < 0 ) y = -y;
//         y = gcd( y, b-x > 0 ? b-x : x-b );
//      }      
//      
//      fout << "Case #" << q+1 << ": " << (y-x%y)%y << endl;
//   }
//
//}
//
//__int64 doit( filein& fin )
//{
//   int R = fin.readInt();
//   int k = fin.readInt();
//   int N = fin.readInt();
//   vector<int> v = fin.readInts( N );
//
//   __int64 tot = 0;
//   int p = 0;
//   for ( int z = 0; z < R; z++ )
//   {
//      __int64 riders = 0;
//      for ( int i = 0; i < N; i++, p=(p+1)%N )
//      {
//         if ( riders + v[p] > k ) break;
//         riders += v[p];
//         //cout << v[p] << ", ";
//      }
//      //cout << endl;
//      tot += riders;
//   }
//
//   return tot;
//}
//
//void main()
//{
//   filein fin( "C-small-attempt0.in" );
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



//__int64 doit( filein& fin )
//{
//   //static int R = fin.readInt();
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

//string doit( filein& fin )
//{
//   int N = fin.readInt();
//   int K = fin.readInt();
//   vector<string> m = fin.readStrings( N );
//   for ( int y = 0; y < N; y++ )
//   {
//      int bot = N-1;
//      for ( int x = N-1; x >= 0; x-- )
//      {
//         if ( m[y][x] == '.' ) continue;
//         swap( m[y][x], m[y][bot] );
//         bot--;
//      }
//   }
//
//   char C[2] = {'R','B'};
//   int win = 0;
//   for ( int col = 0; col < 2; col++ )
//   for ( int y = 0; y < N; y++ )
//   for ( int x = 0; x < N; x++ )
//   for ( int dx = -1; dx <= 1; dx++ )
//   for ( int dy = -1; dy <= 1; dy++ ) if ( dx || dy )
//   {
//      if ( x+dx*(K-1) < 0 || x+dx*(K-1) >= N ) continue;
//      if ( y+dy*(K-1) < 0 || y+dy*(K-1) >= N ) continue;
//      int i;
//      for ( i = 0; i < K; i++ )
//         if ( m[y+i*dy][x+i*dx] != C[col] ) break;
//      if ( i != K ) continue;
//      win |= 1 << col;
//   }
//
//   string s[] = { "Neither", "Red", "Blue", "Both" };
//   return s[win];
//}
//
//void main()
//{
//   filein fin( "A-large (1).in" );
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

int D, I, M, N;
vector<int> v;

int cache[128][256];
int go( int pos, int lastPix )
{
   if ( pos == N ) return 0;
   if ( lastPix >= 0 ) if ( cache[pos][lastPix] != -1 ) return cache[pos][lastPix];
   
   int best = 1<<30;
   if ( abs(v[pos]-lastPix) <= M || lastPix < 0 )
      best = go( pos+1, v[pos] );

   // del
   best = min( best, D + go( pos+1, lastPix ) );
   // ins
   for ( int i = 0; i <= 255; i++ ) 
      if ( abs(v[pos]-i) < abs(v[pos]-lastPix) && abs(lastPix-i) <= M )
      {
         best = min( best, I + go( pos, i ) );
      }
   // rep
   for ( int i = 0; i <= 255; i++ ) if ( abs(i-lastPix) <= M || lastPix < 0 )
      best = min( best, abs(i-v[pos]) + go( pos+1, i ) );
   if ( lastPix >= 0 )
      cache[pos][lastPix] = best;
   return best;
}

int doit( filein& fin )
{
   D = fin.readInt();
   I = fin.readInt();
   M = fin.readInt();
   N = fin.readInt();
   v = fin.readInts( N );

   memset( cache, -1, sizeof(cache) );
   return go( 0, -99999 );
}

void main()
{
   filein fin( "B-large (1).in" );
   fileout fout( "out.txt" );
   trace.setFile( fout );

   int numCases = fin.readInt();

   for ( int q = 0; q < numCases; q++ )
   {      
      trace << "Case #" << q+1 << ": " << doit( fin ) << endl;
   }
}