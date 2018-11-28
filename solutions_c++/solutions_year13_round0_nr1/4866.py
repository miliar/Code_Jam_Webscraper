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
   string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
   string readString() { string x; *this >> x; return x; }
   vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
   __int64 readInt64() { __int64 x; *this >> x; return x; }
};



class FileWriter : public ofstream
{
public:
   FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
};

string doit( FileReader& fin )
{
   int linhaX[] ={0, 0, 0, 0};
   int colunaX[] = {0, 0, 0, 0};
   int diagX[] = {0, 0};
   int linhaO[] ={0, 0, 0, 0};
   int colunaO[] = {0, 0, 0, 0};
   int diagO[] = {0, 0};
   int dot = 0;
   for ( int i = 0; i < 4; i++ )
   {      
          string s = fin.readLine();          
          for ( int j = 0; j < (int) s.length(); j++ ) {
              if(s[j]=='.') { dot++; continue;}
              if(s[j]=='X' || s[j]=='T') { 
                              linhaX[i]++; 
                              colunaX[j]++;
                              if(i==j) diagX[0]++;
                              if(i+j==3) diagX[1]++;
                              }
              if(s[j]=='O' || s[j]=='T') { 
                              linhaO[i]++; 
                              colunaO[j]++;
                              if(i==j) diagO[0]++;
                              if(i+j==3) diagO[1]++;
                              }
          }
   }
   fin.readLine(); 
   for ( int i = 0; i < 4; i++ )
   {      
         if(colunaX[i]==4 || linhaX[i]==4 || diagX[(int) i/2]==4) return "X won";
         if(colunaO[i]==4 || linhaO[i]==4 || diagO[(int) i/2]==4) return "O won";
   }
   if (dot>0) return "Game has not completed";
   return "Draw";
}

int main()
{
   FileReader fin( "A-large.in" );
   FileWriter fout( "outLarge.txt" );
   int T = fin.readInt();
   fin.readLine();
   for ( int i = 0; i < T; i++ )
   {
      stringstream ss;
      ss << "Case #" << i+1 << ": " << doit( fin ) << endl;
      fout << ss.str().c_str();
      OutputDebugStringA( ss.str().c_str() );
   }
   
   return 0;
}
