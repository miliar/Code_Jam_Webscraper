#include <iostream>

using namespace std;

bool board[2][100][100];
int current = 0;

bool next_step()
{
  bool good = false;
  for ( int r=0; r<100; ++r )
    for ( int c=0; c<100; ++c )
    {
      bool north = r > 0 and board[current][r - 1][c];
      bool west = c > 0 and board[current][r][c - 1];
      if ( north and west )
        board[1 - current][r][c] = true;
      else if ( not north and not west )
        board[1 - current][r][c] = false;
      else
        board[1 - current][r][c] = board[current][r][c];
      if ( board[1 - current][r][c] )
        good = true;
    }
  current = 1 - current;
  return good;
}

void read()
{
  current = 0;
  for ( int r=0; r<100; ++r )
    for ( int c=0; c<100; ++c )
      board[0][r][c] = false;
  int R;
  cin >> R;
  for ( int r=0; r<R; ++r )
  {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    for ( int x=x1; x<=x2; ++x )
      for ( int y=y1; y<=y2; ++y )
        board[0][x - 1][y - 1] = true;
  }
}

int main()
{
  int C;
  cin >> C;
  for ( int c=1; c<=C; ++c )
  {
    read();
    int cnt = 1;
    while ( next_step() )
      ++cnt;
    cout << "Case #" << c << ": " << cnt << endl;
  }
  return 0;
}
