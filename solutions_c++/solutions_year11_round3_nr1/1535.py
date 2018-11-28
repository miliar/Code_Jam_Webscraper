#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;


bool findSquareTiles( vector< string >& tiles )
{
  for( unsigned k = 0; k < tiles.size(); ++k ) {
    for( unsigned m = 0; m < tiles[k].length(); ++m ) {
      if( ( tiles[k][m] == '.' ) || ( tiles[k][m] == '/' ) || ( tiles[k][m] == '\\' ) ) 
        continue;
      tiles[k][m] = '/';
      if( ( m+1 < tiles[k].length() && k < tiles.size() ) && tiles[k][m+1] == '#' )
        tiles[k][m+1] = '\\';
      else 
        return false;
      if( ( m < tiles[k].length() && k+1 < tiles.size() ) && tiles[k+1][m] == '#' )
        tiles[k+1][m] = '\\';
      else 
        return false;
      if( ( m+1 < tiles[k].length() && k+1 < tiles.size() ) && tiles[k+1][m+1] == '#' )
        tiles[k+1][m+1] = '/';
      else
        return false;
    }//for( m );
  }//for( k );
  return true;
}

int main()
{
  vector< vector< string > > finalRes;
  int numOfTestCases;
  scanf( "%d", &numOfTestCases );
  for( int i = 0; i < numOfTestCases; ++i ) {  

    int numOfRows;
    scanf( "%d", &numOfRows );
    char space;
    scanf( "%c", &space );
    int numOfCols;
    scanf( "%d", &numOfCols );

    vector< string >tiles;
    for( int m = 0; m < numOfRows; ++m ) {
      string str;
      char temp[55];
      scanf("%s", temp);
      str = temp;
      tiles.push_back( str );
    }
    bool res = findSquareTiles( tiles );
    if( res )
      finalRes.push_back( tiles );
    else {
      vector< string > str;
      str.push_back( "Impossible" );
      finalRes.push_back( str );
    }
  }//for( numOfTestCases );
  ofstream myfile;
  myfile.open ("D:\\JunkStuffs\\Junk_Codes\\GooggleCodeJam2011\\GooggleCodeJam2011\\example.txt");
  for( unsigned i = 0; i < finalRes.size(); ++i ) {
    myfile <<"Case #"<<i+1<<": "<<endl;
    for( unsigned j = 0; j < finalRes[i].size(); ++j ) {
      string str = finalRes[i][j];
      myfile << str <<"\n"<<endl;
    }
  }
  myfile.close();
}