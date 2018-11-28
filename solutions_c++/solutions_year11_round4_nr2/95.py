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

__int64 XX[512][512] = {0};
__int64 YY[512][512] = {0};
__int64 MM[512][512] = {0};


string doit( FileReader& fin )
{
   int SY = fin.readInt();
   int SX = fin.readInt();
   int D = fin.readInt();
   vector<string> m = fin.readStrings( SY );
   
   for ( int y = 1; y <= SY; y++ )
   for ( int x = 1; x <= SX; x++ )
   {
      MM[y][x] = MM[y-1][x] + MM[y][x-1] - MM[y-1][x-1] + (m[y-1][x-1]-'0');
      XX[y][x] = XX[y-1][x] + XX[y][x-1] - XX[y-1][x-1] + (m[y-1][x-1]-'0') * (x-1);
      YY[y][x] = YY[y-1][x] + YY[y][x-1] - YY[y-1][x-1] + (m[y-1][x-1]-'0') * (y-1);
   }

   for ( int K = 500; K >= 3; K-- )
   {
      int squares = K*K-4;
      for ( int y = 0; y+K <= SY; y++ )
      for ( int x = 0; x+K <= SX; x++ )
      {
         __int64 MSUM = MM[y+K][x+K] - MM[y][x+K] - MM[y+K][x] + MM[y][x] - (m[y][x]-'0')   - (m[y+K-1][x]-'0')         - (m[y][x+K-1]-'0')         - (m[y+K-1][x+K-1]-'0');
         __int64 XSUM = XX[y+K][x+K] - XX[y][x+K] - XX[y+K][x] + XX[y][x] - (m[y][x]-'0')*x - (m[y+K-1][x]-'0')*x       - (m[y][x+K-1]-'0')*(x+K-1) - (m[y+K-1][x+K-1]-'0')*(x+K-1);
         __int64 YSUM = YY[y+K][x+K] - YY[y][x+K] - YY[y+K][x] + YY[y][x] - (m[y][x]-'0')*y - (m[y+K-1][x]-'0')*(y+K-1) - (m[y][x+K-1]-'0')*y       - (m[y+K-1][x+K-1]-'0')*(y+K-1);
         __int64 expectedXSUM2 = (x*2+(K-1))*MSUM;
         __int64 expectedYSUM2 = (y*2+(K-1))*MSUM;
         if ( XSUM*2 == expectedXSUM2 && YSUM*2 == expectedYSUM2 )
         {
            stringstream ss;
            ss << K;
            return ss.str();
         }
      }
   }
   return "IMPOSSIBLE";
}

void main()
{
   FileReader fin( "B-large.in" );
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