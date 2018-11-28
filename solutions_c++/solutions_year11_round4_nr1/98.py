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

struct Walkway
{
   int B, E, w;
   bool operator<( const Walkway& rhs ) { return w < rhs.w; }
};

string doit( FileReader& fin )
{
   int X = fin.readInt();
   int S = fin.readInt();
   int R = fin.readInt();
   double t = fin.readInt();
   int N = fin.readInt();
   vector<Walkway> walkways;
   Walkway slow;
   slow.B = 0;
   slow.E = 0;
   slow.w = 0;
   int prev = 0;
   for ( int i = 0; i < N; i++ )
   {
      Walkway ww;
      ww.B = fin.readInt();
      ww.E = fin.readInt();
      ww.w = fin.readInt();
      walkways.push_back( ww );
      slow.E += ww.B - prev;
      prev = ww.E;
   }
   slow.E += X - prev;
   walkways.push_back( slow );
   sort( walkways.begin(), walkways.end() );

   double totalTime = 0;
   for ( int i = 0; i < (int) walkways.size(); i++ )
   {
      double dist = walkways[i].E - walkways[i].B;
      int walkSpeed = S + walkways[i].w;
      int runSpeed = R + walkways[i].w;

      double runTime = dist / runSpeed;
      if ( runTime <= t )
      {
         t -= runTime;
         totalTime += runTime;
         continue;
      }
      double runDist = runSpeed * t;
      totalTime += t;
      t = 0;
      dist -= runDist;
      totalTime += dist / walkSpeed;
   }

   stringstream ss;
   ss.precision( 12 );
   ss << totalTime;
   return ss.str();
}

void main()
{
   FileReader fin( "A-large.in" );
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