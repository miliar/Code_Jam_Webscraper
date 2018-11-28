#include <iostream>
using namespace std;

int main( )
{
  bool X, O, DOT;
  char field[4][5];
  int  caseCnt;

  cin >> caseCnt;
  for ( int caseNr = 1; caseNr <= caseCnt; ++caseNr )
  {
    DOT = false;
    for ( int i = 0; i < 4; ++i )
      cin >> field[i];

    // rows
    for ( int i = 0; i < 4; ++i )
    {
      X = O = true;
      for ( int j = 0; j < 4; ++j )
      {
        if ( field[i][j] == 'X' )
          O = false;
        else if ( field[i][j] == 'O' )
          X = false;
        else if ( field[i][j] == '.' )
        {
          O = false;
          X = false;
          DOT = true;
        }
      }
      if ( X )
        goto XWON;
      else if ( O )
        goto OWON;
    }

    // cols
    for ( int i = 0; i < 4; ++i )
    {
      X = O = true;
      for ( int j = 0; j < 4; ++j )
      {
        if ( field[j][i] == 'X' )
          O = false;
        else if ( field[j][i] == 'O' )
          X = false;
        else if ( field[j][i] == '.' )
        {
          O = false;
          X = false;
          DOT = true;
        }
      }
      if ( X )
        goto XWON;
      else if ( O )
        goto OWON;
    }
    // diagonals
    X = O = true;
    for ( int j = 0; j < 4; ++j )
    {
      if ( field[j][j] == 'X' )
        O = false;
      else if ( field[j][j] == 'O' )
        X = false;
      else if ( field[j][j] == '.' )
      {
        O = false;
        X = false;
        DOT = true;
      }
    }
    if ( X )
      goto XWON;
    else if ( O )
      goto OWON;
    X = O = true;
    for ( int j = 0; j < 4; ++j )
    {
      if ( field[j][3-j] == 'X' )
        O = false;
      else if ( field[j][3-j] == 'O' )
        X = false;
      else if ( field[j][3-j] == '.' )
      {
        O = false;
        X = false;
        DOT = true;
      }
    }
    if ( X )
      goto XWON;
    else if ( O )
      goto OWON;

    // result
    if ( DOT )
      cout << "Case #" << caseNr << ": Game has not completed" << endl;
    else
      cout << "Case #" << caseNr << ": Draw" << endl;
    goto next;
    XWON:
    cout << "Case #" << caseNr << ": X won" << endl;
    goto next;
    OWON:
    cout << "Case #" << caseNr << ": O won" << endl;
    goto next;
    next:;
  }
  return 0;
}