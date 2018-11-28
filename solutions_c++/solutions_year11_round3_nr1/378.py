#include <vector>
#include <string>
#include <iostream>

using namespace std;

void transform(vector<string> &tiles)
{
  int R = tiles.size();
  int C = tiles[0].length();
  bool changed;
  do
  {
    changed = false;
    for ( int r = 0; r < R; ++r )
    {
      for ( int c = 0; c < C; ++c )
      {
        if ( tiles[r][c] == '#' )
        {
          if ( c == C - 1 or r == R - 1 )
            return;
          if ( tiles[r][c + 1] != '#' or tiles[r + 1][c] != '#'
              or tiles[r + 1][c + 1] != '#' )
            return;
          changed = true;
          tiles[r][c] = '/'; tiles[r][c + 1] = '\\';
          tiles[r + 1][c] = '\\'; tiles[r + 1][c + 1] = '/';
          goto more;
        }
      }
    }
  more: ;
  } while ( changed );
}


bool good(vector<string> const &tiles)
{
  int R = tiles.size();
  int C = tiles[0].length();
  for ( int r = 0; r < R; ++r )
    for ( int c = 0; c < C; ++c )
      if ( tiles[r][c] == '#' )
        return false;
  return true;
}


vector<string> read_data()
{
  int R, C;
  cin >> R >> C;
  vector<string> res;
  for ( int r = 0; r < R; ++r )
  {
    string line;
    cin >> line;
    res.push_back(line);
  }
  return res;
}


int main()
{
  int T;
  cin >> T;
  for ( int t = 1; t <= T; ++t )
  {
    vector<string> r = read_data();
    cout << "Case #" << t << ":\n";
    transform(r);
    if ( good(r) )
    {
      int R = r.size();
      for ( int i = 0; i < R; ++i )
        cout << r[i] << '\n';
    }
    else
    {
      cout << "Impossible\n";
    }
  }
  return 0;
}
