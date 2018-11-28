#include <iostream>
#include <vector>

using namespace std;

bool findResult( string input, char& winner,bool& dotPresent ) {
  //cout<<"Input String: "<<input<<endl;
  bool foundWinner( true );
  winner = input[ 0 ];
  unsigned index = 0;
  if( winner == 'T' ) {
    winner = input[ 1 ];
    ++index;
  }
  if( winner == '.' ) {
    return !foundWinner;
  }
  
  for( ; index < input.length(); ++index ) {
    if( winner == input[ index ] || input[ index ] == 'T' ) {
      //cout<<"Matched: "<<winner<<" "<<input[ index ]<<endl;
      continue;
    }
    if( input[ index ] == '.' ) {
      winner = '.';
      dotPresent = true;
    }
    foundWinner = false;
    break;
  }//for( index );
  return foundWinner;
}

char findWinner( vector< string > matrix ) {
  bool foundWinner( false );
  char winner = '\0';
  bool dotPresent( false );
  //rowwise values !!
  for( unsigned k = 0; k < 4; ++k ) {
    foundWinner = findResult( matrix[ k ], winner, dotPresent );
    if( foundWinner ) return winner;
  }

  //cout<<"I am here1: "<<winner<<endl;
  //columnwise values !!
  for( unsigned k = 0; k < 4; ++k ) {
    string temp("");
    for( unsigned m = 0; m < 4; ++m ) {
      temp += matrix[ m ][ k ];
    }//for( m );
    foundWinner = findResult( temp, winner, dotPresent );
    if( foundWinner ) return winner;
  }//for( k );
  //cout<<"I am here2: "<<winner<<endl;
  
  //1st Diagonal !!
  string temp("");
  for( unsigned k = 0; k < 4; ++k ) {
    temp += matrix[ k ][ k ];
  }//for(k);
  foundWinner = findResult( temp, winner, dotPresent );
  if( foundWinner ) return winner;

  //cout<<"I am here3: "<<winner<<endl;
  //2nd Diagonal !!
  temp = "";
  for(int k = 0,m = 3; k < 4; ++k,--m ) {
    temp += matrix[ k ][ m ];
  }
  foundWinner = findResult( temp, winner, dotPresent );
  
  //cout<<"I am here4: "<<winner<<endl;

  if( foundWinner ) return winner;
  
  if( winner != '.' ) winner = '\0';
  if( dotPresent ) winner = '.';
  return winner;
}

int main() 
{
  unsigned numOfTestCases;
  vector< char > finalResult;
  cin >> numOfTestCases;
  for( unsigned k = 0; k < numOfTestCases; ++k ) {
    string input("");
    vector< string > matrix;
    for( unsigned m = 0; m < 4; ++m ) {
      cin >> input;
      matrix.push_back( input );
    }//for( m );
    finalResult.push_back( findWinner( matrix ) );
    //cin >> input;
  }//for( k );
  
  for( unsigned k = 0; k < finalResult.size(); ++k ) {
    if( finalResult[ k ] == '\0')
      cout<<"Case #"<<k+1<<": "<<"Draw"<<endl;
    else if( finalResult[ k ] == '.')
      cout<<"Case #"<<k+1<<": "<<"Game has not completed"<<endl;
    else
      cout<<"Case #"<<k+1<<": "<<finalResult[k]<<" won"<<endl;
  }//for( k );
  return 0;
}