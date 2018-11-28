#include <iostream>
#include <vector>
#include <string>

using namespace std;

int canPlay( const int& low, const int& high, const vector< int >& players )
{
  int res = -1;
  for( int k = low; k <= high; ++k ) {
    unsigned m( 0 );
    for( ; m < players.size(); ++m ) {
      if( !( ( players[m] % k == 0 ) || ( k % players[m] == 0 ) ) )
        break;
    }
    if( m >= players.size() ) {
      return k;
    }
  }
  return res;
}

int main()
{
  vector< int > final;
  int numOfTestCases;
  scanf( "%d", &numOfTestCases );
  for( int i = 0; i < numOfTestCases; ++i ) {  
    int numOfPlayers;
    scanf( "%d", &numOfPlayers );
    char space;
    scanf( "%c", &space );
    int lowNode;
    scanf( "%d", &lowNode );
    scanf( "%c", &space );
    int highNode;
    scanf( "%d", &highNode );

    vector< int > palyers;
    for( int m = 0; m < numOfPlayers; ++m ) {
      int player;
      scanf( "%d", &player );
      palyers.push_back( player );
    }
    int res = canPlay( lowNode, highNode, palyers );
    final.push_back( res );
  }
  for( unsigned k = 0; k < final.size(); ++k ) {
    if( final[k] == -1 )
      cout<<"Case #"<<k+1<<": "<<"NO"<<endl;
    else
       cout<<"Case #"<<k+1<<": "<<final[k]<<endl;
  }
  return 0;
}