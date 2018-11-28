#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include "bigint-2009.05.03/BigInteger.hh"
#include "bigint-2009.05.03/BigIntegerUtils.hh"

BigInteger gcd( const BigInteger& a, const BigInteger& b ) { return b == 0 ? a : gcd( b, a%b ); }

using namespace std;

class filein : public ifstream
{
public:
   filein( const string& filename ) : ifstream( filename.c_str() ) {}
   string   readStr() { string s; *this >> s; return s; }
   string   readLine() { char c='\n'; while ( isspace( c ) ) if ( eof() ) return string(); else c = get(); char buf[100000]; getline( buf, sizeof(buf) ); return string()+c+buf; }
   int      readInt() { int x; *this >> x; return x; }
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

void main()
{
   filein fin( "B-large.in" );
   fileout fout( "out.txt" );
   int T = fin.readInt();

   for ( int q = 0; q < T; q++ )
   {
      int N = fin.readInt();
      vector<int> v;
      BigInteger x, y;
      for ( int i = 0; i < N; i++ ) 
      {
         BigInteger b = stringToBigInteger( fin.readStr() );
         if ( i == 0 ) { x = b; continue; }
         if ( i == 1 ) { y = b-x > 0 ? b-x : x-b; continue; }
         if ( y < 0 ) y = -y;
         y = gcd( y, b-x > 0 ? b-x : x-b );
      }      
      
      fout << "Case #" << q+1 << ": " << (y-x%y)%y << endl;
   }

}