#include <iostream>
#include <fstream>

using namespace std;

int main()
  {
    int T;
    ifstream fin( "A-large.in" );
    ofstream fout( "A-large.out" );
    fin >> T;
    int N, K;
    for ( int i=1; i<=T; i++ )
      {
        fin >> N >> K;
        fout << "Case #" << i << ": ";
        if ( K % ( 1 << N ) == ( 1 << N ) - 1 )
          fout << "ON\n";
        else
          fout << "OFF\n";   
      }
    fin.close();
    fout.close();
  };
