// all your base.cpp : Defines the entry point for the console application.
//

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

#include <string>
using std::string;
using std::getline;

#include <vector>
using std::vector;

#include <cmath>

void handle( int n )
{
  vector< string > board;
  string line;

  for( int i = 0; i < 5; ++i )
  {
    getline( cin, line );
    board.push_back( line );
  }
  board.pop_back(); // remove the empty line
  
  char winning = 'D';
  for( int i = 0; i < 4; ++i ) // HORIZONTAL
  {
    winning = board.at(i)[0];
    bool firstT = ( winning == 'T' ? true : false );
    for( int j = 1; j < 4; ++j )
    {
      if( firstT )
        {
          winning = board.at(i)[j];
          firstT = false;
        }
      if( !(board.at(i)[j] == winning || board.at(i)[j] == 'T') )
      {
        winning = 'D';
        break;
      }
    }
    //cout << "line: " << board.at(i) << endl;
    if( winning != 'D' ) break;
  }
  //cout << "winning: " << winning << endl;
  
  if( winning != 'X' && winning != 'O' )
  {
    for( int i = 0; i < 4; ++i ) // VERTICAL
    {
      winning = board.at(0)[i];
      bool firstT = ( winning == 'T' ? true : false );
      for( int j = 1; j < 4; ++j )
      {
        if( firstT )
          {
            winning = board.at(j)[i];
            firstT = false;
          }
        if( !(board.at(j)[i] == winning || board.at(j)[i] == 'T') )
        {
          winning = 'D';
          break;
        }
      }
      if( winning != 'D' ) break;
    }
  }
  
  if( winning != 'X' && winning != 'O' )
  {
    winning = board.at(0)[0];
    bool firstT = ( winning == 'T' ? true : false );
    for( int i = 1; i < 4; ++i ) // DIAGONAL
    {
      if( firstT )
      {
        winning = board.at(i)[i];
        firstT = false;
      }
      if( !(board.at(i)[i] == winning || board.at(i)[i] == 'T') )
      {
        winning = 'D';
        break;
      }
    }
  }

  if( winning != 'X' && winning != 'O' )
  {
    winning = board.at(0)[3];
    bool firstT = ( winning == 'T' ? true : false );
    for( int i = 1; i < 4; ++i ) // DIAGONAL
    {
      if( firstT )
      {
        winning = board.at(3-i)[i];
        firstT = false;
      }
      if( !(board.at(3-i)[i] == winning || board.at(3-i)[i] == 'T') )
      {
        winning = 'D';
        break;
      }
    }
  }
  
  switch( winning )
  {
    case 'X':
      cout << "Case #" << n << ": " << "X won" << endl;
      break;
    case 'O':
      cout << "Case #" << n << ": " << "O won" << endl;
      break;
    default:
      bool draw = true;
      for( int i = 0; i < 4; ++i )
      {
        for( int j = 0; j < 4; ++j )
        {
          if( board.at(i)[j] == '.' )
          {
            draw = false;
            cout << "Case #" << n << ": " << "Game has not completed" << endl;
            break;
          }
        }
        if( !draw ) break;
      } 
      if( draw )
        cout << "Case #" << n << ": " << "Draw" << endl;
  }
}

int main(int argc, char *argv[])
{
  int N;
  string line;
  cin >> N;
  getline( cin, line );
  for( int i = 1; i <= N; ++i ) handle( i );
  
  return 0;
}

