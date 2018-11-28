#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class FileReader : public ifstream
{
public:
   FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
   int readInt() { int x; *this >> x; return x; }
   __int64 readInt64() { __int64 x; *this >> x; return x; }
};

class FileWriter : public ofstream
{
public:
   FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
   //int writeInt() { int x; *this << x; return x; }
   //int writeString( const string& str ) { *this << str; }
};

string doit( FileReader& fin )
{
   __int64 N = fin.readInt64();
   int pd = fin.readInt();
   int pg = fin.readInt();

   bool pdPossible = false;
   for ( int i = 1; i <= N && i <= 100; i++ )
      if ( pd * i % 100 == 0 )
         pdPossible = true;

   if ( !pdPossible ) return "Broken";   
   if ( pg == 0 && pd != 0 ) return "Broken";
   if ( pg == 100 && pd != 100 ) return "Broken";

   return "Possible";
}

void main()
{
   FileReader fin( "A-large.in" );
   FileWriter fout( "out.txt" );
   int T = fin.readInt();
   for ( int i = 0; i < T; i++ )
   {
      fout << "Case #" << i+1 << ": " << doit( fin ) << endl;

   }
}